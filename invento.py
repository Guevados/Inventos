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
            print("Obra no encontrada!")
        