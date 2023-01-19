class Student():
    def __init__(self, name, surname, rec_book_number, *grades):
        self._name = name
        self._surname = surname
        self._rec_book_num = rec_book_number
        
        self._grades = grades
        self._average_score = average_score = None

    @property
    def name(self):
        return self._name, self._surname


    @property
    def rec_book_number(self):
        return self._rec_book_number    

    @property
    def grades(self):
        return self._grades    

    @property
    def average_score(self):
      def average_score(self):
        if self._average_score is None:
            return sum(self._grades) / len(self._grades)
        return self._average_score

   
class Group():
    student_score = {"student": None, "Grades": []}
    def __init__(self, groupname, faculty, course, *students):
        self._groupname = groupname
        self._faculty = faculty 
        self._course = course        

        if len(students) > 20:
            raise ValueError('There can be no more than 20 students in a group')
     
    
    
    
    def get_student(self, student):
       if self.student_score["student"]:
            return f'Duplication! Student {student.name} is already in the list.\nCheck first and last name!'
       else:
            self.student_score["student"] = student
            return student.name
    
    def __str__(self):
        return f'Group info: {self._faculty}, {self._course}, {self._groupname}\n\n' + ''.join([str(i) for i in self.student_score])
    
    
  

    def top_students(self):
        return sorted(self._group, key=lambda x: x.get_average,  reverse=True)[:5]
        
          



S1 = Student("Victoria", "Monet", "1", 8, 8, 100, 77, 81)
S2 = Student("Victoria", "Monet", "2", 60, 60, 98, 63, 61)
S3 = Student("Mike", "Mike", "3", 86, 99, 88, 77, 81)
S4 = Student("Elka", "Tpwks", "4", 100, 98, 65, 79, 88)
S5 = Student("Alexa", "L", "5", 60, 60, 65, 63, 61)
S6 = Student("jfjdd", "OEIODk", "6", 99, 98, 90, 88, 79)
S7 = Student("LLLL", "ppppp", "7", 60, 98, 65, 63, 61)
S8 = Student("LLLL", "ppppp", "7", 60, 98, 65, 63, 61)


group = Group("ТВ-з11", "TEF", 2, S1, S2, S3, S4, S5, S6, S7, S8)



print("Student:", group.get_student(S1),"Average score:", S1.average_score)
print("Student:", group.get_student(S2),"Average score:", S2.average_score)



print(''.join(str(i) for i in group.top_students()))

