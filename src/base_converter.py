
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
    '9': 9,
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
    'A', 'B', 'C', 'D', 'E', 'F',
]

# lowercase hex letters to uppercase (a..f only)
_LOWER_TO_UPPER_HEX = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D',
    'e': 'E',
    'f': 'F',
}


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
        if up == 'A':
            return 10
        if up == 'B':
            return 11
        if up == 'C':
            return 12
        if up == 'D':
            return 13
        if up == 'E':
            return 14
        if up == 'F':
            return 15
    return -1


def value_to_char(val):
    return _VALUE_TO_CHAR[val]


def parse_decimal_string(s):
    if s is None or s == "":
        return 0, False
    value = 0
    i = 0
    while i < len(s):
        ch = s[i]
        if ch not in _DIGIT_MAP:
            return 0, False
        digit = _DIGIT_MAP[ch]
        value = value * 10 + digit
        i += 1
    return value, True


def to_decimal(number, base):
    if number is None or number == "":
        return 0, False
    total = 0
    i = 0
    while i < len(number):
        ch = number[i]
        val = char_to_value_for_base(ch, base)
        if val < 0:
            return 0, False
        total = total * base + val
        i += 1
    return total, True


def from_decimal(decimal_number, base_to):
    if decimal_number == 0:
        return "0"
    result = ""
    n = decimal_number
    while n > 0:
        r = n % base_to
        ch = value_to_char(r)
        result = ch + result
        n = n // base_to
    return result


def convert(number, base, to_base):
    dec, ok = to_decimal(number, base)
    if not ok:
        return "", False
    return from_decimal(dec, to_base), True


def get_valid_base(text):
    while True:
        raw = input(text)
        val, ok = parse_decimal_string(raw)
        if ok and (val == 2 or val == 8 or val == 10 or val == 16):
            return val
        print("Only bases 2, 8, 10 and 16 are supported!")


def main():
    print("\n" + "=" *50)
    print("    Base Converter - Simple Manual Version")
    print("="*50)

    num = input("\nEnter the number: ")
    base_from = get_valid_base("\nBase of the input number (2, 8, 10, 16): ")
    base_to = get_valid_base("\nTarget base (2, 8, 10, 16): ")

    print("\nConverting...")
    res, ok = convert(num, base_from, base_to)
    if not ok:
        print("Invalid number for the given base!")
        print("="*50 + "\n")
        return

    print(f"\nResult: ({num}){base_from} = ({res}){base_to}")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()
