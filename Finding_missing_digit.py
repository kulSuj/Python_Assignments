#Identify the missing digits in the expression.


def split_expression(str_expression):

    #Check for "=" sign and extract the answer value from expression.
    index_pos = str_expression.find('=')

    if (index_pos != -1):
        answer = str_expression[(index_pos+1): :]
        str_expression = str_expression[:(index_pos)]
    else:
        answer = 0


    #Check which operator is present in expression and retrieve the index position of operator in the expression.
    if(str_expression.find('*')>=0):
        
        index_pos = str_expression.find('*')
        operator = '*'
        
    elif(str_expression.find('/')>=0):
        index_pos = str_expression.find('/')
        operator = '/'

    elif(str_expression.find('+')>=0):
        index_pos = str_expression.find('+')
        operator = '+'
        
    elif(str_expression.find('-')>=0):
        index_pos = str_expression.find('-')
        operator = '-'
        
        
    else:
        index_pos = -1
        operator = 0


    #If operator index position found, fetch the 2 operands and store it in digit1, digit2 respectively.
    if(index_pos >= 0):
       digit1 = str_expression[:index_pos]
       digit2 = str_expression[index_pos + 1::]



    return (digit1, digit2, answer, operator)



#---------------------------------------------------------------------------



def buildDigits(digit1,digit2,answer, intValue):


    #For digit1, digit2, answer, replace every occurence of '?' with intValue
    digit1 = digit1.replace('?',str(intValue))

    digit2 = digit2.replace('?',str(intValue))

    answer = answer.replace('?', str(intValue))


    #return the integer values of digit1, digit2, answer
    return (int(digit1), int(digit2), int(answer))



#---------------------------------------------------------------------------



def calculateValue(digit1, digit2, answer, operator):

    #Check all possible values from 0-9 by substituting '?' and evaluating expression.
    found_value=0
    for intValue in range(10):

        #Call buildDigits function to substitute every '?' with intValue and accept integer digits as return value.
        (int_digit1, int_digit2, int_answer) = buildDigits(digit1,digit2,answer, intValue)


        #Perform operation according to the operator value
        if (operator == '+'):
            actual_answer = int_digit1 + int_digit2

        elif (operator == '-'):
            actual_answer = int_digit1 - int_digit2

        elif (operator == '*'):
            actual_answer = int_digit1 * int_digit2

        elif (operator == '/'):
            actual_answer = int_digit1 / int_digit2

        
        #Check if the actual calculated answer matches the answer provided in expression, if YES, you have found the missing digit.
        if (int_answer == actual_answer):
            print "The missing digit is : ", intValue
            print "The expression is : ", int_digit1, operator, int_digit2, "=", int_answer

            found_value=1
            
            break



    if(found_value == 0): 
        print "Incorrect expression"

     



        
#---------------------------------------------------------------------------------------
#                                   MAIN
#---------------------------------------------------------------------------------------



str_expression = raw_input("Enter the expression : ")


#Check if user has input empty expression
if (str_expression == ""):
    print "No input from user."
    exit (0)

#Call to split_expression function to split the expression and fetch operator, operands, result from the expression provided by user.
(digit1, digit2, answer, operator) = split_expression(str_expression)

#Call to calculateValue to find missing digit and calculate the value of expression
calculateValue(digit1, digit2, answer, operator)



