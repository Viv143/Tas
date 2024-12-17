'''List - Student Grades
Write a Python program that stores student grades in a list and calculates the average grade.
If the average is above 50, print "Pass"; otherwise, print "Fail.'''


#Make class for student
class Student:
    def __init__(self):
        self.marks=[]

#Get Marks via input and store it into a list
    def Marks(self):
        print("Enter Best of Five Subjects Marks:")
        for i in range(1,6):
            mark=int(input("Enter Best of Five Subjects Marks:"))
            self.marks.append(mark)
        print(self.marks)


#Calculate Total of Marks
    def sum_of_marks(self):
        total=sum(self.marks)
        return total

#Calcualte average of grades
    def get_avg_percentage(self):
        total=sum(self.marks)
        avg=total/5
        return avg
    
#Get Result
    
    def result(self):
        avg=self.get_avg_percentage()
        if avg>50:
            print("You are Pass With",self.get_avg_percentage())
        else:
            print("fail")

c1=Student()
c1.Marks()
c1.sum_of_marks()
c1.get_avg_percentage()
c1.result()
