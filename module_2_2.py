first = int(input("Введите первое целое число: "))
# print (first)
second = int(input("Введите первое целое число: "))
# print (second)
third = int(input("Введите первое целое число: "))
# print (third)
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)