#Voila test list for something
linein = input("How many items on the list?")
bad_list = ['tofu']
new_item_list = []
try:
    number = int(linein)
    for counter in range(number):
        message = "What is the "+str(counter+1)+" item in the list?"
        new_item = input(message)
        if new_item.lower() in bad_list:
            print('You are a blood-mouth!')
        else:
            new_item_list.append(new_item)
except:
    print('you probably fucked up')
print(new_item_list)
