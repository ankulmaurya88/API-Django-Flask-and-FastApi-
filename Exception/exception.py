class AppError(Exception):
    pass

class AuthenticationError(AppError):
    pass

class AuthorizationError(AppError):
    pass

class PaymentError(AppError):
    pass

class AuthError(AppError):
    pass


class InsufficientBlanceError(Exception):
    def __init__(self,balance , requested):
        self.balance=balance
        self.requested = requested
        super().__init__(
            f'Balance {balance}, requested {requested}'
        )



class APIError(Exception):
    def __init__(self,message,status):
        self.status=status
        super().__init__(message)



'''
except APIError as e :
    return {"error" : str(e)}.,e.status
'''


try:

except Exception:
    pass


# MENTAL MODEL (Remember this )

# function raise -> Controller map -> Users see


'''

import logging 

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(name)s | %(message)s )

logger=logging.getLogger("payment-service")


'''


class AppError(Exception):
    pass


