class Program:
    @staticmethod
    def main():
        n = int(input())

        fibonacci = [0, 1]

        while len(fibonacci) < n + 2:
            new_fibonacci = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(new_fibonacci)

        print(fibonacci[-1])

        # Alternative recursive approach:
        # print(Program.get_fibonacci(n))

    @staticmethod
    def get_fibonacci(n):
        if n <= 1:
            return 1

        return Program.get_fibonacci(n - 1) + Program.get_fibonacci(n - 2)

Program.main()
