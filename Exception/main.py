from exception import AuthenticationError,AuthorizationError,AppError,InsufficientBlanceError



# raise AuthenticationError("Invalid token")


# try:

# except AuthorizationError :

# except AppError:


# n=int(input('Enter a number: '))

# try:
#     for i in range(n):
#         print(f'number is divible {i}' and {n%i})
# except Exception as e:
#     print(f"arithmetic error: {e}")



def withdraw(balance,amount):
    if amount > balance:
        raise ValueError("Not enough money ")
    


def withdraw(balance,amount):
    if amount > balance:
        raise InsufficientBlanceError("Insufficient balance ")
    

try:
    withdraw(100,200)
except InsufficientBlanceError:
    print('Notify user: low balance')


