
#Converts Roman Numerals to Numeric Values
class Converter(object):
   
    #Constructor for this class
    def __init__(self, _x:str):
        self.x = _x

        #The Numerical Value for each Roman Numeral
        self.Values = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    #Converts the Roman Numeral to Numeric Value
    def Convert(self):

        result:int = 0

        #Iterate through inputted Numerical value
        for i in range(len(self.x)):
            pass

        return result




