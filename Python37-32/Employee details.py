class Employee:
    eno = 0
    ename =''
    emjob =''
    emproject =''

    def GetDetails(self):
        self.eno = int(input('enter employee number :'))
        self.ename = input('enter employee Name :')
        self.emjob = input('enter employee Designation :')
        self.emproject = input('enter employee project name :')

    def ShowDetails(self):
        print('employee number :',self.eno)
        print('employee name :',self.ename)
        print('employee job :',self.emjob)
        print('employee project name :',self.emproject)


employee = Employee()
employee.GetDetails()
employee.ShowDetails()

            
        
        
    
    
    
