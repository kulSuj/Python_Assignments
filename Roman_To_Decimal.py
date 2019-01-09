# Program to covert Roman Number to a Decimal Number
# Roman Numbers are represented by seven different letters: I,V,X,L,C,D,M, which represents 1,5,10,50,100,500 and 1000 respectively.

dict_roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
roman_number = raw_input("Enter the number in Roman format:")


if (roman_number == ""):
    print "Empty string"
    exit (0)


#Test to check if any invalid literal present in user input.
for literal in roman_number:
    if literal not in dict_roman:
        print "Non roman literal '" + literal + "' entered by user: " + roman_number




reverse_roman = roman_number[::-1]
len_roman = len(reverse_roman)

fwd_ptr = 0     
backward_ptr = 0
decimal_number = 0

#print len_roman

while len_roman > 0:

    #print reverse_roman[backward_ptr], reverse_roman[fwd_ptr]

    #print dict_roman[reverse_roman[fwd_ptr]] , dict_roman[reverse_roman[backward_ptr]]

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
