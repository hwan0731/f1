# -*- coding: utf-8 -*-
import pandas as pd

def show_driver_rankings():
    driver_standings = [
        {"순위": 1, "드라이버": "Max Verstappen", "팀": "Red Bull", "포인트": 437},
        {"순위": 2, "드라이버": "Lando Norris", "팀": "McLaren", "포인트": 374},
        {"순위": 3, "드라이버": "Charles Leclerc", "팀": "Ferrari", "포인트": 356},
        {"순위": 4, "드라이버": "Oscar Piastri", "팀": "McLaren", "포인트": 292},
        {"순위": 5, "드라이버": "Carlos Sainz", "팀": "Ferrari", "포인트": 290},
        {"순위": 6, "드라이버": "George Russell", "팀": "Mercedes", "포인트": 245},
        {"순위": 7, "드라이버": "Lewis Hamilton", "팀": "Mercedes", "포인트": 223},
        {"순위": 8, "드라이버": "Sergio Perez", "팀": "Red Bull", "포인트": 152},
        {"순위": 9, "드라이버": "Fernando Alonso", "팀": "Aston Martin", "포인트": 94},
        {"순위": 10, "드라이버": "Esteban Ocon", "팀": "Alpine", "포인트": 65}
    ]
    df = pd.DataFrame(driver_standings)
    print("\n드라이버 순위 (1~10위):")
    print(df.to_string(index=False))

def show_constructor_rankings():
    constructor_standings = [
        {"순위": 1, "팀": "Red Bull", "포인트": 589},
        {"순위": 2, "팀": "McLaren", "포인트": 666},
        {"순위": 3, "팀": "Ferrari", "포인트": 652},
        {"순위": 4, "팀": "Mercedes", "포인트": 468},
        {"순위": 5, "팀": "Aston Martin", "포인트": 94}
    ]
    df = pd.DataFrame(constructor_standings)
    print("\n컨스트럭터 순위:")
    print(df.to_string(index=False))

def show_driver_wins():
    driver_wins = [
        {"순위": 1, "드라이버": "Lewis Hamilton", "우승 횟수": 105},
        {"순위": 2, "드라이버": "Michael Schumacher", "우승 횟수": 91},
        {"순위": 3, "드라이버": "Max Verstappen", "우승 횟수": 65}
    ]
    df = pd.DataFrame(driver_wins)
    print("\n역대 드라이버 우승 횟수:")
    print(df.to_string(index=False))

def show_podium_counts():
    podiums = [
        {"드라이버": "Max Verstappen", "포디움 횟수": 18},
        {"드라이버": "Lando Norris", "포디움 횟수": 17},
        {"드라이버": "Charles Leclerc", "포디움 횟수": 16}
    ]
    df = pd.DataFrame(podiums)
    print("\n2024 포디움 횟수 (1~3등):")
    print(df.to_string(index=False))

def show_race_count():
    race_count = 24
    print(f"\n2024시즌 그랑프리 레이스 횟수: {race_count}회")

# 메뉴 표시 및 선택
def show_menu():
    while True:
        print("\nF1 데이터 메뉴:")
        print("1. 드라이버 순위")
        print("2. 컨스트럭터 순위")
        print("3. 역대 드라이버 우승 횟수")
        print("4. 2024 포디움 횟수")
        print("5. 2024 레이스 횟수")
        print("0. 종료")

        choice = input("원하는 항목 번호를 입력하세요: ")

        if choice == '1':
            show_driver_rankings()
        elif choice == '2':
            show_constructor_rankings()
        elif choice == '3':
            show_driver_wins()
        elif choice == '4':
            show_podium_counts()
        elif choice == '5':
            show_race_count()
        elif choice == '0':
            print("종료합니다.")
            break
        else:
            print("올바른 숫자를 입력하세요.")

# 실행
show_menu()

