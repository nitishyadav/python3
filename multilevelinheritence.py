#multilevel inheritence

class MusicalInstruments:
    numberOfMajorKeys = 12
    
class StringInstuments(MusicalInstruments):
    typeOfWood="Tonewood"
    
class Guitar(StringInstuments):
    def __init__(self):
        self.numberOfStrings=6
        print("This guitar consists of {} strings.It is made of  {} and it can play {} keys".format(self.numberOfStrings,self.typeOfWood,self.numberOfMajorKeys))
        
        
guitar=Guitar()        