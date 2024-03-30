class RomanNumeralConverter:
    def __init__(self):
        self.roman_numerals_key = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        self.decimal_key = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
    
    def convert_to_decimal(self, roman):
        raise SyntaxError("This is not supported")
    
    def convert_to_roman_numeral(self, decimal):
        raise SyntaxError("This is not supported")