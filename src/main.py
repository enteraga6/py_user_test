from src.hello.hello import hello_world
from src.fib.fib import fibonacci

def main():
    hello_world()
    n = int(input("Enter the number of terms: "))
    print("The first {} Fibonacci numbers are:".format(n))
    for i in range(n):
        print(fibonacci(i))

if __name__ == "__main__":
    main()
