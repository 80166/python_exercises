tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
 '''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("tabby_cat_new: %r, %s" % (tabby_cat, tabby_cat) )
print("persian_cat_new: %r, %s" % (persian_cat, persian_cat))
print("backslash_cat_new: %r, %s" % (backslash_cat, backslash_cat))
