class Composer:
    def __init__(self, name, lastname, nationality, period):
        self.Name = name
        self.LastName = lastname
        self.Nationality = nationality
        self.Period = period
    def SeeComposer(self):
        print("Composer: ",self.Name," ",self.LastName," ",self.Nationality," ",self.Period)

class Compositions:
    def __init__(self, title, instrumentation, tipe):
        self.Title = title
        self.Instrumentation = instrumentation
        self.Tipe = tipe
    def AddComposer(self, composer):
        self.Composer = composer
    def SeeComposition(self):
        print("Title: ", self.Title)
        print("Instrumentation ",self.Instrumentation)
        print("Tipe ",self.Tipe)
        self.Composer.SeeComposer()
    def GetTitle(self):
        return self.Title

class Librery(Composer,Compositions):
    def __init__(self):
        self.ListCompositions = []
    def NumsCompositions(self):
        return len(self.ListCompositions)
    def AddComposition(self, title):
        self.ListCompositions = self.ListCompositions + [Compositions]
    def SeeLibrery(self):
        print("###########################")
        for item in self.ListCompositions:
            item.SeeComposition()
        print("###########################")
    def DelComposition(self, title):
        locate = False
        locatedel = -1
        for item in self.ListCompositions:
            locatedel += 1
            if item.GetTitle() == title:
                locate = True
                break
        if locate:
            del self.ListCompositions[locatedel]
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
    composer = Composer(composername, composerlastname)
    composition = Compositions(title, instrumentation)
    composition.AddComposer(composer)
    librery.AddComposition(composition)
    return librery
def SeeLibrery(librery):
    librery.SeeLibrery()

def DelComposition(librery):
    title = input("Enter the titleof the composition to delete: ")
    librery.DelComposition(title)

def NumsComposition(librery):
    print("The numbers of compositions in the librery is: ",librery.NumsComposition())

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
        NumsComposition(librery)
    elif(opc == 5):
        end = True

print("Good Bye!!!")