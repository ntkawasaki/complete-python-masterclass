def spam_1():

    def spam_2():

        def spam_3():
            z = " even"
            z += y
            print("In spam_3, locals are {}.".format(locals()))
            return z

        y = " more" + x  # y must exist before spam_2() called
        y += spam_3()  # do not combine these two assignments
        print("In spam_2, locals are {}.".format(locals()))
        return y

    x = "spam"  # x must exist before spam_2() called
    x += spam_2()  # do not combine these two assignments
    print("In spam_2, locals are {}.".format(locals()))
    return x


print(spam_1())
print(locals())
print(globals())