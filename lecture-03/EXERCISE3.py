hours = int(input("Enter the number of hours worked: "))
rate = float(input("Enter the hourly pay rate: "))
if hours > 40:
    gross = hours * rate
else:
    gross = 40 * rate (hours - 40) * rate * 1.5

    print(f"The gross pay is: ${gross:.2f}")