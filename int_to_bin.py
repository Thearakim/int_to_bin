def int_to_binary(a, b): #function take two paramaters
    sum = a + b    #sum two number take from print
    temBi = ""     #declare string "" for adding the code below
    while sum != 0:  #using loop to make sure a and b is greater than 0 because equal 0 error 
        temBi = str(sum % 2) + temBi  #first it calculated sum % 2 take remainder to temBi 
        sum  //=  2  #divided sum by 2 example 4 divided by 2 = 2 so loop again and temp add again 
    return temBi #return binary value to our function int_to_binary


print(int_to_binary(12, 3))  #put number a =12 and b =3 and print binary value
