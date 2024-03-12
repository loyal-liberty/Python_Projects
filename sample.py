def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    x = float(input("Enter the value of x: "))
    n_terms = int(input("Enter the number of terms to calculate: "))
    
    result = 0
    
    for i in range(n_terms):
        term = ((-1) ** i) * (x ** (i + 1)) / factorial(i + 1)
        result += term
    
        if i % 2 == 0:
            print(f"{x}^{i + 1}/{i + 1}! = {term}", end=" ")
        else:
            print(f"- {x}^{i + 1}/{i + 1}! = {term}", end=" ")
    
    print("\nSum of the series:", result)

if __name__ == "__main__":
    main()
