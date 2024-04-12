# In python 3 raw_nput() is replaced with input()
print ("How old are you?",)
age = input()
print ("How tall are you?",)
height = input()
print ("How much do you weigh?",)
weight = input()
print ("How much do you code in a day?",)
code = input()
print ("So, you're %r old, %r tall and %r heavy." % (
age, height, weight))
# %r is replaced with %s and hence the " \' " problem is solved...
print ("After correction :\n So, you're %r old, %s tall and %r heavy and %r hours" % (
age, height, weight, code))