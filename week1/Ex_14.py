from sys import argv

script, user_name, user_id = argv
# prompt  = '>>> '
response = 'Enter your response: ' # this is also modified
print ("Hi %s, I'm the %s script." % (user_name, script))
print("Please Enter your id here : %s" % user_id ) # Another variable according to the study drills in the exercise
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
likes = input(response)

print ("Where do you live %s?" % user_name)
lives = input(response)

print ("What kind of computer do you have?")
computer = input(response)

print ("""
 Alright, so you said %r about liking me.
 You live in %r. Not sure where that is.
 And you have a %r computer. Nice.
 """ % (likes, lives, computer))