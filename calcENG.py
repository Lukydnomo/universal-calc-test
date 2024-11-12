import os
import colorama
from colorama import init, Fore, Style, Back
from datetime import datetime
import random
import requests as rq
import math
pi = math.pi
import re

init()

options = [
    '1. Basic Operations (+, -, /, *, **)',
    '2. Calculate Square Root',
    '3. Calculate Factorial',
    '4. Calculate Percentage',
    '5. Arithmetic Progression',
    '6. Geometric Progression',
    '7. Solve Quadratic Equations',
    '8. Calculate Time',
    '9. Unit Converter',
    '10. Calculate Average',
    '11. Convert Bases',
    '12. Calculate Simple Interest',
    '13. Calculate Age',
    '14. Die (Dx)',
    '15. Calculate Resistor',
    '16. Currency Converter',
    '17. Find Minimum and Maximum Number',
    '18. Calculate LCM (Least Common Multiple)',
    '19. Calculate GCD (Greatest Common Divisor)',
    '20. Check Prime Number',
    '21. Calculate Perimeter',
    '22. Calculate Area',
    '23. Calculate Volume',
    '24. Solve Linear System',
    '25. Verify CPF',
    '26. Calculate BMI',
    '27. Rocket Launch Simulator',
    '28. Calculate Percentage Increase between Two Numbers',
    '29. Calculate Compound Interest',
    '30. Calculate Average Speed',
    '31. Verify CNPJ',
    '32. Int to Roman Numerals',
    '33. Calculate the Fundamental Principle of Dynamics',
    '34. Calculate Gravitational Force between 2 objects',
    '35. Calculate Gravitational Potential Energy of an object',
    '36. Calculate Income Tax',
    '37. RGB to HEX',
    '38. Calculate Kinetic Energy',
    '39. Coulombs Law (Electrostatic Force)',
    '40. ASCII to Binary'
]

def format_options(options):
    perColumn = 20
    
    roundedCol = perColumn - 1
    num_columns = (len(options) + roundedCol) // perColumn
    column_width = max(len(option) for option in options) + 2
    formatted_options = ""
    for i in range(perColumn):
        for j in range(num_columns):
            index = j * perColumn + i
            if index < len(options):
                formatted_options += f"{options[index]:<{column_width}}"
        formatted_options += "\n"
    return formatted_options

def exit():
    format.input_bold("Press Enter to continue... ")
    clear()
    calc()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class format():
    def print_bold(*args):
        print(Style.BRIGHT, end='')
        for arg in args:
            print(arg, end=' ')
        print(Style.RESET_ALL)

    def input_bold(prompt=''):
        print(Style.BRIGHT, end='')
        user_input = input(prompt)
        print(Style.RESET_ALL, end='')
        return user_input

def printResult(*args):
    for arg in args:
        print(f'Result: {arg}\n', end=' ')

def basic(num3):
    return eval(num3)

def sqrt(num3):
    if num3 < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
        
    estimate = num3 / 2
    precision = 0.0001
        
    while True:
        new_estimate = (estimate + num3 / estimate) / 2
            
        if abs(estimate - new_estimate) < precision:
            return new_estimate
            
        estimate = new_estimate

def factorial(num3):
    if num3 == 0:
        return 1
    else:
        return num3 * factorial(num3 - 1)
        
def percentage(x, y):
    return x * y / 100
    
def formatTime(num4, num5):
    return "{:02d}:{:02d}".format(int(num4), int(num5))

def hours(num4, num5, num6):
    hours_ahead = num6 // 60
    num6 = num6 % 60

    num4 += hours_ahead
    num5 += num6

    if num5 >= 60:
        num4 += 1
        num5 -= 60

    num4 %= 24

    return formatTime(num4, num5)
    
def AP(num4, num5, num6):
    terms = [num4]
    for _ in range(1, int(num6)):
        next_term = terms[-1] + num5
        terms.append(next_term)
    return terms
    
def GP(num4, num5, num6):
    terms = [num4]
    for _ in range(1, int(num6)):
        next_term = terms[-1] * num5
        terms.append(next_term)
    return terms

