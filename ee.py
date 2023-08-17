#This program uses user input to determine whether or not a character from the character list is not used in the input

characters=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def check(strr):                                #creating the function
    for n in range(len(characters)):            #Loop to check all of the characters
         if not(characters[n] in str(strr)):    # if statement to check  if characters for list aren't present in string
            print(characters[n],end="")         # if the character isn't present, the function prints the character on a line next to eachother

strr=input("Enter any word with no spaces, no capitals, and no special characters: ")  

check(strr)                                                                                                                                     
