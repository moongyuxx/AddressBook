def menu():
    print("1. 연락처 입력")
    print("2. 모든 연락처 출력")
    print("3. 연락처 검색")
    print("4. 연락처 삭제")
    print("5. 종료")
    menu = input("메뉴선택: ")
    return menu
    
def main():
    while True:
        menu = print_menu()
        if menu == 1:
        elif menu == 2:
        elif menu == 3:
        elif menu == 4:
        elif menu == 5:
            break
        else:
            print("1~5를 입력해주세요.")
            
if __name__ == "__main__":
    main()