# Shania Ie
# lab 1
# CIS 41B

# Description:
# The Record class parses the file and puts the information into the appropriate data structures.
# It also prints the data, returns the student name and checks whether the inputted grade exists
# Data structure: 2D list - Outer list: Stores the class information
#                         - Inner list: Stores the class name, units and grade of student

class Record:
    def __init__(self, sentence):
        '''
        Constructor:
        Accepts one line of the input file, parses (separates) the line into 
        data values and stores them in the data structure.
        '''
        self.sentence = sentence.rstrip().split(',')
        self.studentname = self.sentence[0]
        
        # raise an exception so that main can print an error message and end the program.
        if int(len(self.sentence) - 1) % 3 != 0:
            raise ValueError(sentence)
        self.row = int((len(self.sentence) - 1) / 3)
        
        # create a 2D list for the classList
        # slicing starts form i*3+1 to i*3+4, here it is required to multiply it
        # by 3 as we want to get the next 3 values
        self.classList = [self.sentence[i*3+1:i*3+4] for i in range(self.row)]
        
    def printData(self):
        '''
        printData:
        prints the student record in multiple lines
        '''
        print(self.studentname)
        for i in sorted(self.classList):
            print("{:8s}: {:4s} {:3s}".format(i[0], i[1], i[2]))
        
    def getName(self):
        '''
        getName:
        returns the student name
        '''
        return self.studentname
    
    def hasGrade(self, grade):
        '''
        hasGrade:
        accepts a letter grade andreturns True if the student record has
        that grade, False otherwise. 
        '''
        for row in self.classList:
            if grade in row:
                return True
        return False  