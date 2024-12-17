class AddressBook:
    def __init__(self):
        self.addresses = {}    

    def add_address(self):
    
        name = input("이름: ")
        phone = input("전화번호: ")
        email = input("이메일: ")
        self.addresses[name] = {"phone": phone, "email": email}

 