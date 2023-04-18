shoppingCart = {}

# Define menu function
def mainMenu():
    print("\nWELCOME TO THE AMANDO SHOPPING SITE\n")
    print("1. Add product to the cart.")
    print("2. Search the product.")
    print("3. Delete the product from the cart.")
    print("4. Quit.")

# Define the function to add a product
def addProduct():
    if len(shoppingCart) >= 5:
        print("Cart is full")
    else:
        n = int(input("Enter the number of products to add: "))
        if len(shoppingCart) + n > 5:
            print("Cart is full")
        else:
            for i in range(n):
                productName = input("Enter product name: ")
                brandName = input("Enter brand name: ")
                shoppingCart[productName] = brandName
            print("Product(s) added successfully")

def searchProduct():
    productName = input("Enter product name: ")
    if productName in shoppingCart:
        print("Product name: ", productName)
        print("Brand name: ", shoppingCart[productName])
    else:
        print("No product exists with this name")

# Define the function to delete a product 
def deleteProduct():
    if len(shoppingCart) == 0:
        print("Cart is empty, no item is found")
    else:
        productName = input("Enter product name to delete: ")
        if productName in shoppingCart:
            del shoppingCart[productName]
            print("Product deleted successfully")
        else:
            print("No product exists with this name")

# Main program loop
while True:
    mainMenu()
    choice = input("\nEnter your choice: ")
    
    if choice == "1" or choice == "1":
        addProduct()
    elif choice == "2" or choice == "2":
        searchProduct()
    elif choice == "3" or choice == "3":
        deleteProduct()
    elif choice == "4" or choice == "4":
        break
    else:
        print("Invalid choice. Please enter again.")
