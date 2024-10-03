# shopping_list = []

# def add_items(item):
#     shopping_list.append(item)

# def remove_items(item):
#     shopping_list.remove(item)

# def view_items():
#     for item in shopping_list:
#         print(item)

# def main():
#     while True:
#         user_choice = input("Do you want to add, remove, view or exit the menu? ").lower()

#         if user_choice == 'add':
#             add_item = input("Add Item: ").strip().lower()
#             add_items(add_item)

#         elif user_choice == 'remove':
#             remove_item = input("Remove Item: ").strip().lower()
#             if remove_item in shopping_list:
#                 remove_items(remove_item)
#             else:
#                 print('Item not found in the list')
#                 pass

#         elif user_choice == 'view':
#             view_items()

#         elif user_choice == 'exit':
#             print('Goodbye!')
#             break
        
#         else:
#             print("Invalid choice. Please try again.")

# main()

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ").strip().lower()
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")

        elif choice == '2':
            item = input("Enter the item to remove: ").strip().lower()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' is not in the shopping list.")

        elif choice == '3':
            if shopping_list:
                print("\nYour Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("\nYour shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
