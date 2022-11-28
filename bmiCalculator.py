# height weight constants 

MAX_HEIGHT_RECORDED_IN_CM = 272 
MAX_WEIGHT_RECORDED_IN_KG = 635
MIN_HEIGHT_RECORDED_IN_CM = 54.6
MIN_WEIGHT_RECORDED_IN_KG = 2.13

# converter functions

def feetToCentimeters(feet):
    return feet * 30.48

def inchesToCentimeters(inches):
    return inches * 2.54

def meterToCentimeters(meter):
    return meter * 100

def milliGramToKiloGram(milliGram):
    return milliGram / 1000000

def gramToKilogram(gram):
    return gram / 1000

def poundToKilogram(pound):
    return pound / 2.205

def tonneToKilogram(tonne):
    return tonne * 1000

# bmi calculation function

def calculateBmi(height, weight):
    return weight / ((height / 100) ** 2)

def isHeightValid(height):
    return height < MAX_HEIGHT_RECORDED_IN_CM and height > MIN_HEIGHT_RECORDED_IN_CM

def isWeightValid(weight):
    return weight < MAX_WEIGHT_RECORDED_IN_KG and weight > MIN_WEIGHT_RECORDED_IN_KG

# helper functions 

def getHealthMessage(bmi):
    if bmi <= 15: return "Severely Underweight" 
    if bmi <= 18.5: return "Underweight"
    if bmi > 18.5 and bmi <= 25: return "Normal - Healthy Weight"
    if bmi > 25 and bmi < 39.9: return "Overweight"
    return "Severely Overweight (Obese)"

def updateToCentimeter(heightUnit):
    height = int(input("Enter height "))
    if heightUnit == 'feet': return feetToCentimeters(height)
    if heightUnit == 'inches': return inchesToCentimeters(height)
    if heightUnit == 'meter': return meterToCentimeters(height)
    return height

def updateToKilogram(weightUnit):
    weight = int(input("Enter weight "))
    if weightUnit == 'milligram': return milliGramToKiloGram(weight)
    if weightUnit == 'gram': return gramToKilogram(weight)
    if weightUnit == 'pounds': return poundToKilogram(weight)
    if weightUnit == 'tonne': return tonneToKilogram(weight)
    return weight

def getWeightUnit(weightUnitsList):
    print()
    print('1 - Tonne')
    print('2 - Kilogram')
    print('3 - Pounds')
    print('4 - Gram')
    print('5 - Milligram')
    print()
    unit = int(input("Choose weight unit "))
    if unit > 5 and unit < 1:
        print(f'Sorry!, {unit} is not valid unit')
        return
    print()
    return weightUnitsList[unit-1]

def getHeightUnit(heightUnitsList):
    print('1 - Feet')
    print('2 - Inches')
    print('3 - Centimeter')
    print('4 - Meter')
    print()
    unit = int(input("Choose height unit "))
    if unit > 4 and unit < 1:
        print(f'Sorry!, {unit} is not valid unit')
        return
    print()
    return heightUnitsList[unit-1]

weightUnitsList = ['tonne', 'kilogram', 'pounds', 'gram', 'milligram']
heightUnitsList = ['feet', 'inches', 'centimeter', 'meter']

print()
print("********** BMI CALCULATOR **********")
print()

weightUnit = getWeightUnit(weightUnitsList)

heightUnit = getHeightUnit(heightUnitsList)

height = updateToCentimeter(heightUnit)

weight = updateToKilogram(weightUnit)

if isHeightValid(height) == False or isWeightValid(weight) == False: exit()

bmi = calculateBmi(height, weight)

bmiResults = getHealthMessage(bmi)

print(f'\nBMI = {bmi} kg/m2 ({bmiResults})')