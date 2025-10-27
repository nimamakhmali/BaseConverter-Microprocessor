number = int(input("Enter a number: "))
base = int(input("Enter the base: ")) # 2, 8, 10, 16
to_base = int(input("Enter the base to convert to: ")) # 2, 8, 10, 16





def to_decimal(number, base):
    decimal_number = 0
    power = 1
    for ch in number[::-1]:
        digit = int(ch)
        if digit >= base:
            print("Invalid number")
            exit()
        decimal_number += digit * power
        power *= base

    return decimal_number


def from_decimal(decimal_number, base_to):
    if decimal_number == 0:
        return "0"
    result = ""
    number = decimal_number
    while number > 0:
        remainder = number % base_to
        result = str(remainder) + result
        number //= base_to
    return result



def convert(number, base, to_base):
    decimal_value = to_decimal(number, base)
    result = from_decimal(decimal_value, to_base)
    return result

def main():
    print("Welcome to the Base Converter")
    num = input("Enter a number: ")
    base_from = int(input("Enter the base: "))
    base_to = int(input("Enter the base to convert to: "))
    result = convert(num, base_from, base_to)
    print(f"The result is: {result}")
    

if __name__ == "__main__":
    main()
