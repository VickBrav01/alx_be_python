shopping_list = []

def add_items(item):
    shopping_list.append(item)

def remove_items(item):
    shopping_list.remove(item)

def view_items():
    for item in shopping_list:
        print(item)

def main():
    while True:
        user_choice = input("Do you want to add, remove, view or exit the menu? ").lower()

        if user_choice == 'add':
            add_item = input("Add Item: ").strip().lower()
            add_items(add_item)

        elif user_choice == 'remove':
            remove_item = input("Remove Item: ").strip().lower()
            if remove_item in shopping_list:
                remove_items(remove_item)
            else:
                print('Item not found in the list')
                pass

        elif user_choice == 'view':
            view_items()

        elif user_choice == 'exit':
            print('Goodbye!')
            break
        
        else:
            print("Invalid choice. Please try again.")

main()

