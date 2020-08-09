#!/usr/bin/python
# Nhap nam sinh tinh tuoi nguoi .

# Su dung module time
import time
year = time.localtime()


def TinhTuoi(YearInput, NameInput):
    Age = year[0] - YearInput
    if Age == 0:
        Age = Age + 1
        print('Chao ban ' + NameInput +
            ', ban', Age, 'tuoi phai khong ?')
    elif Age < 0:
        print('Chao ban ' + NameInput + ', ban co do tuoi khong phu hop !')
    else:
        print('Chao ban ' + NameInput + ', ban', Age, 'tuoi phai khong ?')


def main():
    NameInput = input("Nhap ten cua ban: ")
    YearInput = int(input("Nhap nam sinh cua ban: "))
    TinhTuoi(YearInput, NameInput)


if __name__ == "__main__":
    main()
