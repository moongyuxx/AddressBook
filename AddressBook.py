import csv
class AddressBook:
    def __init__(self):
        self.addresses = {} 
        self.load_address()

    def add_address(self):
    
        name = input("이름: ")
        phone = input("전화번호: ")
        email = input("이메일: ")
        self.addresses[name] = {"phone": phone, "email": email}

    def print_address(self):
        if not self.addresses:
            print("저장된 연락처 없음\n")
        else:
            for name, i in self.addresses.items():
                print(f"{name}  {i['phone']}  {i['email']}\n")

    def search_address(self):
        name_search = input("검색할 연락처 이름: ")
        if name_search in self.addresses:
            address = self.addresses[name_search]
            print(f"{name_search}  {address['phone']}  {address['email']}\n")            
        else:
            print("저장된 연락처 없음\n")
        
    def delete_address(self):
        name_del = input("삭제할 연락처 이름: ")
        if name_del in self.addresses:
            del self.addresses[name_del]
            print(f"{name_del} 삭제되었습니다.\n")            
        else:
            print("저장된 연락처 없음\n")
            
    def store_address(self):
        with open ("AddressBook.csv", mode="w", newline="", ) as file:
            writer = csv.writer(file)
            writer.writerow(["name", "phone", "email"])
            for name, i in self.addresses.items():
                writer.writerow([name, i['phone'], i['email']])
                
    def load_address(self):
        try:
            with open ("AddressBook.csv", mode="r", newline="", ) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.addresses[row['name']] =  {"phone": row['phone'], "email": row['email']}
        except FileNotFoundError:
            self.store_address()