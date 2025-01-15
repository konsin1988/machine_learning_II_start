import datetime
import numpy as np

start = datetime.datetime.now()

# a = [1 for _ in range(100000000)]
# a = [elem + 10 for elem in a]
# a = np.ones(1000000000, int)
# a += 10



end = datetime.datetime.now()
print((end-start).seconds)

