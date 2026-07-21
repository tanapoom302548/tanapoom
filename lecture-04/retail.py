answer = 'y'
while answer.lower() == 'y':
    wholesale = float(input("Enter the item's wholesale cost: "))
    retail = wholesale * 2.5

    print(f"Retail price: ${retail:.2f}")


answer = input("Do you have another item? (Enter y for yes): ")
print("Program End")
    

 
