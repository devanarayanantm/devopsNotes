class Person:
    def __init__(self,age=0,fname='default_name'):
        self.fname=fname
        self.age=age
        self.skills=[]
    def printing(self):
        return f'fname={self.fname}, age={self.age}, skills={self.skills}'
    
    def skill_insertion(self,skill):
        self.skills.append(skill)

p=Person()
# print(p.fname," ",p.age)
p.skill_insertion("python")

print(p.printing())

