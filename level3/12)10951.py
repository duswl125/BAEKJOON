# 문제
'''두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.'''

# 입력
'''입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)'''

# 출력
'''각 테스트 케이스마다 A+B를 출력한다.'''

# 소스 코드
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break

# EOF(End Of File) : try 내부 코드 실행, 에러가 발생하면 break
'''
While True: (True 또는 1)
    try:
        
    except EOFError:
        break
'''
'''입력의 끝(EOF)에 도달하면 input()은 빠져나올 수 있지만,
sys.stdin.readline()은 빈 문자열만 반환하고 에러를 내지 않음'''