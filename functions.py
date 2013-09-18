'''
--------------------------------
Name: Dallas Fraser
Date: 09/14/2013
Purpose: A module I created to help parse info and calculate things
---------------------------------
'''
import unittest
import math
EMPIRICAL = {'68':1, '95':2, '99.7':3}

def find_median(array):
    '''
    a function to calculate the median of the list
    Parameters: 
        array: a list of numbers
    Returns:
        median: the median of the list (float)
    '''
    array = sorted(array) 
    length = len(array)
    if length % 2 == 0:
        median = (array[length//2] + array[(length//2) - 1]) / 2
    else:
        median = array[length//2]
    return median

def find_mode(array):
    '''
    a function that finds the mode of the array
    Parameters: 
        array: a list of numbers
    Returns:
        modes: an list of all the modes if no mode [] (list)
    '''
    array = sorted(array)
    bucket = {}
    for point in array:
        if point in bucket:
            bucket[point] += 1
        else:
            bucket[point] = 1
    modes = []
    max_value = 0
    for number, count in bucket.items():
        if count > max_value:
            modes = [number]
            max_value = count
        elif count == max_value:
            modes.append(number)
    if len(modes) == len(array):
        modes = []
    return modes

def find_range(array):
    '''
    a function that finds the range of the array
    Parameters: 
        array: a list of numbers
    Returns:
        range_value: the range of the data (float)
    '''
    min_value = array[0]
    max_value = array[0]
    for number in array[1:]:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number
    range_value = max_value - min_value
    return range_value

def find_average(array):
    '''
    a function that finds the mean of the array
    Parameters: 
        array: a list of numbers
    Returns:
        mean: the mean of the data (float)
    '''
    aggregate = 0
    for number in array:
        aggregate += number
    mean = aggregate / len(array)
    return mean

def find_mad(array):
    '''
    a function that finds the mean absolute deviation
    Parameters: 
        array: a list of numbers
    Returns:
        mad: the mean absolute deviation (float)
    '''
    mean = find_average(array)
    aggregate = 0 
    for number in array:
        aggregate += abs(number - mean)
    mad = aggregate / len(array)
    return mad

def find_variance(array):
    '''
    a function that finds the variance of the data
    Parameters: 
        array: a list of numbers
    Returns:
        variance: the variance of the data (float)
    '''
    aggregate = 0
    average = find_average(array)
    for number in array:
        aggregate += (number - average) ^ 2
    variance = aggregate / len(array)
    return variance

def find_standard_deviation(array):
    '''
    a function that finds the standard deviation
    Parameters: 
        array: a list of numbers
    Returns:
        : the standard deviation (float)
    '''
    return math.sqrt(find_variance)
    
def make_array(numbers):
    '''
    a function that takes a column delimited string and makes it an array
    Parameters: 
        numbers: the string of inputs
    Returns:
        array: an array representing the input numbers 
               or empty array if unable to parse
    '''
    # get rid of and and spaces
    numbers = numbers.replace(" ", "")
    numbers = numbers.replace("and", ",")
    numbers = numbers.replace(",,", ",")
    numbers = numbers.split(sep=",")
    array = []
    try:
        for number in numbers:
            array.append(int(number))
        return array
    except:
        return []

def apply_empirical_rule(deviation, average):
    '''
    a function that applys the empircal rule and returns the ranges
    Parameters: 
        deviation: the standard deviation of the set
        average: the avergae of the set
    Returns:
        python dictionary { 'percent_range': min-max ...}
    '''
    ranges = {}
    for percent, num_std_dev in EMPIRICAL.items():
        min_value = average - num_std_dev * deviation
        max_value = average + num_std_dev * deviation
        ranges[percent] =  min_value + "-" + max_value 
    return ranges

class testFunctions(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_find_average(self):
        array = [1,2,3]
        mean = find_average(array)
        self.assertEqual(mean, 2)
        array = [3,3,3]
        mean = find_average(array)
        self.assertEqual(mean, 3)
        array = [1.5,2.0,2.5]
        mean = find_average(array)
        self.assertEqual(mean, 2.0)
        
    def test_find_range(self):
        array = [1,2,3,4,5]
        result = find_range(array)
        self.assertEqual(result,4)
        array = [1]
        result = find_range(array)
        self.assertEqual(result,0)
        array = [1,2,3,4,8]
        result = find_range(array)
        self.assertEqual(result,7)
        
    def test_find_mode(self):
        array = [1,2,3,1,2]
        modes = find_mode(array)
        self.assertEqual(modes, [1,2])
        array = [1,2,3,4,5]
        modes = find_mode(array)
        self.assertEqual(modes, [])        
        array = [1,2,1,4,1]
        modes = find_mode(array)
        self.assertEqual(modes, [1])
    
    def test_make_array(self):
        string = '41, 42, and 41'
        array = make_array(string)
        self.assertEqual(array, [ 41,42,41])
        string = '41, 42 and 41'
        array = make_array(string)
        self.assertEqual(array, [ 41,42,41])
        string = '41, 42, 41'
        array = make_array(string)
        self.assertEqual(array, [ 41,42,41])
        string = '41,42,41, and 100'
        array = make_array(string)
        self.assertEqual(array, [ 41,42,41,100])
        string = '41,42,x, and 100'
        array = make_array(string)
        self.assertEqual(array, [])
        
    def test_find_median(self):
        array = [1,2,3]
        result = find_median(array)
        self.assertEqual(result, 2)
        array = [2,1,3]
        result = find_median(array)
        self.assertEqual(result, 2)
        array = [1,2,3,4]
        result = find_median(array)
        self.assertEqual(result, 2.5)
        array = [1,4,3,2]
        result = find_median(array)
        self.assertEqual(result, 2.5)
    
    def test_find_mad(self):
        array = [1,2,3]
        mad = find_mad(array)
        self.assertEqual(mad,(2/3))
        
        
