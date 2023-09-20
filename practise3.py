
class Students:
    
    def __init__(self,name='undefined',age=0,courses='none'):
        students_number = 0
        self.__name = name
        self.__age = age
        self.__courses = courses
        students_number += 1
        
    def get_name_and_age(self):
        return self.__name , self.__age
    
    def set_name_and_age(self,new_name,new_age):
        self.__name = new_name
        self.__age = new_age
        
    def details(self):
        print(f'''Hello {self.__name} your age is {self.__age} and your courses are
***{self.__courses}***''')

    def is_old(self,max_age):
        if max_age <= self.__age:
            print("student is old")
        else:
            print("student isn`t old")

student_1 = Students('mahmoud',22,['python','OOP','Django'])
'''
student_2 = Students('yahia',25,['C','Embeded','MechanicalEngineering'])
student_3 = Students('joo',23,['Networking','C','EmbededSystems'])
student_4 = Students('omar',11,['English','Math','Arabic'])
student_5 = Students('magdy',53,['Law','HumanRights'])

student_1.details()
student_2.details()
student_3.details()
student_4.details()
student_5.details()
'''
student_1.is_old(30)

print(student_1.get_name_and_age())
student_1.set_name_and_age("megzz",30)
print(student_1.get_name_and_age())

#set_name_and_age func will change details func to the new Attributes
student_1.name='sayed' #this 'name' attribute isn`t the same of self.__name
print(student_1.name)
student_1.details() # in describe method we use attributes like self.__name
