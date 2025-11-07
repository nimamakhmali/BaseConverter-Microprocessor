# 🧮 Base Converter

##  About the Project
This project is part of the Microprocessor Course, developed to manually convert numbers between bases 2, 8, 10, and 16.

Unlike typical converters, this implementation does not use any built-in or library base-conversion functions.
All steps — from digit parsing to fractional conversion — are handled manually through arithmetic operations.


## Features

 Supports bases 2, 8, 10, and 16
 Handles negative numbers (e.g., -42 or -101.1)
 Handles fractional values for binary and decimal bases (e.g., 10.101₂ = 2.625₁₀)
 Input validation for invalid digits or unsupported bases
 Fully interactive command-line interface


##  How to Run

### Run the program:
```bash
python src/base_converter.py
```

### Usage examples:

**Example 1:** Binary to decimal
```
Enter the number: 1010.01
Base of the input number (2, 8, 10, 16): 2
Target base (2, 8, 10, 16): 10

Result: (1010.01)₂ = (10.25)₁₀

```

**Example 2:** Hex to binary
```
Enter the number: -13.75
Base of the input number (2, 8, 10, 16): 10
Target base (2, 8, 10, 16): 2

Result: (-13.75)₁₀ = (-1101.11)₂
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