def EQ(num4, num5, num6):
    discriminant = num5**2 - 4*num4*num6

    if discriminant > 0:
        x1 = (-num5 + discriminant**0.5) / (2*num4)
        x2 = (-num5 - discriminant**0.5) / (2*num4)
        return x1, x2
    elif discriminant == 0:
        x = -num5 / (2*num4)
        return x,
    else:
        return "The equation has no real roots."

def convertUnit(opconvmed, opconv):
    if opconv == 1:
        return (opconvmed * 9/5) + 32
    if opconv == 2:
        return (opconvmed * 3.281)
    if opconv == 3:
        return (opconvmed * 2.205)
    if opconv == 4:
        return (opconvmed - 32) * 5/9
    if opconv == 5:
        return (opconvmed / 3.281)
    if opconv == 6:
        return (opconvmed / 2.205)

def average(num3):
    numbers_str = num3
    numbers = [float(x.strip()) for x in numbers_str.split(',')]
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

def convertBases(opconvbaseop, opconvbase):
    if opconvbase == 1:
        return f'{opconvbaseop:b}'
    if opconvbase == 2:
        return f'{opconvbaseop:o}'
    if opconvbase == 3:
        return f'{opconvbaseop:X}'
    if opconvbase == 4:
        return int(str(opconvbaseop), 2)
    if opconvbase == 5:
        return int(str(opconvbaseop), 8)
    if opconvbase == 6:
        return int(opconvbaseop, 16)

def simpleInterest(num4, num5, num6):
    C = num4
    t = (num5 / 100)
    i = num6
    iA = (num6 / 12)
    result = C * t * iA
    return C + result

def age(num3):
    today_exact = datetime.now()

    today_year = today_exact.year
    today_month = today_exact.month
    today_day = today_exact.day

    birth_year, birth_month, birth_day = map(int, num3.split('-'))

    age = today_year - birth_year
    
    if today_month < birth_month or (today_month == birth_month and today_day < birth_day):
        age -= 1
    
    return age

def randomNum(num3):
    return random.randint(int(1.0), int(num3))

def energy(num1, num2):
    V = num1
    I = num2
    R = V / I
    
    return int(R)

def currencyConverter(opconvmony, opconvmonyop):
    api_key = '218e6302cb5c4629a1f852f1a7a3a6b8'
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = rq.get(url)
    data = response.json()

    usd_to_brl = data['rates']['BRL']
    eur_to_usd = data['rates']['EUR']
    ars_to_usd = data['rates']['ARS']
    btc_to_usd = data['rates']['BTC']

    brl_to_usd = 1 / usd_to_brl
    brl_to_eur = brl_to_usd * eur_to_usd
    brl_to_ars = brl_to_usd * ars_to_usd
    brl_to_btc = brl_to_usd * btc_to_usd

    value = opconvmonyop

    if opconvmony == 1:
        result = value * brl_to_usd
        formattedResult = f"${round(result, 2):.2f}"
        return formattedResult
    elif opconvmony == 2:
        result = value * brl_to_eur
        formattedResult = f"€{round(result, 2):.2f}"
        return formattedResult
    elif opconvmony == 3:
        result = value * brl_to_ars
        formattedResult = f"${round(result, 2 ):.2f}"
        return formattedResult
    elif opconvmony == 4:
        result = value * brl_to_btc
        formattedResult = f"₿{result}"
        return formattedResult
    elif opconvmony == 5:  # Division, Real to currency, currency to Real
        result = value * usd_to_brl
        formattedResult = f"R${round(result, 2):.2f}"
        return formattedResult
    elif opconvmony == 6:
        result = value * (usd_to_brl / eur_to_usd)
        formattedResult = f"R${round(result, 2):.2f}"
        return formattedResult
    elif opconvmony == 7:
        result = value * (usd_to_brl / ars_to_usd)
        formattedResult = f"R${round(result, 2):.2f}"
        return formattedResult
    elif opconvmony == 8:
        result = value * (usd_to_brl / btc_to_usd)
        formattedResult = f"R${round(result, 2):.2f}"
        return formattedResult
    
