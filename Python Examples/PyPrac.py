#### Exercise 1 ####

# does 2 to 128 multiples
#fucklist = []
#x = 1
#while x < 20:
#  print(x)
#  x = x*int(2)

#M = "Stay Hard, Feel Cold."
#for x in range(1, 400):
#  if x > 0:
#    print(x)
#    print(M)


#### Exercise 2 ####

#1 - a float is a non-integer.
#2 - fucking, did we?
#4 -

x = 1.0
y = 0.5

#
# 1.5 2.0 2.5 3.0...    print(x) + Y

number_of_numbers = input()
new_item_list = []
number = 1.5
counter = 0
while counter < number_of_numbers:
  number = (counter * .5) + 1.5
  new_item_list.append(number)
  #number += .05
  counter = counter + 1
print(new_item_list

#also

number_of_numbers = input()
new_item_list = []
for counter in range(int(number_of_numbers))
  number = (counter * .5) + 1.5
  new_item_list.append(number)
print(new_item_list)

#lastly

for counter in range(int(number_of_numbers)):
  new_item_list.append((counter * 0.5) + 1.5 )
print(new_item_list)


  ###
 ###
### FUNCTION ###
            ###
           ###


def increment_list():
    number_of_numbers = input("what num of nums?")
    new_item_list = []
    for counter in range(int(number_of_numbers)):
        number = (counter * 0.5) + 1.5
        new_item_list.append(number)
#   return new_item_list
    print(new_item_list)

increment_list()

##
  ## Main line code - ?
  number_of_numbers = input("what num of nums?")
  increment_list()
  print(new_item_list)
##

##
## RETURN FUNCTION?
##
##  This return function is to assemble + stick a new variable ...
## When you finish the function, pass off this information.
##
############
def increment_list(how_many)
    my_new_item_list = []
    for counter in range(int(how_many)):
        number = (counter * 0.5) + 1.5
        my_new_item_list.append(number)
    return my_new_item_list

#mainline
number_of_numbers = input("What is the number of items in your list?")
new_item_list = increment_list(number_of_numbers)
print(new_item_list)
##########


#### Self-Check Swearing ####
def get_sentence(): =
    linein = input(Please type a fucking sentence!)
    return = linein

$D def SelfCheckSwearing(sentence)
    #Need Var: linein
    #Need list: swear words
    #Need compare: Var + list
    #Need splice list from var:linein
    # .. tov?
    return clean

$T def SelfCheckSwearing(senntence_to_check):
    bad_words = ['hell', 'damn']
    words = senntence_to_check.split()
    dirty = False
    for each_word in words:
        if each_word in words:
            dirty = True
    return dirty


# mainline
for counter in range(5):
    # get a sentence
    sentence = get_sentence()
    # SelfCheckSwearing(sentence)
    if check_for_bad_words(sentence):
        print("Stop writing bad words!! FUCK FACE!")
    else:
        print("You typed a clean sentence, square.")



  ***   ******
 ***        *
*** Files ***
*        ***
*****   ***

#
# IMPORT THE BAD FUCKING WORDS , MOTHERFUCKER.
#
$D Def get_thefucking_words()
    #Variable = open(the external file "r = ReadthisShit")
    #(We open an If/Else Function here for surviability against unopenable)
    # assign to a fucking list/element
    #(Else: that list/element goes empty)
    # close
    # another variable = fuckinglist/element.split

$T Def get_bad_words():
    file = open("badwords.txt", "r")
    if file.mode == "r":
        bad_words_text = file.read()
    else
        bad_words_text = ''
    file.close()
    bad_words = bad_words_text.split()
    return bad_words

##
#mainline
