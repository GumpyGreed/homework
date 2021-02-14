# class Foo:
#     def __init__(self, number):
#         self.number = number

#     def __str__(self):
#         return f'Foo: {self.number}'

#     def __add__(self, other):

#         result = str(self.number) + other.number
#         return Foo(result)

# a = Foo(1)
# b = Foo('sdf')

# c = a + b
# print(c)

# class Fraction:
#     def __init__(self, numer, denom):
#         self.numer = numer
#         self.denom = denom

#     def __str__(self):
#         return f'{self.numer} / {self.denom}'

#     def get_numerator(self):
#         return self.numer

#     def get_denominator(self):
#         return self.denom

#     def __add__(self, other):
#         new_numer = other.denom * self.numer + other.numer * self.denom
#         new_denom = other.denom * self.denom
#         return Fraction(new_numer, new_denom)

#     def __sub__(self, other):
#         new_numer = other.denom * self.numer - other.numer * self.denom
#         new_denom = other.denom * self.denom
#         return Fraction(new_numer, new_denom)

#     def convert(self):
#         return self.numer / self.denom


# oneHalf = Fraction(1, 2)
# twoThirds = Fraction(2, 3)
# print(Fraction.convert(oneHalf))
# print(oneHalf - twoThirds)

from random import randint

class Potion:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

    def __str__(self):
        return f'This potion named: {self.name}'

    def get_quality(self):
        return self.quality
    
    def get_named(self):
        return self.name

    def __add__(self, other):
        newName = self.name[::-1] + other.name
        newQuality = (self.quality + other. quality) // 2
        return Potion(newName, newQuality)

    def __sub__(self, other):
        new_quality = other.quality - randint(1, 50)
        return Potion(self.name, new_quality)

    def check_quality(self):
        if self.quality > 75:
            print('Potion is very good')
        elif self.quality > 50:
            print('Potion is avarage')
        else:
            print('Potion has bad quality')

class QualityPotion(Potion):
    def special(self):
        return QualityPotion(self.name, self.quality + 20)

class NonQualityPotion(Potion):
    def special(self):
        return NonQualityPotion(self.name, self.quality - 20)

game = True
potions = {}

while game:
    potion = input(f'NonQuality - n or for quality - q: ').lower()
    if potion == 'exit':
        game = False
    else:
        potion_name = input('Potion name: ')
        potion_quality = randint(1, 100)
        if potion == 'q':
            new_potion = QualityPotion(potion_name, potion_quality)
        elif potion == 'n':
            new_potion = NonQualityPotion(potion_name, potion_quality)
        potions[potion_name] = new_potion
    if len(potion) >= 2:
        act = input(f'Add(+) or Sub(-)').lower()
        pot1 = potions.popitem()[1]
        pot2 = potions.popitem()[1]
        if act == '+':
            mixed_potion = pot1 + pot2
        else:
            mixed_potion = pot1 - pot2
        print('Mixed')
        if mixed_potion.get_quality() < 30:
            print('BOOM!!!')
            game = False
        else:
            potions[mixed_potion.get_named()] = mixed_potion
            print(f'New name: {mixed_potion.get_named()}')
            print(f'New quality: {mixed_potion.get_quality()}')