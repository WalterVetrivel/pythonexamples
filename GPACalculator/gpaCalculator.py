# # Author: Walter Selvakumar
# # Date created: 16 April 2022
# # Date last changed: 16 April 2022
# # A program to calculate the GPA and WAM of a student based on entered grades.
# # GPA = sum(Grade Score * Credit Points) / sum(Credit Points)
# # WAM = sum(Marks * Credit Points) / sum(Credit Points)
# # More details: https://www.canberra.edu.au/Policies/PolicyProcedure/Index/534
# # Input: Grade scores, marks & credit points for N units
# # Output: The GPA and WAM of the student based on the inputs

# Global constants
MAX_UNITS = 40  # Assigned as 40 assuming a 5 year degree with 4 units every semester
GRADE_SCORES = {
    'HD': 7,
    'DI': 6,
    'CR': 5,
    'P': 4,
    'NC': 0
}


def getIntegerInput(label: str):
    '''A function to read an integer value as input'''

    while True:
        try:
            value = int(input(label))
            return value  # If the entered value is a valid integer, just return it, which also breaks out of the loop
        except ValueError or TypeError:
            # If it's not an integer, then the loop continues as there is no break or return statement
            print('Please enter a valid integer')


def calculateGrade(marks: int):
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


def generateUnitDict(unitCode: str, creditPoints: int, marks: int):
    '''A function to create a dictionary to store the details of a unit'''

    return {
        'unitCode': unitCode,
        'creditPoints': int(creditPoints),
        'marks': int(marks),
        'grade': calculateGrade(int(marks))
    }


def readUnitDetails(fileName: str):
    '''A function to read the unit details from a file and return it as a list'''

    gradesFile = open(f'files/{fileName}.txt', 'r')

    unitsList = []
    for line in gradesFile.readlines():
        unitDetails = line.strip().split(', ')

        unitsList.append(generateUnitDict(
            unitDetails[0], unitDetails[1], unitDetails[2]))

    gradesFile.close()

    return unitsList


def getUnitDetails(numberOfUnits: int):
    '''A function to get the details of N units as input and return it as a list'''

    unitsList = []
    unitCounter = 0

    while unitCounter < numberOfUnits:
        unitCode = input('Enter the unit code: ')
        unitCreditPoints = getIntegerInput(
            f'Enter the number of credit points for unit {unitCounter + 1}: ')
        unitMarks = getIntegerInput(
            f'Enter your marks for unit {unitCounter + 1}: ')

        unitsList.append(generateUnitDict(
            unitCode, unitCreditPoints, unitMarks))

        unitCounter += 1

    return unitsList


def calculateWAM(unitsList: list):
    '''A function to calculate the weighted average mark using marks and credit points'''

    weightedMarks = []
    totalCreditPoints = 0

    for unit in unitsList:
        weightedMarks.append(unit['creditPoints'] * unit['marks'])
        totalCreditPoints += unit['creditPoints']

    weightedAverageMark = sum(weightedMarks) / totalCreditPoints
    return weightedAverageMark


def getGradeScore(grade: str):
    '''A function to get the grade score corresponding to the grade'''

    return GRADE_SCORES[grade]


def calculateGPA(unitsList: list):
    '''A function to calculate the grade point average using grade scores and credit points'''

    weightedGradeScores = []
    totalCreditPoints = 0

    for unit in unitsList:
        unitGradeScore = getGradeScore(unit['grade'])

        weightedGradeScores.append(unit['creditPoints'] * unitGradeScore)
        totalCreditPoints += unit['creditPoints']

    gradePointAverage = sum(weightedGradeScores) / totalCreditPoints
    return gradePointAverage


def displayUnitGrades(unitsList: list):
    for unit in unitsList:
        print(
            f"{unit['unitCode']}\t{unit['creditPoints']}\t{unit['marks']}\t{unit['grade']}")


def printMenu(title: str, options: list):
    maxLen = 0
    optNumber = 1

    print('-' * len(str(title).upper()))
    print('{0:^s}'.format(title))
    print('-' * len(str(title)))

    for option in options:
        print(f'{optNumber}. {option}')

        if len(option) > maxLen:
            maxLen = len(option)

        optNumber += 1

    print('-' * (maxLen + 3))


def validateChoice(minChoice: int, maxChoice: int, actualChoice: int):
    if actualChoice in range(minChoice, maxChoice + 1):
        return True

    return False


def getChoice(min: int, max: int):
    while True:
        choice = getIntegerInput('Please enter your choice: ')

        if not validateChoice(min, max, choice):
            print(
                f'Invalid choice. Please enter a number between {min} & {max}.')
        else:
            return choice


def inputMenu():
    while True:
        printMenu('Menu', ['Load grade data from file',
                           'Enter new grade data', 'Exit'])
        choice = getChoice(1, 3)

        if choice == 1:
            try:
                inputFileName = input(
                    'Enter the file name to get grade data: ')

                unitsList = readUnitDetails(inputFileName)
                return unitsList
            except:
                print(
                    'Unable to read the file specified. The file may not exist or the contents might be unreadable. Try again.')
                continue
        elif choice == 2:
            numberOfUnits = min(getIntegerInput(
                'Enter the number of units you want to enter the details for: '), MAX_UNITS)

            unitsList = getUnitDetails(numberOfUnits)
            return unitsList
        elif choice == 3:
            print('Thank you for using our program. Goodbye.')
            exit()


def main():
    print('Welcome to the GPA and WAM calculator.'.upper())

    unitsList = inputMenu()

    while True:
        printMenu('Options', [
                  'Show grade details', 'Calculate GPA', 'Calculate WAM', 'Update grade details', 'Exit'])
        choice = getChoice(1, 5)

        if choice == 1:
            displayUnitGrades(unitsList)
        elif choice == 2:
            gpa = calculateGPA(unitsList)
            print(f'Your GPA is: {gpa}')
        elif choice == 3:
            wam = calculateWAM(unitsList)
            print(f'Your WAM is: {wam}')
        elif choice == 4:
            pass
        elif choice == 5:
            print('Thank you for using our program. Goodbye.')
            exit()


main()
