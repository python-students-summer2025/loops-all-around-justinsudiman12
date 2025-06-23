def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num >= 1:
                return num
            else:
                print("Please enter a number greater than or equal to 1.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def sing(start):
    bottles = start
    keep_singing = True
    while keep_singing:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles - 1} bottle{'s' if bottles - 1 > 1 else ''} of beer on the wall.")
        elif bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            keep_singing = False 
        print() 
        bottles -= 1
        