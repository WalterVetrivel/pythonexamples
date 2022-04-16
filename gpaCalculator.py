# # Author: Walter Selvakumar
# # Date created: 16 April 2022
# # Date last changed: 16 April 2022
# # A program to calculate the GPA and WAM of a student based on entered grades.
# # GPA = sum(Grade Score * Credit Points) / sum(Credit Points)
# # WAM = sum(Marks * Credit Points) / sum(Credit Points)
# # More details: https://www.canberra.edu.au/Policies/PolicyProcedure/Index/534
# # Input: Grade scores, marks & credit points for N units
# # Output: The GPA and WAM of the student based on the inputs

MAX_UNITS = 40
GRADE_SCORES = {
    'HD': 7,
    'DI': 6,
    'CR': 5,
    'P': 4,
    'NC': 0
}


def getIntegerInput(label):
    '''A function to read an integer value as input'''
    while True:
        try:
            value = int(input(label))
            return value  # If the entered value is a valid integer, just return it, which also breaks out of the loop
        except ValueError or TypeError:
            # If it's not an integer, then the loop continues as there is no break or return statement
            print('Please enter a valid integer')


def calculateGrade(marks):
    '''A function to calculate the grade (HD, DI, CR, P, NC) based on the marks'''
    if marks >= 85:
        return 'HD'
    if marks >= 75:  # No need to check whether it is less than 85 as if it isn't, then the function would already have returned 'HD'
        return 'DI'
    if marks >= 65:
        return 'CR'
    if marks >= 50:
        return 'P'
    else:
        return 'NC'


def generateUnitDict(creditPoints, marks):
    '''A function to create a dictionary to store the details of a unit'''
    return {
        'creditPoints': creditPoints,
        'marks': marks,
        'grade': calculateGrade(marks)
    }


def readUnitDetails(numberOfUnits):
    '''A function to read the details of N units and return it as a list'''
    unitsList = []
    unitCounter = 0

    while unitCounter < numberOfUnits:
        unitCreditPoints = getIntegerInput(
            f'Enter the number of credit points for unit {unitCounter + 1}: ')
        unitMarks = getIntegerInput(
            f'Enter your marks for unit {unitCounter + 1}: ')

        unitsList.append(generateUnitDict(unitCreditPoints, unitMarks))

        unitCounter += 1

    return unitsList


def calculateWAM(unitsList):
    weightedMarks = []
    totalCreditPoints = 0

    for unit in unitsList:
        weightedMarks.append(unit['creditPoints'] * unit['marks'])
        totalCreditPoints += unit['creditPoints']

    weightedAverageMark = sum(weightedMarks) / totalCreditPoints
    return weightedAverageMark


def getGradeScore(grade):
    return GRADE_SCORES[grade]


def calculateGPA(unitsList):
    weightedGradeScores = []
    totalCreditPoints = 0

    for unit in unitsList:
        unitGradeScore = getGradeScore(unit['grade'])
        weightedGradeScores.append(unit['creditPoints'] * unitGradeScore)
        totalCreditPoints += unit['creditPoints']

    gradePointAverage = sum(weightedGradeScores) / totalCreditPoints
    return gradePointAverage


def main():
    numberOfUnits = min(getIntegerInput(
        'Enter the number of units for which to calculate GPA & WAM: '), MAX_UNITS)

    unitsList = readUnitDetails(numberOfUnits)
    weightedAverageMark = calculateWAM(unitsList)
    gradePointAverage = calculateGPA(unitsList)
    
    print(weightedAverageMark)
    print(gradePointAverage)


main()