def findNum(num3):
    numbers = list(map(float, num3.split()))
    minimum = min(numbers)
    maximum = max(numbers)

    return f'Minimum: {int(minimum)}, Maximum: {int(maximum)}'

def calculate_lcm(*num3):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    result = 1
    for num in num3:
        result = lcm(result, num)
    return result

def calculate_gcd(*num3):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    result = num3[0]
    for num in num3[1:]:
        result = gcd(result, num)
    return result

def checkPrime(num3):
    mult = 0

    for count in range(2, num3):
        if (num3 % count == 0):
            pMdC = count
            mult += 1

    if num3 in (0, 1):
        return (f'Invalid number')
    else:
        if(mult == 0):
            return (f"{num3} is prime")
        else:
            return (f"{num3} is not prime, it is a multiple of {pMdC}")

def perimeter(option21):
    if option21 == 1:
        side1 = float(input("Enter the value of the first side: "))
        side2 = float(input("Enter the value of the second side: "))
        resultPerim = 2 * (side1 + side2)
    elif option21 == 2:
        side1 = float(input("Enter the value of the first side: "))
        side2 = float(input("Enter the value of the second side: "))
        side3 = float(input("Enter the value of the third side: "))
        resultPerim = side1 + side2 + side3
    elif option21 == 3:
        side = float(input("Enter the value of the side: "))
        resultPerim = 4 * side

    return resultPerim

def area(option22):
    if option22 == 1:
        h = float(input("Enter the height value: "))
        b = float(input("Enter the base value: "))
        resultArea = b * h
    elif option22 == 2:
        h = float(input("Enter the value of the first side: "))
        b = float(input("Enter the value of the second side: "))
        resultArea = b * h
    elif option22 == 3:
        i = float(input("Enter the value of the side: "))
        resultArea = i ** 2
    elif option22 == 4:
        D = float(input("Enter the value of the larger diagonal: "))
        d = float(input("Enter the value of the smaller diagonal: "))
        resultArea = (D * d) / 2
    elif option22 == 5:
        b = float(input("Enter the base value: "))
        h = float(input("Enter the height value: "))
        resultArea = (b * h) / 2
    elif option22 == 6:
        B = float(input("Enter the value of the larger base: "))
        b = float(input("Enter the value of the smaller base: "))
        h = float(input("Enter the height value: "))
        resultArea = ((B + b) * h ) / 2
    elif option22 == 7:
        r = float(input("Enter the value of the radius: "))
        resultArea = pi * r ** 2

    return resultArea

def volume(option23):
    if option23 == 1:
        a = float(input("Enter the value of the side: "))
        resultVolume = a ** 3
    elif option23 == 2:
        a = float(input("Enter the value of the first side: "))
        b = float(input("Enter the value of the second side: "))
        c = float(input("Enter the value of the third side: "))
        resultVolume = a * b * c
    elif option23 == 3:
        r = float(input("Enter the value of the radius of the base: "))
        h = float(input("Enter the height value: "))
        resultVolume = pi * r ** 2 * h
    elif option23 == 4:
        r = float(input("Enter the value of the radius: "))
        resultVolume = (4 / 3) * pi * r ** 3
    elif option23 == 5:
        r = float(input("Enter the value of the radius of the base: "))
        h = float(input("Enter the height value: "))
        resultVolume = (1 / 3) * pi * r ** 2 * h
    elif option23 == 6:
        Abase = float(input("Enter the area of the base: "))
        h = float(input("Enter the height value: "))
        resultVolume = (1 / 3) * Abase * h
    elif option23 == 7:
        Abase = float(input("Enter the area of the base: "))
        h = float(input("Enter the height value: "))
        resultVolume = Abase * h
    
    return resultVolume

def sysLinear(eq1, eq2):
    def parse_equation(equation):
        equation = equation.replace(" ", "")
        lhs, rhs = equation.split("=")
        rhs = float(rhs)
        coefficients = re.findall(r'([+-]?\d*\.?\d*)(x|y)', lhs)
        coeffs = {'x': 0, 'y': 0}
        
        for coeff, var in coefficients:
            coeff_value = float(coeff) if coeff and coeff != '+' and coeff != '-' else float(coeff + '1')
            coeffs[var] += coeff_value
            
        return coeffs['x'], coeffs['y'], rhs

    a1, b1, c1 = parse_equation(eq1)
    a2, b2, c2 = parse_equation(eq2)

    det = a1 * b2 - a2 * b1

    if det == 0:
        raise ValueError("The system does not have a unique solution (the equations are dependent or inconsistent).")

    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    
    return x, y

