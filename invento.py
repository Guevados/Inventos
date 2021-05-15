class Composer:
    def __init__(self, name, lastname, nationality, period):
        self.Name = name
        self.LastName = lastname
        self.Nationality = nationality
        self.Period = period
    def SeeComposer(self):
        print("Composer: ",self.Name," ",self.LastName,"\nNationality: ",self.Nationality,"\nPeriod: ",self.Period)

class Compositions:
    def __init__(self, title, instrumentation, type):
        self.Title = title
        self.Instrumentation = instrumentation
        self.Type = type
    def AddComposer(self, composer):
        self.Composer = composer
    def SeeComposition(self):
        print("Title: ", self.Title)
        print("Instrumentation ",self.Instrumentation)
        print("Type ",self.Type)
        self.Composer.SeeComposer()
    def GetTitle(self):
        return self.Title

class Librery(Composer,Compositions):
    def __init__(self):
        self.ListCompositions = []
    def NumsCompositions(self):
        return len(self.ListCompositions)
    def AddComposition(self, Compositions):
        self.ListCompositions = self.ListCompositions + [Compositions]
    def SeeLibrery(self):
        print("____________________________")
        for item in self.ListCompositions:
            item.SeeComposition()
            print("____________________________")
    def DelComposition(self, title):
        locate = False
        del_locate = -1
        for item in self.ListCompositions:
            del_locate += 1
            if item.GetTitle() == title:
                locate = True
                break
        if locate:
            del self.ListCompositions[del_locate]
            print("Deleted work correctly!")
        else:
            print("Work not found!")

def SeeMenu():
    print ("""Menu
1) Add composition to librery
2) See Librery
3) Delete composition
4) Number of compositions
5) Exit""")

def AddCompositionLibrery(librery):
    title = input("Enter the title of the composition: ")
    instrumentation = input("Enter the instrumentation: ")
    composername = input("Enter the name to composer: ")
    composerlastname = input("Enter the last name to composer: ")
    nationalitycomposer = input("Enter  the nationality to composer: ")
    periodcomposer = input("Enter the period to composer: ")
    typecomposition = input("Enter the type composition: ")
    composer = Composer(composername, composerlastname, nationalitycomposer, periodcomposer)
    composition = Compositions(title, instrumentation,  typecomposition)
    composition.AddComposer(composer)
    librery.AddComposition(composition)
    return librery

def SeeLibrery(librery):
    librery.SeeLibrery()

def DelComposition(librery):
    title = input("Enter the titleof the composition to delete: ")
    librery.DelComposition(title)

def NumsCompositions(librery):
    print("The numbers of compositions in the librery is: ", librery.NumsCompositions())
    #arreglo de esta funcion

end = False
librery = Librery()

while not end:
    SeeMenu()
    opc = int(input("Select option: "))
    if (opc == 1):
        librery = AddCompositionLibrery(librery)
    elif (opc == 2):
        SeeLibrery(librery)
    elif(opc == 3):
        DelComposition(librery)
    elif(opc == 4):
        NumsCompositions(librery)
    elif(opc == 5):
        end = True

print("Good Bye!!!")
