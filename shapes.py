from cmath import pi

class  Circle:
    def __init__(self,radius):
        self.radius = radius 

    def area(self):
        print (self.radius**2*pi)

    def circum(self):
        circum_perimetre = pi*(self.radius + self.radius)
        print (f"Your circle perimetre is {circum_perimetre}")


class  Square:
    def __init__(self,a):
        self.a = a
    def area_square(self):
        print(self.a * self.a)

    def perimetre_square(self):
        perimetre = (4 * self.a)
        print(f"Square perimetre {perimetre}")


class  Rectangle:
    def __init__(self,width,length):
        self.witdh = width
        self.length = length

    def area_rectangle(self):
        formula = (self.witdh*self.length)
        return f"Area of your rectangle is {formula}"

    def perimetre_rectangle(self):
        calculate = 2 * (self.witdh+self.length)
        return f"The perimetre of this rectangle is {calculate}"


class Sphere:
    def __init__(self,r): 
        self.r = r

    def area_sphere(self):
        result = 4 * pi * (self.r*self.r)
        return f" {result} is the area of sphere"

    def volume_sphere(self):
        volume = 4/3 *pi*(self.r**3)
        return f"{volume} is the volume of your sphere"
            

        
        
