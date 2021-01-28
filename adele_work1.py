# # string concatenation (aka how to put strings together)
# #suppose we want to create a string that says"suscribe to _____
# youtuber= "Adele Kim" #some string variable

# #few ways to do this
# print("subscribe to " + youtuber)
# print("suscribe to {}" .format(youtuber))
# print(f"suscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person =input("Famous person: ")

madlib = f"Computar programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
