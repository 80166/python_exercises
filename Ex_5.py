user_name = 'Zed A. Shaw'
user_age = 35 # not a lie
user_height = 74 # inches
user_weight = 180 # lbs
user_eyes = 'Blue'
user_teeth = 'White'
user_hair = 'Brown'

print ("Let's talk about %s." % user_name)
print ("He's %d inches tall." % user_height)
print ("He's %d pounds heavy." % user_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (user_eyes, user_hair))
print ("His teeth are usually %s depending on the coffee." % user_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (user_age, user_height, user_weight, user_age + user_height + user_weight))