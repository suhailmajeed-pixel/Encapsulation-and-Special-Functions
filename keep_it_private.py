class myclass:
    __privateVar = 27;

    def __priveMeth(self):
        print("i am inside myclass")

    def hello(self):
        print("private varaibal value : ", myclass.__privateVar)

foo = myclass()
foo.hello()
foo.__priveMeth