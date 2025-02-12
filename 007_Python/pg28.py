class Person:
    def __init__(self,age=0,fname='default_name'):
        self.fname=fname
        self.age=age
        self.skills=[]
    def printing(self):
        return f'fname={self.fname}, age={self.age}, skills={self.skills}'
    
    def skill_insertion(self,skill):
        self.skills.append(skill)

class Student(Person):
    def __init__(self, age=0, fname='default_name',studid=0):
        super().__init__(age, fname)
        self.studentId=studid

    def printing(self):
        return f'{super().printing()}, StudentId={self.studentId}'

s1=Student(22,"ram",101)
s1.skill_insertion("c")
print(s1.printing())