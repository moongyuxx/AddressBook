class AddressBook:
    def __init__(self):
        self.addresses = {}    

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
                print(f"{name}  {i["phone"]}  {i["email"]}\n")

    def search_address(self):
        name_search = input("검색할 이름: ")
        if name_search in self.addresses:
            address = self.addresses["name_search"]
            print(f"{name_search}  {address["phone"]}  {address["email"]}\n")            
        else:
            print("저장된 연락처 없음\n")
        