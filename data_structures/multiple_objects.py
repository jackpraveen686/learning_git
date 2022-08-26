class Emp:
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
    def display(self):
        print(self.name,self.salary,self.age)
n=["praveen","sam","rocky","shiva"]
sa=[200,300,400,500]
ag=[22,33,44,55]
ob=[]
for i in range(0,4):
    ob.append(Emp(n[i],sa[i],ag[i]))
    if i==2:
        continue
    ob[i].display()
