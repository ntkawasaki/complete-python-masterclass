# how to update a shelve
import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# create the shelve
with shelve.open("recipes", writeback=True) as recipes:  # add writeback=True
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta

    # try to update, but shelve doesnt know list changed. appended to a copy
    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")

    # # one way is to use temp list and reset the values
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list  # even if we comment this out, will still be there because copied to memory

    # with writeback=True, this will work
    # simpler code, but heavier memory usage
    # recipes["soup"].append("croutons")
    recipes["soup"] = soup
    recipes.sync()  # clears cache
    soup.append("cream")  # trying to add "cream" to an object that was cleared from cache

    for snack in recipes:
        print(snack, recipes[snack])  # returns the key, value
