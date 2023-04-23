print("Hello")



class MyProgram():
    def firstProgram(self, Name, Branch, Collge):
        self.Name = Name
        self.Branch = Branch
        self.Collge = Collge

    def Marks(self, marks):
        self.marks = marks
        return f"{(self.marks*100)/600}"

MyP= MyProgram()
MyP.firstProgram("Sai Kiran", "Automobile", "VKR &VNB") 
print(MyP.Marks(522))