# main.py - 간단한 계산기 프로그램

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history = []

def main():
    calc = Calculator()
    
    print("=== 간단 계산기 ===")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 히스토리 보기")
    print("4. 종료")
    print("4. 추가")
    
    while True:
        choice = input("\n선택하세요 (1-4): ")
        
        if choice == '1':
            a = float(input("첫 번째 숫자: "))
            b = float(input("두 번째 숫자: "))
            result = calc.add(a, b)
            print(f"결과: {result}")
            
        elif choice == '2':
            a = float(input("첫 번째 숫자: "))
            b = float(input("두 번째 숫자: "))
            result = calc.subtract(a, b)
            print(f"결과: {result}")
            
        elif choice == '3':
            history = calc.get_history()
            if history:
                print("\n=== 계산 히스토리 ===")
                for item in history:
                    print(item)
            else:
                print("히스토리가 없습니다.")
                
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
            
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()