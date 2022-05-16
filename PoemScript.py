#Python doesn't have a built in random number generator
#so this is here to import a module that has one premade.

import random

#Option to add your own nouns through the IDLE window.
#needs more development but this is a kernel of what
#it may grow into.

newSingularNoun = input("Add a singular noun, like cat, dog, or rock:")
singularNounList = [newSingularNoun]
print ("Singular noun list so far:")
print (singularNounList)

def createSingularNounList():
    keepGoing = input("Add another word? Type y or n.")
    if keepGoing == "y":
        newItem = input("Add a word:")
        singularNounList.append(newItem)
        print ("Singular nouns in list so far:")
        print (singularNounList)
        createSingularNounList()
    elif keepGoing == "n":
        print ("okay! Next bit!")
    return singularNounList

singularNounList = createSingularNounList()
'''

#You can manually add items to your noun list here
#Just make sure your new nouns are contained in quotes
#and seperated by commas


singularNounList = ["moon", "pulsar","nebula", "red star", "ice giant", "comet", "equinox",
                    "loom", "lemon", "milk bottle", "cabinet", "sorbet", "ear drum", "mayfly",
                    "man", "ocean", "face", "order", "grass", "home", "eye", "friend", "wax",
                    "rind", "machine", "android", "wind", "day", "sea", "reflection", "permission",
                    "crest", "pink soap", "phylum", "sea", "phone"]
'''

#This section generates a random number that is then used to pick a random
#noun from our noun list. The first item is zero, not one, so this bit of code
#tells python to pick a random item on the list in the range of 0 to the length
# of the total list minus 1.

#From there it creates multiple nouns that you can use.
#If you want a different number each time you have to make
#the random function role the dice again.

singNounListLength = len(singularNounList)
r = random.randrange(0,(singNounListLength-1))
singNoun = singularNounList[r]

r = random.randrange(0,(singNounListLength-1))
singNoun2 = singularNounList[r]

r = random.randrange(0,(singNounListLength-1))
singNoun3 = singularNounList[r]



#Option to add your own beings similar to single noun list
''' newBeing = input("Add a proper noun, concept, or being:")
beingList = [newBeing]
print ("Being list so far:")
print (beingList)

def createBeingList():
    keepGoing = input("Add another word? Type y or n.")
    if keepGoing == "y":
        newItem = input("Add a word:")
        beingList.append(newItem)
        print ("Being list so far:")
        print (beingList)
        createBeingList()
    elif keepGoing == "n":
        print ("okay! Next bit!")
    return beingList

beingList = createBeingList()'''

beingList = ["Enola Gay", "Sappho", "Eros", "Electra", "Sleep", "God", "Los Angeles", "Job",
             "Marilyn Monroe", "the Louvre", "New Orleans", "Hercules", "Abraham", "Eve",
             "Pinocchio", "Kurt Vonnegut", "Death", "your mother", "your father",
             "your sister", "your brother"]

beingListLength = len(beingList)
r = random.randrange(0,(beingListLength-1))
being = beingList[r]

#pronouns should not be input by user since we have them pretty much set.
pronouns = ["he", "she", "they", "we", "I", "you"]

#for some templates, a pronoun or name may work, so this combines the two lists
beingPronounList = pronouns.copy() 
beingPronounList.extend(beingList)

beingPronounListLength = len(beingPronounList)
r = random.randrange(0,(beingPronounListLength-1))
beingPronoun = beingPronounList[r]

r = random.randrange(0,(beingPronounListLength-1))
beingPronoun2 = beingPronounList[r]

#Add past verbs here
pastVerbs = ["dyed", "wounded", "knitted", "baked", "spun", "drank", "gasped", "thundered",
             "cut", "drowned", "swept", "waltzed", "crept", "sang", "gathered", "shook",
             "peeled", "saved", "plowed", "bleached"]

pastVerbsLength = len(pastVerbs)
r = random.randrange(0,(pastVerbsLength-1))
pastVerb = pastVerbs[r]


#questions should not be input by user since we have them pretty much set.
questions = ["Why","How","Where","When","Who"]
r = random.randrange(0,4)
question = questions[r]

r = random.randrange(0,4)
question2 = questions[r]

#Same with would should options and conditionals
wouldShould = ["would", "should", "wouldn't", "shouldn't"]
r = random.randrange(0,3)
pickWouldShould = wouldShould[r]

r = random.randrange(0,1)
pickWouldShould2 = wouldShould[r]

#Conditionals here
conditionals = ["always","sometimes","never", "maybe"]
r = random.randrange(0,3)
conditional = conditionals[r]

#Add present verbs here
presentVerbs = ["survive","cry","paint", "sing", "dance", "swim", "dream", "carve",
                "gallop", "weave", "murmur", "stumble", "croak", "crease", "fold"]

presentVerbsLength = len(presentVerbs)
r = random.randrange(0,(presentVerbsLength-1))
presentVerb = presentVerbs[r]


r = random.randrange (0,(presentVerbsLength-1))
presentVerb2 = presentVerbs[r]

r = random.randrange(0,(presentVerbsLength-1))
presentVerb3 = presentVerbs[r]

#Add adjectives here
adjectives = ["pink", "red", "blue", "glowing", "soft", "cold", "open", "childish",
              "best", "muddy", "human", "grey", "dead", "stumped", "wide", "narrow",
              "hot", "lambent", "gold", "shallow"]

adjLength = len(adjectives)
r = random.randrange(0,(adjLength-1))
adjective = adjectives[r]

#Add plural nouns here
pluralNouns = ["feet", "showers", "blue-eyed dogs", "exoskeletons", "book lungs",
               "sorrows", "strangers", "strings of lights", "sequins", "pearls",
               "champagnes", "quilts", "yarns", "pools", "shames", "hands", "gardens",
               "lots", "crumbs", "mosquitos", "chairs", "horns", "bowls", "mice",
               "casts", "famines"]

pluralNounsLength = len(pluralNouns)
r = random.randrange(0,(pluralNounsLength-1))
pluralNoun = pluralNouns[r]

#Add present verbs with an s
presentVerbs2 = ["scratches", "leaps", "gnaws", "burns", "walks", "drives",
                 "sails", "grieves", "glosses", "stutters", "thrashes", "remembers"]
presentVerbs2Length = len(presentVerbs2)
r = random.randrange(0,(presentVerbs2Length-1))
presentVerb2 = presentVerbs2[r]


#Templates

'''
#Template 1
print (" ")
print ("*****")
print (" ")
print (question + " " + presentVerb2 + " the " + singNoun + "?")
print ("It was " + conditional + " " + beingPronoun + ".")
print ("My " + adjective + " " + singNoun2 + ", " + being + " and I." )
print ("Our " + singNoun3 + " " + pastVerb + ".")
'''

#Template 2

print (" ")
print ("*****")
print (" ")
print ("The " + singNoun + " is " + being + "'s " + singNoun2 + ".")
print (question + " " + pickWouldShould + " " + beingPronoun + " " + presentVerb + "?")
print ("It's like " + beingPronoun2 + " " + pickWouldShould2 + " " + conditional + " " + presentVerb2 + ":")
print ("Here are the " + pluralNoun + " a " + singNoun3 + " " + pastVerb + ".")



