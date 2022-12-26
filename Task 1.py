#Вычислить число c заданной точностью d

import math
value = 10/3
d = 0.00001
print(f'Число {value} с заданной точностью {d} равно {round(value, int(math.log(d, 10))*-1)}')

