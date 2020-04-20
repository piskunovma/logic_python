# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

arr_1 = [i for i in range(2, 100)]
print(arr_1)
arr_2 = [i for i in range(2, 10)]
print(arr_2)

res = 0
for itm in arr_1:
    sum = 0
    for itm2 in arr_2:
        if itm % itm2 == 0:
            sum += 1
            if sum == len(arr_2):
                res += 1
                print(itm)
print(res)