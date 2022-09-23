"""
Given an integer num as input, find ones' complement of ``num``. The ones' complement of a binary number is the value obtained by inverting all the bits in the binary representation of the number (swapping 0s and 1s). The value ``num`` could be between 0 and 10000. Your code should handle the following scenarios thoughtfully: 

Out-of-range input values.
Invalid input values.
To complete this project, you CAN NOT use: 

Any Python method or function. 
Any Python loop structure.
Any list, array,set, or dictionary object. 
You can only use the following components: 

Conditional statements if, if-else and if-elif-else
Simple variable assignment
Binary operators like and, or and not. 
Sample input: 

Enter a binary value between 0 and 10000: 101
The ones' complement of 101 is 10.
"""
class Project():
    def __init__(self):
        self.value = str()
        self.length = 0
        self.solution = 0
        self.maxIndex = 0
        self.indexx = 0

    def composite(self,givenBit):
        if givenBit == 0:
            return 1
        else:
            return 0
    
    def binaryToDecimalConverter(self, givenBitValue):
        try:
            #print(givenBitValue[self.length])
            self.value = self.value + str(self.composite(int(givenBitValue[self.length])))
            self.length+=1
            self.binaryToDecimalConverter(givenBitValue)
        except:
            #we have reached the end of binary string so now we go back.
            
            self.maxIndex = self.length
            self.length = self.length - 1
            return


    def compute(self, binaryValue):
        if self.length == -1:
            return 
        else:
            #print(self.indexx,self.length)
            self.solution= self.solution + (int(self.value[self.indexx]) * (2**self.length))
            #print(self.value[self.indexx]+"*"+str(2**self.length))
            self.length = self.length - 1
            self.indexx=self.indexx+1
            if(self.maxIndex< self.indexx):
                return
            self.compute(binaryValue)

    #Driver Code
    def processor(self, givenBinaryCode):
        if int(givenBinaryCode)<0 or int(givenBinaryCode)>=10000:
            print("Invalid input!")
            return

        
        self.binaryToDecimalConverter(givenBinaryCode)
        #values of lenght, index and value are generated.

        print("you have entered: "+givenBinaryCode)
        print("One's compliement is: "+self.value)
        self.compute(self.value)
        print("Decimal equivalent number: "+str(self.solution))

    def converter(self,decimalValue):
       # print(decimalValue)
        #check if we have reached the end.
        if(decimalValue==0):
            self.value = self.value[::-1]
            return
        else:
            self.value=self.value+str(self.composite(decimalValue%2))
            
            
            decimalValue = decimalValue // 2
            self.converter(decimalValue)


obj = Project()
print("Please enter a binary number between 0  and 10000: ")
rawInputValue = input()
obj.processor(rawInputValue)
