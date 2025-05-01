class n:
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print(self.name)
        print(self.id_number)

class employee(n):
    def __init__(self,name,id_number,salary,post):
        self.salary=salary
        self.post=post
        n.__init__(self,name,id_number)

a=employee("John",12345,50000,"Manager")
a.display()