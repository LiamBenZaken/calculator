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
