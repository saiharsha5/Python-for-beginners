class Candidate:
    def __init__(self,name,age,gender,phno,email,skills):
        self.name=name
        self.age=age
        self.gender=gender
        self.phno=phno
        self.email=email
        self.skills=set(skills)
class JobOpening:
    def __init__(self,title,eligibility,salary,reqskills):
        self.title=title
        self.eligibility=eligibility
        self.salary=salary
        self.reqskills=set(reqskills)
class Interview:
    def __init__(self,candidate,jobopenings,date,time):
        self.candidate=candidate
        self.jobopenings=jobopenings
        self.date=date
        self.time=time
        
        

        