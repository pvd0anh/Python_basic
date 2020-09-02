'''
Đề bài: viết chương trình hỗ trợ học sinh:
1. Hiển thị lịch học hôm nay,
2. Nhập danh sách bài tập về nhà,
3. Tóm tắt lý thuyết nội dung ôn tập,
4. Danh sách bài tập để luyện giải bài tập,
5. Chương trình giải phương trình: y = ax + b
Viết chương trình dạng menu cho phép sử dụng các tính năng trên
'''

def Home():
    while True:
        line = '+ {:-<6} + {:-^29}+'.format('', '')
        row_menu = '| {:^37} |'.format('WELCOME TO KASE SCHOOL')
        row_tile_menu = '| {:^6} | {:^29}|'.format('Choose', 'Nội dung')
        help_tile_menu = '| {:^5}  | {:<29}|'.format('-1', 'Hướng dẫn sử dụng')
        row_1 = '| {:^6} | {:<29}|'.format('1', 'Xem thời khóa biểu')
        row_2 = '| {:^6} | {:<29}|'.format('2', 'Danh sách bài tập về nhà')
        row_3 = '| {:^6} | {:<29}|'.format('3', 'Ôn tập lý thuyết')
        row_4 = '| {:^6} | {:<29}|'.format('4', 'Luyện giải bài tập')
        row_5 = '| {:^6} | {:<29}|'.format('5', 'Giải phương trình tìm x')
        row_6 = '| {:^6} | {:<29}|'.format('0', 'Exit')
        print('\n', line, '\n', row_menu, '\n', line, '\n', row_tile_menu, '\n', line, '\n', help_tile_menu,
                '\n', row_1, '\n', row_2, '\n', row_3, '\n', row_4, '\n', row_5,'\n', row_6, '\n', line)


        ch = int(input("->"))

        if ch == -1:
            print("Hướng dẫn sử dụng phần mềm")
            help_text = """Nhập giá trị ở cột Choose và nhấn Enter để sử dụng các chức năng: \n
            \t 1: Xem thời khóa biểu trong tuần, nội dung này đã được nhập từ trước đó,
            \t 2: Hiển thị danh sách bài tập bạn cần phải hoàn thành trước khi đến lớp,
            \t 3: Nội dung lý thuyết cần nắm,
            \t 4: Danh sách bài tập được giáo viên giao về nhà,
            \t 5: Chương trình hỗ trợ giải toán tìm x,
            \t 0: Để thoát khỏi chương trình.
            """
            print(help_text)
            print('Nhấn Enter để tiếp tục chương trình:')
            input()

        elif ch == 1:
            print(" ")
            schedule()

        elif ch == 2:
            print(" ")
            home_work()

        elif ch == 3:
            print(" ")
            theory()

        elif ch == 4:
            print(" ")
            exercise()

        elif ch == 5:
            print(" ")
            find_x()

        elif ch == 0:
            print("Tạm biệt và hẹn gặp lại bạn")
            exit()
        
        else:
            print("Nhập giá trị có trong dánh sách lựa chọn nhé bạn <3")

def schedule():
    #TODO: Thiết kế bảng chứa thời khóa biểu trong tuần
    pass

def home_work():
    #TODO: Nhâp danh sách bài tập cần làm
    pass

def theory():
    #TODO: Thiết kế bảng chứa danh sách kiến thức cần ôn tập
    pass

def exercise():
    #TODO: Liệt kê danh sách bài tập cần làm
    pass

def find_x():
    #TODO: viết chương trình giải phương trình tìm x
    pass

if __name__ == "__main__":
    Home()

import turtle
turtle.forward(50)
turtle.left(144)
turtle.forward(50)
turtle.left(144)
turtle.forward(50)
turtle.left(144)
turtle.forward(50)
turtle.left(144)
turtle.forward(50)
turtle.left(144)
