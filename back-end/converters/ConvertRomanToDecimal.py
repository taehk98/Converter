from converters.RomanNumeralConverter import RomanNumeralConverter

class ConvertRomanToDecimal(RomanNumeralConverter):
    # override convert_to_decimal from RomanNumeralConverter
    def convert_to_decimal(self, input_roman):
        print(input_roman)
        for numeral in input_roman:
            if numeral not in self.roman_numerals_key:
                return "Invalid Input"
            
        if self.valid_order(input_roman) is False:
            return "Invalid order"
        
        reversed_input = list(reversed(input_roman))
        print(reversed_input)
        decimal = self.roman_numerals_key[reversed_input[0]]
        preceed_value = self.roman_numerals_key[reversed_input[0]]
        
        if len(reversed_input) != 1:
            for curr_numeral in reversed_input[1:]:
                curr_value = self.roman_numerals_key[curr_numeral]
                if preceed_value <= curr_value:
                    decimal += curr_value
                else:
                    decimal -= curr_value
                preceed_value = curr_value
        else: 
            return self.roman_numerals_key[input_roman]
        
        return decimal
    
    def valid_order(self, input_roman):
        allowed_pairs = {
            'IV', 'IX' , 'XL', 'XC', 'CD', 'CM', 'II'
        }
        allowed_combinations = {
            'I': ['I', 'X', 'V'],
            'X': ['X', 'C', 'I', 'V', 'L'],
            'V': ['V', 'L', 'I'],
            'L': ['L', 'V', 'I', 'X', 'D'],
            'C': ['C', 'V', 'I', 'X', 'L', 'M', 'D'],
            'D': ['D', 'V', 'I', 'X', 'L', 'C'],
            'M': ['M', 'D', 'V', 'I', 'X', 'L', 'C']
        }
                
        i = 0
        while i < len(input_roman) - 1:
            current_numeral = input_roman[i]
            next_numeral = input_roman[i + 1]

            combination = current_numeral + next_numeral
            if combination in allowed_pairs and next_numeral in allowed_combinations[current_numeral]:
                if combination == 'II':
                    allowed_combinations['I'] = ['I']  
                elif combination == 'IV':
                    allowed_combinations['V'] = []
                    allowed_combinations['I'] = []
                elif combination == 'IX':
                    allowed_combinations['X'] = []
                    allowed_combinations['I'] = []
                elif combination == 'XL':
                    allowed_combinations['L'] = ['I', 'V']
                elif combination == 'XC':
                    allowed_combinations['C'] = ['I', 'V']
                elif combination == 'CD':
                    allowed_combinations['D'] = ['I', 'V', 'L', 'X']
                elif combination == 'CM':
                    allowed_combinations['M'] = ['I', 'V', 'L', 'X']               
            else:
                if next_numeral not in allowed_combinations[current_numeral]:
                    return False
            i += 1
        return True
            
