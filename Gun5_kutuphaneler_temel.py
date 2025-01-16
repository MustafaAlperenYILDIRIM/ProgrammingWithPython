import math
print(math.pi)  
print(math.sqrt(16))
print(math.factorial(5))
print(math.pow(2,3))
print(math.log(100,10))


import random
print(random.randint(1, 10))
print(random.random())#0-1 arasında rastgele sayı üretir
print(random.choice([1,2,3,4,5]))
print(random.sample([1,2,3,4,5], 3))
print(random.uniform(1, 10))



from datetime import datetime
print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)
print(datetime.now().microsecond)
print(datetime.now().isoformat())
print(datetime.now().ctime())


import os
print(os.getcwd())
print(os.listdir())
print(os.name)


import sys
print(sys.version)
print(sys.platform)


