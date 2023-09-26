#Create class(university)
class University():
    name = ''
    age = 0.00
    course = ''
    lecturer = ''
    
    def Student(self):
        print(f"my name is {self.name} and my age is {self.age}")
    
    def Courses(self):
        print(f"my course is {self.course}")
    
    def Lecturer(self):
        print(f"my lecturer is {self.lecturer}")
        
uni = University()
uni.name = 'Lule Emmanuel'
uni.age = 23
uni.course = 'BSIT'
uni.lecturer = 'KASOZI BRIAN'

uni.Student()
uni.Courses()
uni.Lecturer()