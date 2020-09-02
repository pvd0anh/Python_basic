"""
Bài: viết chương trình quản lý sinh viên với những chức năng sau:
    1.Tạo và thêm thông tin sinh viên
    2.Hiển thị thông tin sinh viên
    3.Tìm kiếm thông tin của sinh viên
    4.Xóa sinh viên ra khỏi danh sách
    5.Cập nhật thông tin sinh viên
    6.Hàm thoát khỏi chương trình
Chương trình dạng menu cho phép sử dụng các tính năng trên.
"""


class sinhvien:
    def __init__(self, ten, mssv, toan, van):
        self.ten = ten
        self.mssv = mssv
        self.toan = toan
        self.van = van

    # hàm tạo và thêm mới sinhvien
    def create(self, ten, mssv, Toan, Van):
        ob = sinhvien(ten, mssv, Toan, Van)
        ls.append(ob)
        print("Bạn muốn thêm bao nhiêu sinh viên:")
        n = int(input())
        for i in range(n):
            ten = str(input("Tên sinh viên {}: ".format(i+1)))
            mssv = int(input("MSSV sinh viên {}: ".format(i+1)))
            Toan = int(input("Điểm môn toán sinh viên {}: ".format(i+1)))
            Van = int(input("Điểm môn văn sinh viên {}: ".format(i+1)))
            ob = sinhvien(ten, mssv, Toan, Van)
            ls.append(ob)
            print("\n")
        '''
        Vấn đề gặp phải:
            + khi nhập giá trị mssv, Toán, Văn được yêu cầu phải là số thực
            + người dùng nhập kiểu Starting
            + câu hỏi đặt ra là: làm sao để giải quyết vấn đề này?
            => sử dụng try_except trong python
            Nội dung này sẽ được tìm hiểu và ứng dụng trong khóa advance
        '''

    # Hàm hiển thị thông tin chi tiết sinh viên
    def display(self, ob):
        print("Tên sinh viên : ", ob.ten)
        print("Mã số sinh viên : ", ob.mssv)
        print("Điểm môn toán : ", ob.toan)
        print("Điểm môn văn : ", ob.van)

    # Hàm tìm kiếm thông tin sinh viên
    def search(self, mssv):
        #TODO: add chỉnh hết tất cả các trường

        for i in range(ls.__len__()):
            if(ls[i].mssv == mssv):
                return i
        print("Không sinh viên nào có mssv", mssv)
        return False

    # Hàm xóa thông tin sinh viên
    def delete(self, mssv):
        i = obj.search(mssv)
        del ls[i]

    # Hàm cập nhật thông tin
    def update(self):
        #TODO: add chỉnh hết tất cả các trường

        mssv_old = int(input("Nhập mssv cần chỉnh sửa:"))
        i = obj.search(mssv_old)
        if i:
            mssv_new = int(input("Nhập mssv mới:"))
            ls[i].mssv = mssv_new


# Tạo 1 list để thêm sinhvien
ls = []
# Tạo object sinhvien
obj = sinhvien('', 0, 0, 0)
# sinhvien
list_choice = """
                1.Tạo và thêm thông tin sinh viên\n
                2.Hiển thị thông tin sinh viên\n
                3.Tìm kiếm thông tin của sinh viên\n
                4.Xóa sinh viên ra khỏi danh sách\n
                5.Cập nhật thông tin sinh viên\n
                6.Exit\n"""
print("\nChương trình quản lý thông tin sinh viên:")
while True:
    print(list_choice)

    ch = int(input("Nhập lựa chọn:[1,2,3,4,5]: "))

    if(ch == 1):
        ten = 'Pham Van Doanh'
        mssv = 2345
        Toan = 10
        Van = 7
        obj.create(ten, mssv, Toan, Van)

    elif(ch == 2):
        print("\n")
        print("\nDanh sách sinh viên:\n")
        for i in range(ls.__len__()):
            obj.display(ls[i])
            input()

    elif(ch == 3):
        mssv = int(input("Nhập mssv cần tìm: "))
        s = obj.search(mssv)
        if s:
            obj.display(ls[s])
        input()

    elif(ch == 4):
        mssv = int(input("Nhập mssv cần xóa: "))
        obj.delete(mssv)
        print(ls.__len__())
        print("Danh sách sinh viên sau khi xóa:")
        for i in range(ls.__len__()):
            print("\n")
            obj.display(ls[i])
        input()

    elif(ch == 5):
        obj.update()
        print(ls.__len__())
        print("Danh sách sau khi được cập nhật:")
        for i in range(ls.__len__()):
            obj.display(ls[i])
            print("\n")
        input()

    else:
        print("Thank You !")
        exit()
