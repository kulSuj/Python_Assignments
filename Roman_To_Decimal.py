# Program to convert Roman Number to a Decimal Number
# Roman Numbers are represented by seven different letters: I,V,X,L,C,D,M, which represents 1,5,10,50,100,500 and 1000 respectively.

#Map for roman literals.
dict_roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}



def countSequence(roman_number):
    #Test if a roman literal is repeated more than 3 times in a sequence.
    fwd_ptr = 1
    back_ptr = 0
    len_roman = len(roman_number)

    
    while len_roman > 1 :
   
        if (roman_number[fwd_ptr] == roman_number[back_ptr]) :


            #Roman literals "V", "L", "D" are not allowed to repeat more than once.
            if ((roman_number[back_ptr] == "V") or (roman_number[back_ptr] == "L") or (roman_number[back_ptr] == "D")):
                print "Roman literal '" + roman_number[back_ptr] + "' cannot be present more than once."
                return 0



            #Loop to check if any roman literal is repeated more than 3 times, the roman number cannot have a literal more than three times.
            counter = 2

            range_cnt = len_roman - 2
            
            for i in range(range_cnt):

                fwd_ptr = fwd_ptr + 1

                back_ptr = back_ptr + 1
                len_roman = len_roman - 1

                
                if (len_roman == 0): #End of Roman Number string
                    break

   
                if (roman_number[fwd_ptr] == roman_number[back_ptr]):
                    counter = counter + 1

                else:
                    break

   
            if (counter >= 4):
                print "Roman literal '" + roman_number[back_ptr] + "' cannot be repeated more than 3 times in a sequence."
                return 0

            
        fwd_ptr = fwd_ptr + 1
        back_ptr = back_ptr + 1
        len_roman = len_roman - 1

        

    return 1
    


def testForPrecedence(roman_number):

    #Precedence rule :
    #"I" can precede "V" and "X"
    #"X" can precede "L" and "C"
    #"C" can precede "D" and "M"
    
    fwd_ptr = 1
    back_ptr = 0
    len_roman = len(roman_number)


    illegal_literal_flag = 0

    while back_ptr <= (len_roman - 2):

        counter = len_roman - back_ptr

        while counter > 1 :
           
            if (roman_number[back_ptr] == "I"):
                if ((roman_number[fwd_ptr] == "L") or (roman_number[fwd_ptr] == "C") or (roman_number[fwd_ptr] == "D") or (roman_number[fwd_ptr] == "M")):
                    illegal_literal_flag = 1
                    break
        
            if ((roman_number[back_ptr]) == "V" and (roman_number[fwd_ptr] != "I")):
                illegal_literal_flag = 1
                break
            
            if (roman_number[back_ptr] == "X"):
                if ((roman_number[fwd_ptr] == "D") or (roman_number[fwd_ptr] == "M")):
                    illegal_literal_flag = 1
                    break

            if ((roman_number[back_ptr]) == "L" and ((roman_number[fwd_ptr] == "C") or (roman_number[fwd_ptr] == "D") or (roman_number[fwd_ptr] == "M"))):
                illegal_literal_flag = 1
                break

            if ((roman_number[back_ptr]) == "D" and (roman_number[fwd_ptr] == "M")):
                illegal_literal_flag = 1
                break


            fwd_ptr = fwd_ptr + 1
            counter = counter - 1
            illegal_literal_flag = 0


                        
        if (illegal_literal_flag != 0):
                break
            
        back_ptr = back_ptr + 1
        fwd_ptr = back_ptr + 1

       
    if (illegal_literal_flag == 1):
        print roman_number[back_ptr] + " cannot preceed " + roman_number[fwd_ptr]
        return 0

    else:
        return 1
          


def testForIllegalSequence(roman_number):

    illegal_sequence = ('IVI', 'IXI', 'IXV', 'IXX', 'XLX', 'XCX', 'XCL', 'CDC', 'CMC', 'CMD')


    for seq in illegal_sequence :
        if (roman_number.find(seq) == -1):
            print "Invalid roman number : " + roman_number
            return 0

    return 1
        
            
def isValidRomanNumber(roman_number):

    #Test for empty roman string.
    if (roman_number == ""):
        print "Empty string"
        return 0


    #Test to check if any invalid literal present in user input.
    for literal in roman_number:
        if literal not in dict_roman:
            print "Non roman literal '" + literal + "' entered by user: " + roman_number
            return 0


    #Test to check if a single Roman literal is not repeated more than 3 times.
    if (countSequence(roman_number) == 0):
        return 0
       

    #Test for precedence of roman literal.
    if(testForPrecedence(roman_number)== 0):
        return 0


    if(testForIllegalSequence(roman_number)==0):
        return 0

    
    return 1





#-----------------------------------------------
#               Main program
#-----------------------------------------------

roman_number = raw_input("Enter the number in Roman format:")


if (not isValidRomanNumber(roman_number)):
    exit (0)


reverse_roman = roman_number[::-1]
len_roman = len(reverse_roman)

fwd_ptr = 0     
backward_ptr = 0
decimal_number = 0


while len_roman > 0:

    if (fwd_ptr == 0 ):
        decimal_number = dict_roman[reverse_roman[fwd_ptr]]
                
    elif (dict_roman[reverse_roman[fwd_ptr]] < dict_roman[reverse_roman[backward_ptr]]):
        decimal_number = decimal_number - dict_roman[reverse_roman[fwd_ptr]]

    else:
        decimal_number = decimal_number + dict_roman[reverse_roman[fwd_ptr]]


    if (fwd_ptr == 0 ):
        fwd_ptr = fwd_ptr + 1
    else :
        fwd_ptr = fwd_ptr + 1
        backward_ptr = backward_ptr + 1
        
    len_roman = len_roman - 1

print ""
print "The decimal form of roman number '" + roman_number + "' is: ", decimal_number




