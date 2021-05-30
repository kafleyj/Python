# # a=11
# # b=12
# # print("the sum of a and b is ",(a+b))
# class Employee:
#      company="Google"
# harry=Employee()
# print(harry.company)
# harry.salary=300
# print(harry.salary)
# Employee.company="Youtube"

# print(harry.company)
class Calculator:
    def _init_(self,num):
        self.number=num
    def sqaure (self):
        print(f"the valie of {self.number}square is{self.number **2}")
    def sqaureroot (self):
        
        print(f"the valie of {self.number}squareroot is{self.number **0.5}") 
    def cube (self):
        
        print(f"the valie of {self.number} cube is{self.number **3}")
a=Calculator(3)
a.sqaure()
a.sqaureroot()
a.cube () 