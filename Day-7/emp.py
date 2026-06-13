class Emp():
    def __init__(self,name,id,job,sal,dept):
        self.name=name
        self.id=id
        self.job=job
        self.sal=sal
        self.dept=dept
def details(self):
        print('============')
        print(f"Name = {self.name}")
        print(f"id = {self.id}")
        print(f"job = {self.job}")
        print(f"salary = {self.sal}")
        print(f"dept = {self.job}")
e1=Emp('raj',420,'s/w',20000,'manager')
details(e1)
        