
def is_prime(num):
    if num == 2:
        return True
    else:
        for i in range(2, num//2 + 1):
            if num % i == 0:
                return False

            return True

def main():
    while True:
        start, stop = tuple(map(int, input("Enter range start from stop with space : ").split()))
        if start >= 2 and stop > start and stop <= 100:
            break
    for i in range(start, stop + 1):
        if is_prime(i):
            print(i, end=" ")

if __name__ == '__main__':
    main()
