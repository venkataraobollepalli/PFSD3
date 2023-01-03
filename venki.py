class klu:
    print('how r u')
    def function1(self):
        print('Am Fine')
        print(self.a+self.b)
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print('inside the constructor')
cse=klu(2,3)
cse.function1()
cse.__init__(1,2)