def verifyCPF(cpf):
    cpf = ''.join([char for char in cpf if char.isdigit()])
    
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return "Invalid CPF"
    
    sum1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    rest1 = sum1 % 11
    digit1 = 0 if rest1 < 2 else 11 - rest1
    
    sum2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    rest2 = sum2 % 11
    digit2 = 0 if rest2 < 2 else 11 - rest2
    
    if int(cpf[9]) == digit1 and int(cpf[10]) == digit2:
        return "Valid CPF"
    else:
        return "Invalid CPF"

def BMI(weight, height):
    weight, height = float(weight), float(height)
    finalBMI = weight / height ** 2

    if finalBMI <= 18.5:
        return f"Underweight, your BMI is: {finalBMI:.2f}"
    elif finalBMI >= 18.51 and finalBMI <= 24.9:
        return f"Normal weight, your BMI is: {finalBMI:.2f}"
    elif finalBMI >= 25 and finalBMI <= 29.9:
        return f"Overweight, your BMI is: {finalBMI:.2f}"
    elif finalBMI >= 30 and finalBMI <= 34.9:
        return f"Obesity grade I, your BMI is: {finalBMI:.2f}"
    elif finalBMI >= 35 and finalBMI <= 39.9:
        return f"Obesity grade II, your BMI is: {finalBMI:.2f}"
    else:
        return f"Obesity grade III (morbid), your BMI is: {finalBMI}"

def rocketSimulator(v0, g):
    v0, g = float(v0), float(g)
    timeToClimb = v0 / g
    maxHeight = (v0 ** 2) / (2 * g)
    totalFlightTime = 2 * timeToClimb

    return f"The rocket would take {round(timeToClimb, 2)} seconds to reach maximum height ({round(maxHeight, 2)}m), and the total flight time would be {round(totalFlightTime, 2)} seconds"

def percentageIncrease(initialValue, finalValue):
    return f"{round(((finalValue - initialValue) / initialValue) * 100, 2)} %"

def compoundInterest(initialCapital, interestRate, periods):
    initialCapital, interestRate, periods = float(initialCapital), float(interestRate), float(periods)
    result = initialCapital * (1 + (interestRate / 100)) ** periods
    return f"{round(result, 2)}"

def averageSpeed(distance, time):
    return f"{round(distance / time, 2)} m/s"

def validateCNPJ(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))
    if len(cnpj) != 14:
        return f"The CNPJ {cnpj} is invalid"
    
    first_digit_weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    second_digit_weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    
    sum = sum(int(cnpj[i]) * first_digit_weights[i] for i in range(12))
    rest = sum % 11
    first_digit = 0 if rest < 2 else 11 - rest
    
    if first_digit != int(cnpj[12]):
        return f"The CNPJ {cnpj} is invalid"
    
    sum = sum(int(cnpj[i]) * second_digit_weights[i] for i in range(13))
    rest = sum % 11
    second_digit = 0 if rest < 2 else 11 - rest
    
    if second_digit != int(cnpj[13]):
        return f"The CNPJ {cnpj} is invalid"
    
    return f"The CNPJ {cnpj} is valid"

def romanConverter(inp):
    inp = int(inp)
    if not isinstance(inp, type(1)):
        return "expected integer, got %s" % type(inp)
    if not 0 < inp < 4000:
        return "Must be a number between 1 and 3999"
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []
 
    for i in range(len(ints)):
        count = int(inp / ints[i])
        result.append(nums[i] * count)
        inp -= ints[i] * count
    return ''.join(result)

def PFDNewton(m, a):
    return f"The force is {m * a} newtons"

