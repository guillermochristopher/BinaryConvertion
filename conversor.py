##inspection version 2.0
print("The program does a conversion of two decimal numbers (integers), does the addition or substraction,(if there are negative numbers) then it represents")
print(" the initial numbers and the result in binary format using 8 bits\n")
print("Due to the binary format only use 8 bits the range of numbers that it can represent is 256, that holds 128 numbers dedicate to integers with sign")
print("and 128 including the 0 for positive numbers.\n")
print("-------------------------------------------------------------------------------------------------------------------------------------------------")
print("")

##function in charge of inspecting the inputs:
def inspect_inputs(a,b):
    

    if((a<=127 and a>=-128) and (b<=127 and b>=-128)):
        validation=True
    else:
        validation=False
   
   
    return validation

##function in charge of convert from decimal to binary
def conversion(a, b):
    h=[]
    y=[]
    o= []
    r= []
    for i in range(8):
        c=int(a%2)   ##dividing the first number and taking up its rest.
        j= int(b%2)   ##idem but to the second number
        a=a/2            ##dividng the input by 2 so we can keep doing the conversion
        b=b/2 
        o.append(c)     ##add c to the empty list  o
        r.append(j)       ##add j to the empty list r
##Now, we got two full list of the numbers converted in binary, the problem is that the order of that list is not
##useful for our operations because its order is inverted

##Inverting the order:
    h=o[::-1]       
    y=r[::-1]
    return h, y

##function in charge of make the calculus
def operation(q,w):
    ##defining variables
    carry=0
    
    lis=[]
    lis2=[]
    carrylist=[0,0,0,0,0,0,0,0]
    Sum=[]
    orderSum=[]

##takes the carry and save it in a carrylist 
    for d in range(7, -1, -1):
       
        if(carrylist[d]==0):
            result=(q[d] and w[d])
            if(result==1):
                carrylist[d-1]=1
               
                carry=1
            elif(result==0):
                result=(q[d] or w[d])
                if(result==1):
                    
                    carrylist[d-1]=0
                    carry=0
                elif(result==0):
                        
                        carrylist[d-1]=0
                        carry=0
        elif(carrylist[d]==1):
            result=(q[d] and w[d])
            if(result==1):
                carrylist[d-1]=1
                carry=0
                
            elif(result==0):
                result=(q[d] or w[d])
                if(result==1):
                    
                    carrylist[d-1]=1
                    carry=0
                elif(result==0):
                    
                    carrylist[d-1]=0
                    carry=0

##make the xor comparison
    for i in range(7,-1,-1):
        lis.append(q[i] ^ w[i])

    orderlis1=lis[::-1] ##order the initial lis and save it

 ##make the and comparison
    for x in range(7,-1,-1):
        lis2.append(q[i] & w[i])

    orderlis2=lis2[::-1]

##doing the xor comparison between the carrylist and the orderlis1 give us the result of the addition!
    for f in range (7,-1,-1):
        Sum.append(carrylist[f] ^ orderlis1[f])
    orderSum=Sum[::-1]
    return carry, orderSum

def main():
     
    
    print("What operation do you want to do?")
    print("Opcion [A]: Convert from decimal to binary")
    print("Option [B]: Convert from binary to decimal")
    Option=str(input())
    
    if(Option=="A"):
        moreConversion="yes"
        while(moreConversion[0]=="y"): ##this way the program will only take the first letter of the user's response,
                                                                        ##this allows to type things like "yeah", "yep", "y", "yes"
            a=int(input("First number to convert: "))
            b=int(input("Second number to convert: "))
            Carry=int
            q=[]
            w=[]
            SumList=[]

            ##Inspect input values If it is valid, you can continue, if not, the program promps the user enter a valid data.
            if(inspect_inputs(a,b)==True):
                
                ##make the conversion to binary
                q,w=conversion(a,b)

                #display the conversion
                print("\nThe conversion in binary format for the first one is: \n",*q)
                print("")
                print("The conversion in binary format for the second one is:\n",*w)
                print("")
                
                ##make the operation between two numbers in binary format:
                Carry, SumList=operation(q,w)

                ##display the result
                print("The result of calculate the addition, or the substraction, is:\n")
                print(">> In Decimal format:\n",a+b,"\n")

            ##To check if there is overload
                if((a+b < -128) or (a+b > 127)):
                    print(">> OVERLOAD! << Result out of range to") 
                    print("represent in 8 bits. Range=[-128 to 127]")
                    print("To make possible the representation is needed 1 bit more:\n ""[", Carry, "]", *SumList)
                else : print(">> In Binary format:\n",*SumList)
                print("")
                    
            ##ask if wanna do another operation
                moreConversion=str(input("Do you want to do another conversion?: [yes / no]\n"))

            elif (inspect_inputs(a,b)==False):
                print("\nNot valid data. Number out of range [-128, 127]")
                moreConversion=str(input("Do you want to do another conversion?: [yes / no]\n"))
        print("\nThanks for use Binary Conversion 6.0\nBye :D")   
    if(Option=="B"):
        print("OH! There is a problem with this option...")
        print("The student had no more time to do this feature, but he will finish it, promise :D")

main()

