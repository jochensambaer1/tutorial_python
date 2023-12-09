def main():
    try:
        number = float(input("Enter a number: "))
        
        while number != 1:
            if number % 2 == 0:
                result = number / 2
            else:
                result = number * 3 + 1
            
            print("Result:", result)
            number = result
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
