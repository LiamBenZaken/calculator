#starting program the calculate
def add(nums):
    print(nums[0] + nums[1])


def sub(nums):
    print(nums[0] - nums[1])


def mull(nums):
    print(nums[0] * nums[1])


def div(nums):
    if nums[1] == 0:
        print("ERROR - cant divide by zero!")
        return
    print(nums[0] / nums[1])


def myPow(nums):
    try:
        print(nums[0] ** nums[1])
    except:
        print("Oops! Result too large...")


def isValidInput():
    while True:
        try:
            n1 = float(input("please enter the first number:"))
            n2 = float(input("please enter the second number:"))
            nums = (n1, n2)
            return nums
        except ValueError:
            print("Oops! That was no valid number.  Try again...")


print("welcome to the calculator!")
print("enter the first char of the method that you want to use:")

while True:
    print("a - for add")
    print("s - for sub")
    print("m - for mul")
    print("d - for div")
    print("p - for pow")
    print("e - exit")
    char = input()

    match char:
        case 'a':
            add(isValidInput())
        case 's':
            sub(isValidInput())
        case 'm':
            mull(isValidInput())
        case 'd':
            div(isValidInput())
        case 'p':
            myPow(isValidInput())
        case 'e':
            print("thanks for used the calculator :)")
            break
        case default:
            print("there is no char like this in the menu...")

#finished the code :)