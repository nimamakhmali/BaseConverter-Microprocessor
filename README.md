# 🧮 Base Converter

##  About the Project
This is a **microprocessor course mini-project** for converting numbers between bases **2, 8, 10, and 16**.

No built-in or library function is used for base conversion; **all steps are implemented manually**.


##  How to Run

### Run the program:
```bash
python src/base_converter.py
```

### Usage examples:

**Example 1:** Binary to decimal
```
Enter the number: 1010
Base of the input number (2, 8, 10, 16): 2
Target base (2, 8, 10, 16): 10

Result: (1010)2 = (10)10
```

**Example 2:** Hex to binary
```
Enter the number: F3A
Base of the input number (2, 8, 10, 16): 16
Target base (2, 8, 10, 16): 2

Result: (F3A)16 = (111100111010)2
```

**Example 3:** Decimal to octal
```
Enter the number: 255
Base of the input number (2, 8, 10, 16): 10
Target base (2, 8, 10, 16): 8

Result: (255)10 = (377)8
```

##  How it works
The program uses two stages for conversion:

1. Convert the input to base-10 using iterative accumulation
2. Convert from base-10 to the target base using repeated division

##  Algorithms
- To decimal: iterative multiply-and-add
- From decimal: repeated division and remainders

##  For the microprocessor course
This project demonstrates manual base conversion relevant to low-level numeric representation.
