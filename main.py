from AddressBook import AddressBook

def print_menu():
    print("1. 연락처 입력")
    print("2. 모든 연락처 출력")
    print("3. 연락처 검색")
    print("4. 연락처 삭제")
    print("5. 종료")
    menu = int(input("메뉴선택: "))
    return menu
    
def main():
    address = AddressBook()
    while True:
        menu = print_menu()
        if menu == 1:
            address.add_address()
        elif menu == 2:
            address.print_address()
        elif menu == 3:
            address.search_address()
        elif menu == 4:
            address.delete_address()
        elif menu == 5:
            address.store_address() #종료되면 주소록 저장
            break
        else:
            print("1~5를 입력해주세요.")
            
if __name__ == "__main__":
    main()