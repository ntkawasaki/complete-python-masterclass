class Tag(object):
    """HTML Tag."""

    def __init__(self, name, contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):
    """DocType."""

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', "")
        self.end_tag = ""  # DOCTYPE does not have an end tag


class Head(Tag):
    """Head."""

    def __init__(self, title=None):
        super().__init__("head", "")

        if title:
            self._title_tag = Tag("title", title)
            self.contents = str(self._title_tag)


class Body(Tag):
    """Body."""

    def __init__(self):
        super().__init__("body", "")  # body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)  # composition
        self._body_contents.append(new_tag)

    def display(self, file=None):  # overrides
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HTMLDoc(object):
    """HTMLDoc Class. Composed of three other classes."""

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)  # delegates add_tag to Body instance

    def display(self, file=None):
        self._doc_type.display(file=file)
        print("<HTML>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print("</HTML>", file=file)


if __name__ == "__main__":

    # my_page = HTMLDoc("Demo HTML Doc")
    #
    # my_page.add_tag("H1", "Main Heading")
    # my_page.add_tag("H2", "Sub-heading")
    # my_page.add_tag("P1", "Paragraph that will appear on page.")
    #
    # with open("test.html", "w") as test_doc:
    #     my_page.display(file=test_doc)
    #
    # my_page.display()

    new_body = Body()
    new_body.add_tag("h1", "aggregation")
    new_body.add_tag("p", "Unlike <strong>composition</strong>, aggregation uses existing instances"
                          " of objects to build up another object.")

    new_body.add_tag("p", "The composed object doesnt actually own the objects its composed of"
                          " - if its destroyed, those objects conitnue to exist.")

    new_doc_type = DocType()
    new_header = Head("Aggregation Document")
    my_page = HTMLDoc(new_doc_type, new_header, new_body)

    with open("test_3.html", "w") as test_doc_2:
        my_page.display(file=test_doc_2)
