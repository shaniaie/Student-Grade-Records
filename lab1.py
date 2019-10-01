# Shania Ie
# Lab 1
# CIS 41B

# Description:
# The Lab 1 file reads in the data from the txt file, prints the student records, prompts
# the user to enter one of the following (search for one record, grade count or quit). For
# the search function, it prints out the student name in a sorted manner according to their
# last name. Grade count lets the user to search the grades of the student and displays how 
# many student gets the following grade. 

from record import Record

def getData():
    '''
    getData:
    Accept a filename or use the default filename lab1in.txt
    Read in from the file and create a list of Record objects
    If the file open is not successful or if the Record object raises an exception,
    print a descriptive error message and end the program
    '''
    try:
        DEFAULTFILE = 'lab1in.txt'
        fileName = input("Please enter file name or hit Enter for default file: ")
        if fileName == '':
            fileName = DEFAULTFILE        
        
        recordList = []
        with open (fileName) as inFile:
            for line in inFile:
                s = Record(line)
                recordList.append(s)
        return recordList
    
    except FileNotFoundError:
        raise SystemExit(fileName + " not found")
    
def printAll(dataList):
    '''
    printAll:
    Call the print method of each Record object in the list.
    '''
    for d in dataList:
        d.printData()

def getChoice(sequence):
    '''
    getChoice:
    Get a choice from the user and keeps prompting the user until there is a 
    valid choice and then return the choice
    '''
    print('\ns. search for one record\ng. grade count\nq. quit')
    userInput = input("\nEnter your choice: ")
    while True:
        try:
            return sequence[userInput]
        except KeyError:
            print('Input does not exist')  
        userInput = input("Enter your choice: ")
    print()    
        
def userProcess(dataList):
    '''
    userProcess:
    Call the getChoice function above to get a valid choice
    As long as the choice is not 'q', call a search function or a countGrade function to process the user choice.
    Keep looping until the user choice is 'q'
    '''
    charOption = {'s': 0, 'g': 1, 'q': 2}
    printList = [search, countGrade]
    resultChoice = getChoice(charOption)
    
    while resultChoice != 2:
        printList[resultChoice](dataList)
        resultChoice = getChoice(charOption)
    
def search(dataList):
    '''
    search:
    Create a generator to return one student record at a time. 
    The student records are returned in alphabetical order by student last name.
    Loop to let the user press the Enter key to get the next student record, 
    or enter any other key to stop the search. 
    '''
    print("\nPrinting one student record one at a time")
    studentGen = (s for s in sorted(dataList, key = lambda s:s.getName().split(' ')[-1]))
    val = next(studentGen)
    val.printData()
    inputChoice = input('Press Enter for next name, anything else to quit: ')
    
    while inputChoice == '':
        try:
            val = next(studentGen)
            val.printData()
            inputChoice = input('Press Enter for next name, anything else to quit: ') 
        except StopIteration:
            print("End of student records")
            inputChoice = ' '
        
def countGrade(dataList):
    '''
    countGrade: 
    Keep prompting the user for a grade until there is a valid grade 
    Print an error message to remind the user of the valid grades if the grade is not valid
    Call a findGrade function to print the number of students that have the user input grade.
    '''
    gradeTuple = ('A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D','D-', 'F')
    inputLetter = input("Input letter grade: ")
    
    while inputLetter not in gradeTuple:
        print("Grade should be A-F with optional + and -")
        inputLetter = input("Input letter grade: ")
    
    findGrade(dataList, inputLetter)

def check(f):
    '''
    check:
    Keep track of whether an input string argument has already been passed to the function
    Prints out the inputted string arguments in a set
    '''
    enteredGrades = set()
    def wrapper(*args,**kwargs):     
        for elem in args:
            try:
                if elem not in enteredGrades:
                    enteredGrades.add(elem)
                    print(enteredGrades)
                    return f(*args, **kwargs)
                print("Already searched this grade")
            except TypeError:
                pass  
        for elem in kwargs.values():
            try:
                if elem not in enteredGrades:
                    enteredGrades.add(elem)
                    print(enteredGrades)
                    return f(*args, **kwargs)
                print("Already searched this grade")
            except TypeError: 
                pass        
    return wrapper

@check
def findGrade(dataList, inputLetter):
    '''
    findGrade:
    Call the hasGrade method of each Record object, and use the return value to count
    the number of students with the user input grade. Print the number of students with that grade.
    '''
    grade = 0
    for d in dataList:
        if d.hasGrade(inputLetter) == True:
            grade += 1
    print(grade,"student(s) with grade",inputLetter)


def main():
    try:
        dataList = getData()
        printAll(dataList)
        userProcess(dataList)
        
    except ValueError as e:
        print("line: " + str(e) + "is not available")

main()