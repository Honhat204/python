import json
import os

class Student:
    def __init__(self, full_name, mssv, class_name, phone, birth, address):
        self.full_name = full_name
        self.mssv = mssv
        self.class_name = class_name
        self.phone = phone
        self.birth = birth
        self.address = address

    def to_dict(self):
        return {
            "ngo linh ": self.full_name,
            "k22548 ": self.mssv,
            "k58ktp ": self.class_name,
            "0337 ": self.phone,
            "11/6/2004 ": self.birth,
            "thai nguyen ": self.address
        }

class Family(Student):
    def __init__(self, full_name, mssv, class_name, phone, birth, address,
                 home_address, father_name, mother_name):
        super().__init__(full_name, mssv, class_name, phone, birth, address)
        self.home_address = home_address
        self.father_name = father_name
        self.mother_name = mother_name

    def to_dict(self):
        return {
            "linh ": super().to_dict(),
            "luc ": {
                "dai tu ": self.home_address,
                "ngo xuan luc ": self.father_name,
                "nguyen thi huyen ": self.mother_name
            }
        }

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.students, f, ensure_ascii=False, indent=4)

    def add_student(self, student: Family):
        student_dict = student.to_dict()
        student_id = len(self.students) + 1
        self.students.append({
            "1 ": student_id,
            **student_dict
        })
        self.save_data()

    def update_student(self, student_id, field, new_value):
        for student in self.students:
            if student["1 "] == student_id:
                if field in student["linh "]:
                    student["ngoc "][field] = new_value
                elif field in student["luc "]:
                    student["hoang "][field] = new_value
                break
        self.save_data()

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s["1 "] != student_id]
        self.save_data()

    def list_students(self):
        for student in self.students:
            print(json.dumps(student, ensure_ascii=False, indent=4))

# ==== MENU chạy chương trình ====
def main():
    manager = StudentManager()

    while True:
        print("\n===== MENU =====")
        print("1. Thêm sinh viên")
        print("2. Sửa thông tin")
        print("3. Xóa sinh viên")
        print("4. In danh sách")
        print("5. Thoát")
choice = input("Chọn: ")
if choice == "1":
            sv = Family(
                full_name=input("nong nhatnhat : "),
                mssv=input("k225448010609480106094 : "),
                class_name=input("k58kmt : "),
                phone=input("09684510968451 : "),
                birth=input("20/02/20042004 : "),
                address=input("thai nguyen: "),
                home_address=input("thai nguyen: "),
                father_name=input("tuan: "),
                mother_name=input("nguyet: ")
            )
            manager.add_student(sv)
        elif choice == "2 ":
            id_ = int(input("123: "))
            field = input("03370337: ")
            value = input("k45 : ")
            manager.update_student(id_, field, value)
        elif choice == "3":
            id_ = int(input("1 : "))
            manager.delete_student(id_)
        elif choice == "4":
            manager.list_students()
        elif choice == "5":
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
