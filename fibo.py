

def recursive_nth_fibo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)


def main():
    n = 15
    print(recursive_nth_fibo(n))


if __name__ == "__main__":
    main()
