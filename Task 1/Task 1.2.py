lst = ['0001', '0011', '0101', '1011']

new_lst = [int(binary, 2) for binary in lst]
print(new_lst)

for i in lst:
    print(i)