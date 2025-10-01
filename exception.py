# Exception = events detected during execution that interrupt the flow of a programme

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    
except ZeroDivisionError as e:
    print(e)
    print('You can not divide by zero5')
except ValueError as e:
    print(e)
    print('Enter only numbers pls')
except Exception as e:
    print(e)
    print('Something went wrong:')
else:
    print(result)
finally:
    print("This will always execute")