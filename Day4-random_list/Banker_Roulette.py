# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
import random
names_string = input()
names =names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0,num_items-1) 
print(names[random_choice])
# 🚨 Remember to remove the print statement above when you submit.