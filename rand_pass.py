import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "01234567890"
symbol = "[{(<>)}],;:.!?/\|@#$%^&*_+-="

all = lower + upper + number + symbol
lenght = 10
password = "".join(random.sample(all, lenght))
print ('Senha gerada:',password)
