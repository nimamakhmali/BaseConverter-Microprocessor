# -------------------------------
#   Base Converter - Final Version
#   Supports bases: 2, 8, 10, 16
#   Handles negative and fractional numbers (for base 2 and 10)
# -------------------------------

_DIGIT_MAP = {
    '0': 0, 
    '1': 1, 
    '2': 2, 
    '3': 3, 
    '4': 4,
    '5': 5, 
    '6': 6, 
    '7': 7, 
    '8': 8, 
    '9': 9
}

# map numeric value to character for 0..15
_VALUE_TO_CHAR = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'A', 'B', 'C', 'D', 'E', 'F'
]

# lowercase hex letters to uppercase (a..f)
_LOWER_TO_UPPER_HEX = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D',
    'e': 'E',
    'f': 'F'
}

# -------------------------------
#  Helper functions
# -------------------------------

def to_upper_hex_letter(ch):
    if ch in _LOWER_TO_UPPER_HEX:
        return _LOWER_TO_UPPER_HEX[ch]
    return ch

def char_to_value_for_base(ch, base):
    if ch in _DIGIT_MAP:
        val = _DIGIT_MAP[ch]
        if val < base:
            return val
        return -1
    if base == 16:
        up = to_upper_hex_letter(ch)
        if up == 'A': return 10
        if up == 'B': return 11
        if up == 'C': return 12
        if up == 'D': return 13
        if up == 'E': return 14
        if up == 'F': return 15
    return -1


def value_to_char(val):
    return _VALUE_TO_CHAR[val]

# -------------------------------
#  Conversion to decimal
# -------------------------------
def to_decimal(number, base):
    if number is None or number == "":
        return 0.0, False

    negative = False
    if number[0] == '-':
        negative = True
        number = number[1:]


    if '.' in number:
        int_part, frac_part = number.split('.', 1)
    else:
        int_part, frac_part = number, ""

    total = 0.0

    # integer part
    for ch in int_part:
        val = char_to_value_for_base(ch, base)
        if val < 0:
            return 0.0, False
        total = total * base + val

    # fractional part
    power = 1.0 / base
    for ch in frac_part:
        val = char_to_value_for_base(ch, base)
        if val < 0:
            return 0.0, False
        total += val * power
        power /= base

    if negative:
        total = -total
    return total, True

# -------------------------------
#  Conversion from decimal
# -------------------------------

def from_decimal(decimal_number, base_to):
    if decimal_number == 0:
        return "0"

    negative = decimal_number < 0
    if negative:
        decimal_number = -decimal_number

    int_part = int(decimal_number)
    frac_part = decimal_number - int_part

    # integer part
    result_int = ""
    if int_part == 0:
        result_int = "0"
    else:
        while int_part > 0:
            r = int_part % base_to
            result_int = value_to_char(r) + result_int
            int_part //= base_to

    # fractional part
    result_frac = ""
    count = 0
    while frac_part > 0 and count < 10:  # up to 10 digits after point
        frac_part *= base_to
        digit = int(frac_part)
        result_frac += value_to_char(digit)
        frac_part -= digit
        count += 1

    result = result_int
    if result_frac != "":
        result += "." + result_frac
    if negative:
        result = "-" + result
    return result

# -------------------------------
#  Conversion wrapper
# -------------------------------

def convert(number, base_from, base_to):
    dec, ok = to_decimal(number, base_from)
    if not ok:
        return "", False
    return from_decimal(dec, base_to), True

def get_valid_base(text):
    while True:
        raw = input(text)
        if raw in ['2','8','10','16']:
            return int(raw)
        print("Only bases 2, 8, 10 and 16 are supported!")

# -------------------------------
#  Main function
# -------------------------------

def main():
    print("\n" + "=" * 50)
    print("        Base Converter - Final Version")
    print("=" * 50)

    num = input("\nEnter the number (can be negative or fractional): ")
    base_from = get_valid_base("\nBase of the input number (2, 8, 10, 16): ")
    base_to = get_valid_base("\nTarget base (2, 8, 10, 16): ")

    print("\nConverting...")
    res, ok = convert(num, base_from, base_to)
    if not ok:
        print("Invalid number for the given base!")
        print("=" * 50 + "\n")
        return

    print(f"\nResult: ({num}){base_from} = ({res}){base_to}")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()

