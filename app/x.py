import re
N = 50000

for i in range(-N,N):
    if re.fullmatch("(0*(1(01*0)*1)*0*)*", bin(i)[2:]) and i % 3 != 0:
        print(i)

print('Done')