from converters.RomanNumeralConverter import RomanNumeralConverter

class ConvertDecimalToRoman(RomanNumeralConverter):
    # override convert_to_roman_numeral from RomanNumeralConverter
    def convert_to_roman_numeral(self, decimal):
        decimal = int(decimal)
        roman_output = ''
        # The input should not go over 3999
        if decimal > 3999:
            raise ValueError("The decimal input should be less than 3,999")
        
        for curr_std_decimal in sorted(self.roman_numerals_key.values(), reverse=True):
            curr_std_decimal_str = str(curr_std_decimal)
            decimal_str = str(decimal)
            # for 1, 10 , 100, 1000
            if curr_std_decimal_str[0] == str(1):
                if curr_std_decimal == 100:
                    if decimal_str[0] == str(4) and len(decimal_str) == 3:
                        decimal -= 400
                        roman_output += 'CD'
                elif curr_std_decimal == 10:
                    if decimal_str[0] == str(4) and len(decimal_str) == 2:
                        decimal -= 40
                        roman_output += 'XL'
                elif curr_std_decimal == 1:
                    if decimal_str[0] == str(4) and len(decimal_str) == 1:
                        decimal -= 4
                        roman_output += 'IV'
                while curr_std_decimal <= decimal:
                    decimal -= curr_std_decimal
                    roman_output += self.decimal_key[curr_std_decimal]
            # for  5, 50, 500          
            elif curr_std_decimal_str[0] == str(5):
                if curr_std_decimal == 500:
                    if decimal_str[0] == str(9) and len(decimal_str) == 3:
                        decimal -= 900
                        roman_output += 'CM'
                if curr_std_decimal == 50:
                    if decimal_str[0] == str(9) and len(decimal_str) == 2:
                        decimal -= 90
                        roman_output += 'XC'
                if curr_std_decimal == 5:
                    if decimal_str[0] == str(9) and len(decimal_str) == 1:
                        decimal -= 9
                        roman_output += 'IX'
                while curr_std_decimal <= decimal:
                        decimal -= curr_std_decimal
                        roman_output += self.decimal_key[curr_std_decimal]
                    
        return roman_output