import json
key = open("surdic.json", "w")
masterfile=[]
q = True
while q == True:
    data={}
    survQ1 = input("What is your favorite movie?")
    survQ2 = input("What is your age?")
    survQ3 = input("How are you?")
    survQ4 = input("Who is your favorite musical artist?")
    survQ5 = input("Are you smart?")

    data["What is your favorite movie?"] = survQ1
    data["What is your age?"] = survQ2
    data["How are you?"] = survQ3
    data["Who is your favorite musical artist?"] = survQ4
    data["Do you think you are smart?"] = survQ5
    #masterfile = list(data)
    #print(list(data))
    masterfile.append(data)
    #dictionaryToJson = json.dumps(data)
    json.dump(data,key)
    #print(dictionaryToJson)
    #json.write(',\n')

    if(input("Is that the last survey?") == "yes"):
        q = False
        print(masterfile)
    else:
        continue
