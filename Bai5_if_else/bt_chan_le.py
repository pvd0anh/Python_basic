#!/usr/bin/python
# Chuong trinh kiem tra so chan le

def KiemTraChanLe(number):
    number = number % 2
    if number == 1:
        return "So le"
    elif number == 0:
        return "So chan"


def main():
    number = int(input("Nhap so int: "))
    print(KiemTraChanLe(number))

if __name__ == "__main__":
    main()
