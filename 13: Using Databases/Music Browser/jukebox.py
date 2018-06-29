import sqlite3
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


class ScrollBox(tkinter.Listbox):
    """ScrollBox."""

    def __init__(self, window, **kwargs):
        """Initialize Attributes."""

        super().__init__(window, **kwargs)
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky="nsw", rowspan=1, columnspan=1, **kwargs):
        """Override grid."""

        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky="nse", rowspan=rowspan)
        self["yscrollcommand"] = self.scrollbar.set


class DataListBox(ScrollBox):
    """DataListBox subclass."""

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        """Initialize attributes."""

        self.linked_box = None
        self.link_field = None
        self.link_value = None

        super().__init__(window, **kwargs)
        self.cursor = connection.cursor()
        self.table = table
        self.field = field
        self.bind("<<ListboxSelect>>", self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ', '.join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        """Clear data."""

        self.delete(0, tkinter.END)  # range of values

    def link(self, widget, link_field):
        """Link method."""

        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        """Rebuild SQL, clear, and re insert data."""

        self.link_value = link_value  # store id so we know "master" record its populated from

        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + "=?" + self.sql_sort
            print(sql)                                     # TODO delete
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)         # TODO delete
            self.cursor.execute(self.sql_select + self.sql_sort)

        # clear listbox before reloading data
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        """Return albums for an artist."""

        if self.linked_box:
            print(self is event.widget)                    # TODO delete
            index = self.curselection()[0]
            value = self.get(index),

            # get id from db row
            # make sure were getting correct one, by including link_value if appropriate
            if self.link_value:
                value = value[0], self.link_value
                sql_where = " WHERE " + self.field + "=? AND " + self.link_field + "=?"
            else:
                sql_where = " WHERE " + self.field + "=?"
            # get artist ID from db row
            link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
            self.linked_box.requery(link_id)


if __name__ == "__main__":

    conn = sqlite3.connect('music.sqlite')

    main_window = tkinter.Tk()
    main_window.title('Music DB Browser')
    main_window.geometry('1024x768')

    main_window.columnconfigure(0, weight=2)
    main_window.columnconfigure(1, weight=2)
    main_window.columnconfigure(2, weight=2)
    main_window.columnconfigure(3, weight=1)    # spacer column on right

    main_window.rowconfigure(0, weight=1)
    main_window.rowconfigure(1, weight=5)
    main_window.rowconfigure(2, weight=5)
    main_window.rowconfigure(3, weight=1)

    # labels
    tkinter.Label(main_window, text="Artists").grid(row=0, column=0)
    tkinter.Label(main_window, text="Albums").grid(row=0, column=1)
    tkinter.Label(main_window, text="Songs").grid(row=0, column=2)

    # artists listbox
    artist_list = DataListBox(main_window, conn, "artists", "name")
    artist_list.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    artist_list.config(border=2, relief='sunken')

    artist_list.requery()

    # albums listbox
    album_lv = tkinter.Variable(main_window)
    album_lv.set(("Choose an artist",))
    album_list = DataListBox(main_window, conn, "albums", "name", sort_order=("name",))
    album_list.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    album_list.config(border=2, relief='sunken')

    artist_list.link(album_list, "artist")

    # songs listbox
    song_lv = tkinter.Variable(main_window)
    song_lv.set(("Choose an album",))
    song_list = DataListBox(main_window, conn, "songs", "title", sort_order=("track", "title"))
    song_list.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
    song_list.config(border=2, relief='sunken')

    album_list.link(song_list, "album")

    # mainloop
    main_window.mainloop()
    print("closing database connection")
    conn.close()