def universalGravitation(m1a, m2a, ra):
    m1 = float(eval(m1a))
    m2 = float(eval(m2a))
    r = float(eval(ra))
    
    G = 6.67430e-11

    F = G * (m1 * m2 / (r ** 2))
    
    return f"The gravitational force between Object 1 ({m1}kg) and Object 2 ({m2}kg) is: {F} Newtons"

def gravitationalPotentialEnergy(m, g, h):
    U = m * g * h

    return f"The energy of the object is {U} Joules"

def incomeTax(base):
    if 2826.65 >= base > 2112.00:
        rate = 7.5 / 100
        deduction = 158.4
    elif 3751.05 >= base > 2826.65:
        rate = 15 / 100
        deduction = 370.4
    elif 4664.68 >= base > 3751.05:
        rate = 22.5 / 100
        deduction = 651.73
    else:
        rate = 27.5 / 100
        deduction = 884.96

    if base <= 2112.00:
        tax = 0
    else: 
        tax = (base * rate) - deduction
    return f"R${round(tax, 2):.2f}"

def RGBtoHEX(rgbInp):
    rgbInp = str(rgbInp)
    rgbSplitted = rgbInp.split(",") 
    rgbDiv16 = [float(rgbDivided) / 16 for rgbDivided in rgbSplitted] 
    rgbDiv16Round = [float(f"{int(rgb16Rounding):.0f}") for rgb16Rounding in rgbDiv16] 
    rgbRes = [float(rgbMod) % 16 for rgbMod in rgbSplitted] 
    rgbResHex = [hex(int(hexing))[2:] for hexing in rgbRes] 
    rgbDiv16RoundHex = [hex(int(sixteenhexing))[2:] for sixteenhexing in rgbDiv16Round] 

    RGBHexed = '#' + ''.join([str(a) + str(b) for a, b in zip(rgbDiv16RoundHex, rgbResHex)]) 

    return RGBHexed

def kineticEnergy(m, v):
    EC = (1 / 2) * m * (v ** 2)
    return f"{round(EC):.2f} Joules"

def coulombsLaw(q1, q2, r):
    q1 = float(eval(q1))
    q2 = float(eval(q2))
    ke = 8.99 * (10 ** 9)

    F = ke * (abs(q1 * q2) / (r ** 2))

    return f"{round(F, 2):.2f} Newtons"

def asciiBin(inp):
    if int(inp) == 1:
        inp1 = input("Enter your word/character: ")
        listafod = list(inp1)
        ascii_value = [ord(going) for going in listafod]
        result = ''.join([f"{bin(val)[2:].zfill(8)} " for val in ascii_value])
    elif int(inp) == 2:
        inp1 = input("Enter your value in binary: ")
        listafod = inp1.split()
        binary_value = [int(going, 2) for going in listafod]
        result = ''.join([chr(val) for val in binary_value])

    return result

""" ----------------------------------------- """

