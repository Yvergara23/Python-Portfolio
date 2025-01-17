#Yareli Vergara
#December 9th 2024
#Mad Libs

def Mad_Libs1_prep():
    global animal
    global greekGod
    global person
    global location
    global emotion
    print ("Think of an animal")
    animal = str(input("Animal"))
    print ("Think of a Greek God")
    greekGod = str(input("Greek God"))
    print ("Think of a person")
    person = str(input("Person"))
    print ("Think of a location")
    location = str(input("Location"))
    print ("Think of an emotion (past tense)")
    emotion = str(input("Emotion"))
def Mad_Libs_1():
    global animal
    global greekGod
    global person
    global location
    global emotion
    print ("When I was walking in " + location + " I saw " + greekGod + " turn " + person + " into a " + animal + ". I was very " + emotion)

def MadLibsOne():
    Mad_Libs1_prep()
    Mad_Libs_1()

MadLibsOne()