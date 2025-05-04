class Stud:

    uni = "ky"
     


   def __init__(self , name , group , gpa = 1.0):
      self.name = name
      self.group = group
      self.gpa = gpa
    def __bool__(self):
        return self.gpa >= 2.0
    
    def __str__ (self):
        return "gfgfg {self.name} have gpa {self.gpa}"

    def sayhi (self):
        print("hi . me name is {self.name} {self.group}")
    def infffe (self):
        print("name"self.name)
        print("group"self.group)
       

s1 = Stud("mam" , "gggggg")

print(bool(s1))
print(s1)