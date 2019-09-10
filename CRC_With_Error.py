# This program uses standard CRC-32 :
# 100000100110000010001110110110111     <------ Binary
# 0x104c11db7                           <------ Hexadecimal
# And the polynomial function is :
# x32 + x26 + x23 + x22 + x16 + x12 + x11 + x10 + x8 + x7 + x5 + x4 + x2 + x1 + 1
#-----------------------------------------------------------------------------
import random
import time

randomString = ''   #make a 32 bit random string for Data
for i in range (0,32):
    randomInt = random.randint(0, 1)
    randomString = '%s%s'%(randomString,str(randomInt))

Data1_str = randomString
print('32 bit Data = '+ Data1_str)

Data_kzero_str = Data1_str + '00000000000000000000000000000000' #Extend the Data bits with k zeros
print('32 bit Data with 32 zeros = ' + Data_kzero_str)

crc32_bin = 0b100000100110000010001110110110111
crc32_str = '100000100110000010001110110110111'
crc32_int = int(crc32_str,2)
print('CRC32 = '+ crc32_str)

while Data_kzero_str[0] != '1':     #calculate the Checkbit
    Data_kzero_str = Data_kzero_str[1:]
while len(Data_kzero_str) > 32:
    Data_kzero_cal = Data_kzero_str[:33]
    Data_kzero_cal_int = int(Data_kzero_cal,2)
    r = Data_kzero_cal_int ^ crc32_int
    r_bin = bin(r)
    r_str = str(r_bin)
    r_str = r_str[2:]
    Data_kzero_str = r_str + Data_kzero_str[33:]
    #print(Data_kzero_str)

print('Reminder = ' + Data_kzero_str)
while len(Data_kzero_str) != 32:
    Data_kzero_str = '0' + Data_kzero_str
print('Checkbit = ' + Data_kzero_str)

Codeword = Data1_str + Data_kzero_str       #make the Codeword
print('Codeword = ' + Codeword)


print('')       #send to receiver
for i in range (0,5):
    print('#################################### Sending ###############################################')
    time.sleep(0.7)
print("#################################### Recieved ##############################################")

randomInt = random.randint(0, 1)    #50% error injection
if randomInt == 0 :
    Codeword = Codeword + '1'

print('Data = '+ Codeword)

while Codeword[0] != '1':       #divide and check for zero
    Codeword = Codeword[1:]
while len(Codeword) > 32:
    Codeword_cal = Codeword[:33]
    Codeword_cal_int = int(Codeword_cal,2)
    r = Codeword_cal_int ^ crc32_int
    r_bin = bin(r)
    r_str = str(r_bin)
    r_str = r_str[2:]
    Codeword = r_str + Codeword[33:]
print('Reminder = ' + Codeword)

if int(Codeword) == 0 :
    print('Correct , None error detected. ')
else:
    print('Mistake , Some error(s) detected. ')

input()
exit()
