family = ["Muliadi", "Linda", "Hansen", "Jonathan"]

def main():
    i = int(input("How many family members do you want to see? "))
    inputcheck(i) # Check the input if more than the length of family[] array 
    for i in range(i):
        print(family[i])

def inputcheck(i):
    if i >= (len(family))+1: # Loop if answer is wrong
        print("Please put a number between 1 to",len(family))
        main()
    else:
        return # Break loop if answer within specs

main()