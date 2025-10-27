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

    