def calc():
    clear()
    
    format.print_bold(f"Calculator\n\n{format_options(options)}")
    option = int(input("Choose an operation: "))
    ifop = str(option).isdigit() and int(option) in range(1, len(options) + 1)

    if ifop:
        if option in [1, 2, 3, 14, 17, 18, 19, 13, 10, 20]:
            if option in [2, 3, 14]:
                num3 = float(input("Choose the number: "))
            elif option == 20:
                num3 = int(input("Choose the number: "))
            elif option == 1:
                clear()
                print("+ Addition\n- Subtraction\n* Multiplication\n/ Division\n** Power\n\nExample: (a+b-c*d/e**f)")
                num3 = input("Write your mathematical operation: ")
            elif option in (10, 18, 19):
                num3 = input("Write the list of numbers separated by commas (x,y,z): ")
                if option == 18:
                    num3 = [int(x) for x in num3.split(",")]
                elif option == 19:
                    num3 = tuple(map(int, num3.split(',')))
            elif option == 13:
                num3 = input("Enter your date of birth (YYYY-MM-DD): ")
            elif option == 17:
                num3 = input("Enter the list separated by spaces: ")
        elif option in [4, 15]:
            if option in []:
                num1 = float(input("Choose the first number: "))
                num2 = float(input("Choose the second number: "))
            elif option == 4:
                num1 = float(input("Choose the base number: "))
                num2 = float(input("Choose the percentage: "))
            elif option == 15:
                num1 = float(input("Enter the voltage: "))
                num2 = float(input("Enter the amperage: "))
        elif option in [5, 6, 7, 8, 12]:
            if option in [5, 6]:
                num4 = float(input("Choose the A1 (First term of the progression): "))
                num5 = float(input("Choose the R (Common difference): "))
                num6 = float(input("Choose the N (Number of desired terms): "))
            elif option in [7]:
                format.print_bold("Base: ax - bx + c = 0")
                num4 = float(input("Choose the coefficient 'a': "))
                num5 = float(input("Choose the coefficient 'b': "))
                num6 = float(input("Choose the coefficient 'c': "))
            elif option == 8:
                num4 = float(input("Choose the hours (0-23): "))
                num5 = float(input("Choose the minutes (0-59): "))
                num6 = float(input("Choose the minutes to advance (0-59): "))
            elif option == 12:
                num4 = float(input("Enter the initial value: "))
                num5 = float(input("Enter the rate in decimal (x): "))
                num6 = float(input("Enter the interval (in months): "))
            else:
                num4 = float(input("Choose the first number: "))
                num5 = float(input("Choose the second number: "))
                num6 = float(input("Choose the third number: "))
        elif option == 9:
            clear()
            unit_conversion_options1 = [
                '1. Celsius to Fahrenheit',
                '2. Meters to Feet',
                '3. Kilograms to Pounds'
            ]
            unit_conversion_options2 = [
                '4. Fahrenheit to Celsius',
                '5. Feet to Meters',
                '6. Pounds to Kilograms'
            ]
            
            format.print_bold("\n".join(unit_conversion_options1), "\n-----------------------")
            format.print_bold("\n".join(unit_conversion_options2))
            opconv = int(input("Which measurement would you like to convert? "))
            
            ifopconv = str(opconv).isdigit() and int(opconv) in range(1, len(unit_conversion_options1) + len(unit_conversion_options2) + 1)

            if ifopconv:
                if opconv in [1, 2, 3, 4, 5, 6]:
                    if opconv == 1:
                        opconvmed = float(input("Celsius: "))
                    elif opconv == 2:
                        opconvmed = float(input("Meters: "))
                    elif opconv == 3:
                        opconvmed = float(input("Kilograms: "))
                    elif opconv == 4:
                        opconvmed = float(input("Fahrenheit: "))
                    elif opconv == 5:
                        opconvmed = float(input("Feet: "))
                    elif opconv == 6:
                        opconvmed = float(input("Pounds: "))
            else:
                print("Invalid option, it must be a number between 1 and", (len(unit_conversion_options1) + len(unit_conversion_options2)), ", and you selected: \n>", opconv, "<\nYour silly")
                exit()
        elif option == 11:
            clear()
            base_conversion_options1 = [
                '1. Decimal to binary',
                '2. Decimal to octal',
                '3. Decimal to hexadecimal'
            ]
            base_conversion_options2 = [
                '4. Binary to decimal',
                '5. Octal to decimal',
                '6. Hexadecimal to Decimal'
            ]
            
            format.print_bold("\n".join(base_conversion_options1), "\n-----------------------")
            format.print_bold("\n".join(base_conversion_options2))
            opconvbase = int(input("Which base would you like to convert? "))
            
            ifopconvbase = str(opconvbase).isdigit() and int(opconvbase) in range(1, len(base_conversion_options1) + len(base_conversion_options2) + 1)

            if ifopconvbase:
                opconvbase = int(opconvbase)
                if opconvbase in [1, 2, 3]:
                    opconvbaseop = int(input("Decimal: "))
                elif opconvbase == 4:
                    opconvbaseop = int(input("Binary: "))
                elif opconvbase == 5:
                    opconvbaseop = int(input("Octal: "))
                elif opconvbase == 6:
                    opconvbaseop = input("Hexadecimal: ")
            else:
                print("Invalid option, it must be a number between 1 and", (len(base_conversion_options1) + len(base_conversion_options2)), ", and you selected: \n>", opconvbase, "<\nYour silly")
                exit()
        elif option == 16:
            clear()
            currency_conversion_options1 = [
                '1. Real to Dollar',
                '2. Real to Euro',
                '3. Real to Argentine Peso',
                '4. Real to Bitcoin'
            ]
            currency_conversion_options2 = [
                '5. Dollar to Real',
                '6. Euro to Real',
                '7. Argentine Peso to Real',
                '8. Bitcoin to Real'
            ]
            
            format.print_bold("\n".join(currency_conversion_options1), "\n-----------------------")
            format.print_bold("\n".join(currency_conversion_options2))
            opconvmony = int(input("Which base would you like to convert? "))
            
            ifopconvmony = str(opconvmony).isdigit() and int(opconvmony) in range(1, len(currency_conversion_options1) + len(currency_conversion_options2) + 1)

            if ifopconvmony:
                opconvmony = int(opconvmony)
                if opconvmony in [1, 2, 3, 4]:
                    opconvmonyop = float(input("Real: "))
                elif opconvmony == 5:
                    opconvmonyop = float(input("Dollar: "))
                elif opconvmony == 6:
                    opconvmonyop = float(input("Euro: "))
                elif opconvmony == 7:
                    opconvmonyop = float(input("Argentine Peso: "))
                elif opconvmony == 8:
                    opconvmonyop = float(input("Bitcoin: "))
            else:
                print("Invalid option, it must be a number between 1 and", (len(currency_conversion_options1) + len(currency_conversion_options2)), ", and you selected: \n>", opconvmony, "<\nYour silly")
                exit()
        elif option == 21:
            clear()
            format.print_bold("Which shape would you like to calculate?\n\n1. Rectangle / Parallelogram\n2. Triangle\n3. Square / Rhombus")
            option21 = int(input(">> "))
        elif option == 22:
            clear()
            format.print_bold("Which shape would you like to calculate?\n\n1. Parallelogram\n2. Rectangle\n3. Square\n4. Rhombus\n5. Triangle\n6. Trapezoid\n7. Circle")
            option22 = int(input(">> "))
        elif option == 23:
            clear()
            format.print_bold("Which shape would you like to calculate?\n\n1. Cube\n2. Rectangular Prism\n3. Cylinder\n4. Sphere\n5. Cone\n6. Pyramid\n7. Prism")
            option23 = int(input(">> "))
        elif option == 24:
            clear()
            eq1 = input("Enter the first equation (e.g., x + y = 5): ")
            eq2 = input("Enter the second equation (e.g., x - y = -35): ")
        elif option == 25:
            option25 = input("Enter the CPF to be verified: ")
        elif option == 26:
            clear()
            option26weight = input("Enter your weight: ")
            option26height = input("Enter your height: ")
        elif option == 27:
            clear()
            initialVelocity = input("What is the initial velocity of the rocket (m/s)? ")
            gravityAcceleration = input("What is the value of gravity (m/s², on Earth it is 9.81)? ")
        elif option == 28:
            initialValue = float(input("Enter the initial value: "))
            finalValue = float(input("Enter the final value: "))
        elif option == 29:
            clear()
            initialCapital = input("Enter the initial capital amount: ")
            interestRate = input("Enter the interest rate you would like to apply: ")
            periods = input("Enter the number of periods: ")
        elif option == 30:
            clear()
            distance = float(input("Enter the distance traveled (in meters): "))
            time = float(input("Enter how long it took (in seconds): "))
        elif option == 31:
            clear()
            cnpj = input("Enter the CNPJ (xxxxxxxx/0001-yy): ")
        elif option == 32:
            clear()
            option32 = input("Enter a number between 1 and 3999: ")
        elif option == 33:
            clear()
            mass = float(input("Enter the mass of the object (kg): "))
            acceleration = float(input("Enter the acceleration of the object (m/s²): "))
        elif option == 34:
            clear()
            mass1 = input("Enter the mass of Object 1 (Kg): ")
            mass2 = input("Enter the mass of Object 2 (Kg): ")
            distanceBetween2Bodies = input("Enter the distance between the 2 objects (m): ")
        elif option == 35:
            clear()
            mass = float(input("Enter the mass of the object (Kg): "))
            gravity = float(input("Enter the acceleration due to gravity (m/s², approximately 9.81 m/s² on Earth): "))
            heightObj = float(input("Enter the height of the object above the ground (m): "))
        elif option == 36:
            clear()
            monthlyIncome = float(input("Enter your monthly income: "))
        elif option == 37:
            clear()
            rgbInput = input("Enter the color in RGB (255,255,255): ")
        elif option == 38:
            clear()
            mass3 = float(input("Enter the mass of the object (kg): "))
            velocity3 = float(input("Enter the velocity of the object (m/s): "))
        elif option == 39:
            clear()
            chargeMagnitude1 = input("Enter the magnitude of the first charge (C): ")
            chargeMagnitude2 = input("Enter the magnitude of the second charge (C): ")
            distance = float(input("Enter the distance between the charges (m): "))
        elif option == 40:
            clear()
            inp = input("1. ASCII -> Binary\n2. Binary -> ASCII\n\n>>")
    else:
        clear()
        print(f"Invalid option, it must be a number between 1 and {len(options)}, and you selected: \n>{option}<\nYour silly")
        exit()

    match option:
        case 1:
            printResult(basic(num3))
            exit()
        case 2:
            printResult(sqrt(num3))
            exit()
        case 3:
            printResult(factorial(num3))
            exit()
        case 4:
            printResult(percentage(num1, num2))
            exit()
        case 5:
            printResult(AP(num4, num5, num6))
            exit()
        case 6:
            printResult(GP(num4, num5, num6))
            exit()
        case 7:
            printResult(EQ(num4, num5, num6))
            exit()
        case 8:
            printResult(hours(num4, num5, num6))
            exit()
        case 9:
            printResult(convertUnit(opconvmed, opconv))
            exit()
        case 10:
            printResult(average(num3))
            exit()
        case 11:
            printResult(convertBases(opconvbaseop, opconvbase))
            exit()
        case 12:
            printResult(simpleInterest(num4, num5, num6))
            exit()
        case 13:
            printResult(age(num3))
            exit()
        case 14:
            printResult(randomNum(num3))
            exit()
        case 15:
            printResult(energy(num1, num2))
            exit()
        case 16:
            printResult(currencyConverter(opconvmony, opconvmonyop))
            exit()
        case 17:
            printResult(findNum(num3))
            exit()
        case 18:
            printResult(calculate_lcm(*num3))
            exit()
        case 19:
            printResult(calculate_gcd(*num3))
            exit()
        case 20:
            printResult(checkPrime(num3))
            exit()
        case 21:
            printResult(perimeter(option21))
            exit()
        case 22:
            printResult(area(option22))
            exit()
        case 23:
            printResult(volume(option23))
            exit()
        case 24:
            solution = sysLinear(eq1, eq2)
            print(f"Solution of the system: x = {solution[0]}, y = {solution[1]}")
            exit()
        case 25:
            print(verifyCPF(option25))
            exit()
        case 26:
            print(BMI(option26weight, option26height))
            exit()
        case 27:
            print(rocketSimulator(initialVelocity, gravityAcceleration))
            exit()
        case 28:
            printResult(percentageIncrease(initialValue, finalValue))
            exit()
        case 29:
            printResult(compoundInterest(initialCapital, interestRate, periods))
            exit()
        case 30:
            print(averageSpeed(distance, time))
            exit()
        case 31:
            print(validateCNPJ(cnpj))
            exit()
        case 32:
            print(romanConverter(option32))
            exit()
        case 33:
            print(PFDNewton(mass, acceleration))
            exit()
        case 34:
            print(universalGravitation(mass1, mass2, distanceBetween2Bodies))
            exit()
        case 35:
            print(gravitationalPotentialEnergy(mass, gravity, heightObj))
            exit()
        case 36:
            print(incomeTax(monthlyIncome))
            exit()
        case 37:
            print(RGBtoHEX(rgbInput))
            exit()
        case 38:
            print(kineticEnergy(mass3, velocity3))
            exit()
        case 39:
            print(coulombsLaw(chargeMagnitude1, chargeMagnitude2, distance))
            exit()
        case 40:
            print(asciiBin(inp))
            exit()

calc()
