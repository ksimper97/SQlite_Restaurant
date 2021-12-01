import sqlite3

con = sqlite3.connect('inventory.db')
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS inventory (product TEXT, quantity REAL, price REAL)")

def inventory():
    inv_choice = None
    while inv_choice != "6":
        # 1. view 2. insert 3. delete 4. search 5. back
        print("1. View")
        print("2. Insert")
        print("3. Update")
        print("4. Delete")
        print("5. Search")
        print("6. Back")
        inv_choice = input ("> ")

        if inv_choice == "1":
            cursor.execute("SELECT * FROM inventory")
            print("{:>10} {:>10} {:>10}".format("Product", "Quantity", "Price"))
            for record in cursor.fetchall():
                print("{:>10} {:>10} {:>10}".format(record[0],record[1],record[2]))
            print()
        
        if inv_choice == "2":
            try:
                product = input("Product: ")
                cursor.execute("SELECT product FROM inventory WHERE product = ?", (product,))
                if len(cursor.fetchall()) == 0:
                    
                    quantity = input("Quantity: ")
                    price = input("Price: ")
                    values = (product, quantity, price)
                    cursor.execute("INSERT INTO inventory VALUES (?,?,?)", values)
                    con.commit()
                else:
                    print("Product already exists. Updating...")
                    quantity = input("New Quantity: ")
                    values = (quantity, product)
                    cursor.execute("UPDATE inventory SET quantity = ? WHERE product = ?", values)
                    con.commit()

            except ValueError:
                print("Invalid Input")

        if inv_choice == "3":
            try:
                product = input("Product: ")
                quantity = input("New Quantity: ")
                values = (quantity, product)
                cursor.execute("UPDATE inventory SET quantity = ? WHERE product = ?", values)
                con.commit()
                if cursor.rowcount == 0:
                    print("Invalid Product")
            except ValueError:
                print("Invalid Input")

        if inv_choice == "4":
            try:
                product = input("Delete: ")
                cursor.execute("DELETE FROM inventory WHERE product = ?", (product,))
                con.commit()
            except ValueError:
                print("Invalid Input")

        if inv_choice == "5":
            product = input("Enter Product Name: ")
            cursor.execute("SELECT product FROM inventory WHERE product = ?", (product,))
            if len(cursor.fetchall()) == 0:
                print("Product doesn't exist")
            else:
                cursor.execute("SELECT * FROM inventory WHERE product = ?", (product,))
                print("{:>10} {:>10} {:>10}".format("Product", "Quantity", "Price"))
                for record in cursor.fetchall():
                    print("{:>10} {:>10} {:>10}".format(record[0],record[1],record[2]))
                print()
        

        

choice = None
while choice != "4":
    print("1. Inventory")
    print("2. Reservation")
    print("3. Tables")
    print("4. Quit")
    choice = input("> ")
    print()
    if choice == "1":
        inventory()
    if choice =="2":
        pass
    if choice =="3":
        pass