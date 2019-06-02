class Student:
    sno = 0
    sname = ''
    sdep = ''
    math = 0
    engli  = 0
    scie = 0

    def GetDetails(self):
        self.sno = int(input('Enter Student No :'))
        self.sname = input('Enter Student Name :')
        self.sdep = input('Enter Student Depertment :')
        self.math = int(input('Enter mathemetics score :'))
        self.engli = int(input('Enter English Score :'))
        self.scie = int(input('Enter Science score :'))

    def ShowDetails(self):
        Total = self.math + self.engli + self.scie
        Average = Total/3
        if Average >= 75:
            tclass = 'Frist'
        elif Average >= 65:
            tclass = 'Second'
        elif Average >= 55:
            tclass = 'Thrid'
        elif Average >= 45:
            tclass = 'Fourth'
        else:
            tclass = 'feild'

        print ('total :',Total)
        print ('average :',Average)
        print ('class :',tclass)


student = Student()
student.GetDetails()
student.ShowDetails()


        
    
        
