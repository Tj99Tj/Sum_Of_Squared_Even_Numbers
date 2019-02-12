import random
app=True
while True:
    def program():
        print("This program computes the sum of the squared even numbers between 1 and a number of your choice (N)")
        N = int(input("\n What number would you like to compute up to? \n N ="))

        sum = 0
        for N in range(2, (N+1), 2):
            sum += N**2
        print("\nThe sum of the squared even numbers between 1 and your input N is:", sum)
    program()

    again = input("\n Would you like to try it again with a different number? (Type Y for yes and N for no)\n")
    if again == "Y":
        continue
    if again == "N":
        app=False
        print("Ok, Goodbye!!")
        break

    
