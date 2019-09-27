class Rectangle():
    """Holds width and length and calculates area."""
    area_formula = "area = length * width"
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

handle = open("rectangle.txt","r")

for line in handle:
    line=list(line)
    print(line)
    i = 1
    rectangle1 = Rectangle(int(line[0]),int(line[1]))
    print(f"Rectangle {i}: area", rectangle1.area())
    i +=1


