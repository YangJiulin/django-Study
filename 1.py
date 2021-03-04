class A:
    a = 1
    def __str__(self) -> str:
        return 'A'

if __name__ == '__main__':
    a = A()
    print(a)