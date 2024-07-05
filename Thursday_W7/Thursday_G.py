class Parent:
    def __init__(self, height, complexion, eye_colour):
        self.height = height
        self.complexion = complexion
        self.eye_colour = eye_colour

    def __str__(self) -> str:
        return (f'I am {self.height} tall and {self.complexion} in complexion with my eye colour being {self.eye_colour}.')

parent_1 = Parent('163.5 cm', 'dark', 'brown')
parent_2 = Parent('170 cm', 'light', 'blue')

print(parent_1)
print(parent_2)

class Children(Parent):
    def __init__(self, height, complexion, eye_colour, age):
        super().__init__(height, complexion, eye_colour)
        self.age = age

    def __str__(self) -> str:
        return super.__str__(f'I am {self.age} years old and {self.height} tall. My skin colour is {self.complexion} with my eye colour being {self.eye_colour}')
    
child_1 = Children ('132.0 cm', 'light brown', 'brown', 14)
child_2 = Children ('120.5 cm', 'light', 'brownish blue', 9)
child_3 = Children ('155.6 cm', 'dark', 'blue', 20)

print(child_1)
print(child_2)
print(child_3)

class Grandchildren(Children):
    def __init__(self, height, complexion, eye_colour, age, developmental_stage):
        super().__init__(height, complexion, eye_colour, age)
        self.developmental_stage = developmental_stage

    def __str__(self) -> str:
        return super.__str__(f'I am just a {self.developmental_stage} of {self.age} old with an eye colour of {self.eye_colour}. I am {self.height} tall with skin toned {self.complexion}.')

grandchild_1 = Grandchildren ('51.2 cm', 'light', 'brown', '6 months', 'baby')
grandchild_2 = Grandchildren ('98.2 cm', 'dark', 'blue', '2 years', 'toddler')
grandchild_3 = Grandchildren ('48.6 cm', 'dark', 'brown', '2 weeks', 'neonate')
grandchild_4 = Grandchildren ('100.5 cm', 'light brown', 'bluish brown', '4 years', 'toddler')

print(grandchild_1)
print(grandchild_2)
print(grandchild_3)
print(grandchild_4)


