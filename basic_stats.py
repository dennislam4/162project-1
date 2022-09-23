# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 09-21-2022
# Description: A class named student that uses two private data members of a student's name and grade. Alongside is a
# separate function called basic_stats which takes as a parameter a list of student objects and returns a tuple that has
# the mean, median, and mode of the grades. Mean, median, and mode functions are imported from the statistics library in
# order to perform the calculations.

from statistics import mean
from statistics import median
from statistics import mode

class Student:
    """
    Represents student information which contatins their name and grade.
    """
    def __init__(self, name, grade):
        """Initializes the name and grade parameters of student."""
        self._name = name
        self._grade = grade

    def get_grade(self):
        """Get grade method. Used to get the grade value from the student information."""
        return self._grade

def basic_stats(student_list):
    """
    First creates an empty list from which the grade value is appended in from using the get_grade method. Takes the grade
    values from the list of students given and then using the statistics library, returns the mean, median, and mode of
    student grades in an ordered tuple.
    """
    grades = []
    for grade in student_list:
        grades.append(grade.get_grade())
        grade_mean = mean(grades)
        grade_median = median(grades)
        grade_mode = mode(grades)
    return (grade_mean,grade_median,grade_mode)
