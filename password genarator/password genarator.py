from random import choices
from string import ascii_letters, punctuation, digits

temp = ascii_letters + punctuation + digits
c = choices(temp, k=20)
res = ""
for i in c:
    res = res + i

print(res)