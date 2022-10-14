from operator import truediv


class FizzBuzz:
    """
    A class that replaces numbers that are divisible by 3 with the word "Fizz", the ones that are divisible by 5 with "Buzz", and the ones that are divisible by both with "FizzBuzz".

    ...

    Attributes
    ----------
    item_list : list
        list of integers provided by user
    result_set : list
        list of strings returned back to user

    Methods
    -------
    Create_ResultSet(input_list)
        Generates the list of strings based on an input list of integers
    Print(result_set)
        Prints out result to users
    """
    
    #Generates the list of strings based on an input list of integers
    @classmethod
    def Create_ResultSet(cls, input_list):
        # Setup temp resultset
        result = []

        #Initialize iterator
        iterator = iter(input_list)
        #Will help us exit the while loop
        completed_iterating = False

        #Obtain value
        value = next(iterator)

        #Now iterate through item_list
        while not completed_iterating:
            try:
                # Divisible by 3 and 5
                if FizzBuzz._evenly_divisible_by_3_5(value) == True:
                    result.append('fizzbuzz')
                # Divisible by 3
                elif FizzBuzz._evenly_divisible_by_3(value) == True:
                    result.append('fizz')
                # Divisible by 5
                elif FizzBuzz._evenly_divisible_by_5(value) == True:
                    result.append('buzz')
                # If input doesn't meet any known use case, simply append the input back into the list
                else:
                    result.append(value)
                
                #Proceed to next in iteration
                value = next(iterator)

            #Handle iterating beyond end of list and gracefully exiting while loop    
            except StopIteration:
                completed_iterating = True

        #Return the result
        return result

    #Print out results to user
    @classmethod
    def Print(cls, result_set):
        
        #Initialize iterator
        iterator = iter(result_set)
        
        #Will help us exit the while loop
        completed_iterating = False

        #Obtain value
        value = next(iterator)

        #Now iterate through item_list
        while not completed_iterating:
            try:
                print(value, ",")
                
                #Proceed to next in iteration
                value = next(iterator)

            #Handle iterating beyond end of list and gracefully exiting while loop    
            except StopIteration:
                completed_iterating = True

    # Init
    def __init__(self, input_list=None):
        # Handles empty input_list
        if input_list == None:
            self._item_list = []
        else:
            self._item_list = input_list
        
        self.result_set = []
        
        # Generate resultset
        self.result_set = self.Create_ResultSet(self.item_list)
        
        # Print out result set to user
        self.Print(self.result_set)

     # Getter property decorator for item_list
    @property
    def item_list(self):
        return self._item_list

    # Setter property decorator for item_list
    @item_list.setter
    def item_list(self, value):
        self._item_list = value

    # Getter property decorator for result_set
    @property
    def result_set(self):
        return self._result_set

    # Setter property decorator for result_set
    @result_set.setter
    def result_set(self, value):
        self._result_set = value

    # Determines if integer is evenly divisible by 3
    @staticmethod
    def _evenly_divisible_by_3(num):
        if num % 3 == 0:
            return True
        else:
            return False

    # Determines if integer is evenly divisible by 5
    @staticmethod
    def _evenly_divisible_by_5(num):
        if num % 5 == 0:
            return True
        else:
            return False
    
    # Determines if integer is evenly divisible by 3 and 5
    @staticmethod
    def _evenly_divisible_by_3_5(num):
        if FizzBuzz._evenly_divisible_by_3(num) == True and FizzBuzz._evenly_divisible_by_5(num) == True:
            return True
        else:
            return False

 # Driver code
if __name__=='__main__':
    #Input data
    data = [45, 22, 14, 65, 97, 72]
    #Instantiate object
    f = FizzBuzz(data)