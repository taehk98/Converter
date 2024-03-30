from RomanNumeralConverter import RomanNumeralConverter
class ConvertRomanToDecimal(RomanNumeralConverter):
    # override convert_to_decimal from RomanNumeralConverter
    def convert_to_decimal(self, input_roman):
        preceed_value = 0
        decimal = 0
        for curr_numeral in reversed(input_roman):
            curr_value = self.roman_numeral_key[curr_numeral]
            if preceed_value < curr_value:
                # Error if Rule 4 does not match
                if preceed_value < curr_value/10:
                    raise ValueError("This is an invalid input")
                decimal += curr_value
            else:
                decimal -= curr_value
            preceed_value = curr_value
        return decimal
    