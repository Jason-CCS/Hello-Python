# import a whole module, you have to way to import
# first
import Modules.m.m1 as foo

foo.f1()

# second way
from Modules.m import m1

m1.f1()

# import part of module, you only have one way to do:
from Modules.m.m1 import f1 as function1
function1()


