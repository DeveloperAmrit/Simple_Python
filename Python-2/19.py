class employee:
    salary = 2000
    salarybonus = 500
    
    @property                    # This makes function as an attribute(property ) of the class.It is a getter decorator.
    def totalsalary(self):
        return  self.salary + self.salarybonus



a = employee()

print(a.totalsalary)     # This will use the function as total salary property of class and rint total salary.

# BUT what if we changed the total salary. We also have to adjust salarybonus and salary.
# We use setter methods for this.


class employee:
    salary = 2000
    salarybonus = 500
    
    @property                    
    def totalsalary(self):
        return  self.salary + self.salarybonus


       

    @totalsalary.setter                           # setter is a decorator used to set values of attributes of a class through functions.
    def totalsalary(self,value):
        self.salarybonus = value - self.salary      # This will adjust salarybonus according to totalsalary. 

b = employee()

print(b.totalsalary)
print(b.salarybonus)

# If we changed totalsalary it will automtically set the salarybonus.

b.totalsalary = 5000         # The value of value parameter is setted.

print( "Total salary of b is" ,b.totalsalary)
print( " Salarybonus of b is" ,b.salarybonus)       # Salarybonus has been adjusted.
