# String are immutable

names = "john,anmol,jim,abhi"
print("names:", names)
upper_case_name = names.upper()

print("names now", names, id(names))
print("Upper case :", upper_case_name, id(upper_case_name))

s1 = names.capitalize()
s2 = names.title()
s3 = names.swapcase()
s4 = names.replace('j', 'kO')

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s4:", s4)

# password = input("Enter your password:")
#rstrip(),lstrip()
# print("password", password.strip())
#
# data = '000000000001230000000'
# print("data", data.strip('0'))
#
# numbers = 4.520000
# numbers = float(str(numbers).strip('0'))
# print(numbers, type(numbers))

message = "no internet coonectivity"
print(message)
print(message.center(50))
print(message.ljust(50))
print(message.rjust(50))

msg = "hlo there"
print(msg.find('ere'))
print(msg.find('there'))
print(msg.index('ere'))
print(msg.rindex('ere'))

data="1234"
print(data.zfill(5))

for ch in msg:
    print(ch, end="\n")

idx1 = msg.index('ere')
idx2 = idx1 + len('there')
print("idx 1 :", idx1)
print("idx 2 :", idx2)
