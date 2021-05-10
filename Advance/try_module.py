# import a whole module, you have to way to import
# first
import Advance.m.m1 as foo

foo.f1()

# second way
from Advance.m import m1

m1.f1()

# import part of module, you only have one way to do:
from Advance.m.m1 import f1 as function1
function1()


