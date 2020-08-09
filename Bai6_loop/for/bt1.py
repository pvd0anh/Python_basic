# Tìm các số chia hết cho 7 nhưng không phải bội số của 5,
# nằm trong đoạn 10 và 200

for i in range(10, 201):
    if (i % 7 == 0) and (i % 5 != 0):
        print(i)
