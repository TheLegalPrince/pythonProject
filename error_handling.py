import random as r
import string
try:
    raise NameError
except:
    print('Re-raising the exception')
    raise
finally:
    print(r.randint(1, 2))
    print(r.randrange(1, 2),end='\n\n')
    for i in (string.digits[1:8]):
        print(i)