class Converter(object):

    #Constructor
    def __init__(self):

        #A Dictionary of Values that will be used to Convert Roman Numerals to a Numeric Value
        self.Values = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    #Performs Conversion from Roman Numerals to Decimal Values
    def RomanNumeralToDecimal(self, romanNumeral:str = ''):
        
        #Keeps the Sum for the value of the Roman Numeral
        sum = 0

        #Check if the entered String is greater than 0
        if len(romanNumeral) > 0:

            #Interate through the Entered Roman Numeral
            for i in range(len(romanNumeral) - 1):

                #The Current Character in romanNumeral
                left = romanNumeral[i]

                #The Next Character in romanNumeral
                right = romanNumeral[i + 1]

                #If next Character in romanNumeral is greater than than the current, perform subtraction from sum by the left Value
                if self.Values[left] < self.Values[right]:
                    sum -= self.Values[left]

                #For all other other cases, perform addition to sum by the left Value
                else:
                    sum += self.Values[left]

            #Add the Value of the Last Character from Roman Numerals to the total sum to prevent from numeric value being a negative value
            sum += self.Values[romanNumeral[-1]]

        #Return the value of sum
        return sum





