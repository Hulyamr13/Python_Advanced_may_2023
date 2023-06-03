from project1.mammal import Mammal
from project1.lizard import Lizard

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)

lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
