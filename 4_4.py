class FibonacciContainer:
    def __init__(self, n):
        self.fibonacci_numbers = self.generate_fibonacci_numbers(n)
    
    def generate_fibonacci_numbers(self, n):
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci
    
    def __len__(self):
        return len(self.fibonacci_numbers)
    
    def __getitem__(self, index):
        return self.fibonacci_numbers[index]

# створення об'єкта класу FibonacciContainer з n = 10
fib_container = FibonacciContainer(10)

print("Довжина контейнера:", len(fib_container))
print("Перші 5 чисел:", fib_container[:5])
