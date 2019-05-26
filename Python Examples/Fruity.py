#Function = Get fruitlist, favfruitprobe,
def fruitlist():
    fruitstring = input("List-'em-you-fucking-fruit!")
    fruits = fruitstring.split()
    return fruits


def favfruitprobe():
    probe = input("Whats'yer-fav, mr\.fruitacular?")
    fav = probe.split()
    print(fav)
    return fav


def comparelistvprobe(one, two):
    for x in fruits:
        if x in favfruit:
            fave = True
            print(fave)
    return fave


#mainline
fruits = fruitlist()
favfruit = favfruitprobe()
comparelistvprobe(fruits, favfruit)

# check


# # if fave == True:
#     print("YOU LOVE THAT FRUIT, eh McFruitntosh?")
# else:
#     print("You're still a fruity motherfucker!")
#


#target
  #Get List Of FaV Fruit - string
  #Splice string into list.split
  #Save that fucking list
  #Now, ask the motherfucker for a fruit - should it be
  #on the list, tell him it is. If not, FUCK OFF.
