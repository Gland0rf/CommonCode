class String:
    def removeLastEmptySpace(input):
        '''Removes the last empty space of a String (if exists)'''
        input = input.split("\n")
        if input[-1] == "": del input[-1]
        output = "\n".join(input)
        return output
    
class Array:
    def getFromXToY(array, start, end):
        '''
        Get all the values from x to y of an array\n
        Array - The array to check\n
        Start - The start index (starting with 0)\n
        End - The ending index (starting with 0)\n
        Returns an array
        '''

        start -= 1

        return array[start:end]
    
    def sumOfArray(array):
        '''
        Calculates the sum of all indexes (Integers)\n
        Array - The input array\n
        Returns the sum
        '''

        sum = 0
        for i in array:
            sum += int(i)
        return sum
    
    def findHighestSumInLine(array):
        '''
        Tries to fiend the highest possible sum in an int array\n
        Note that the sum can not be formed by randomly taking indexes of the array,
        but they have to be in one line.\n
        Example - 1 2 5 -10 2 4 5 -5\n
        In this example, 2-4-5 is the highest possible Combination\n
        Array - The Array to check\n
        Returns the highest sum, the possiblities and the start pos and the end pos of each possibility\n
        '''
        max_sum = float("-inf")
        current_sum = 0
        start = end = temp_start = 0
        possibilities = []

        for i, num in enumerate(array):
            num = int(num)
            if current_sum + num < num:
                temp_start = i
                current_sum = num
            else:
                current_sum += num

            if current_sum > max_sum:
                start = temp_start
                end = i
                max_sum = current_sum
                possibilities = [(start, end)]
            elif current_sum == max_sum:
                possibilities.append((temp_start, i))

        return max_sum, len(possibilities), possibilities
        
class Time:
    def convertTimeToSeconds(time, splitChar):
        '''
        Converts a time in the format xx(splitChar)xx(splitChar)xx into seconds\n
        Time - Your Time\n
        Splitchar - The char that splits hours from minutes and seconds, e.g xx:xx:xx\n
        Returns an integer
        '''

        time = time.split(splitChar)

        hours = int(time[0])
        minutes = int(time[1])
        seconds = int(time[2])

        hoursInSeconds = hours*3600
        minutesInSeconds = minutes*60

        timeInSeconds = hoursInSeconds + minutesInSeconds+ seconds

        return timeInSeconds
    
    def is_time_in_range(start_time, end_time, time_to_check):
        '''
        Checks if the given time is withing the range of the first 2 parameters.\n
        start_time - The start time
        end_time - The end time
        time_to_check - The time that should be checked for if it's between
        Return a boolean
        '''
        # Convert input time to total seconds
        hours = time_to_check[0]
        minutes = time_to_check[1]
        seconds = time_to_check[2]
        
        input_seconds = hours * 3600 + minutes * 60 + seconds

        # Convert start and end times to total seconds
        start_seconds = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]
        end_seconds = end_time[0] * 3600 + end_time[1] * 60 + end_time[2]

        # Check if the input time is within the range
        return start_seconds < input_seconds < end_seconds


class Fibonacci:

    def getAtN(num):
        '''
        Gets the Fibonacci Number at the Spot N - ex. at spot 6, the corresponding fibo number is 8.\n
        Num - The Index you want the Value of\n
        Returns an integer
        '''

        zahl = 0
        zahl2 = 1


        if num == 0:
            return 0

        if num == 1:
            return 1

        for i in range(1, num):
            comb = zahl + zahl2
            zahl = zahl2
            zahl2 = comb

        return zahl2
    
class Tuples:
    def getTuplesFromArray(data_to_read, start, end, amount):
        '''
        Gets each line and turns csv's into tuples
        data_to_read - The data to read
        start - The starting point of the array to read
        end - The ending point of the array to read
        amount - The amount of values that are in one line
        Returns an array
        '''
        output_array = []
        for x in range(start, end):
            line = data_to_read[x]
            line = line.split(",")
            if len(line) < amount:
                print("getTupleFromArray() encountered an error - There aren't enough given values in the line to match the given parameter. None will be returned.")
                return None
            list_line_data = []
            for x in range(amount):
                current = line[x]
                list_line_data.append(current)
            output_array.append(tuple(list_line_data))
            
        return output_array