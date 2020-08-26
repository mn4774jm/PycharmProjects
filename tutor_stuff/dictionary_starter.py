""" M. Bock 6/29/2020 Dictionary Sample Program – this starter program is very similar to the lab.
As you adapt it to the new content, you will have to add a new "edit" feature, for the user
to change an existing entry. The edit option has to be added to the menus, and a function has to be
added and called. In addition, note the program features of the starter file that change case of strings.
You may have to adapt this code to fit capitalization of your new program. """

def main():
    try:
        user_info = {'Fourty-2': 'Douglas Adams', 'wakeUpSheeple': 'Phillip K. Dick'}
        display_menu()
        while True:
            command = input('Command: ')
            command = command.lower()
            if command == 'view':
                view(user_info)
            elif command == 'add':
                add(user_info)
            elif command == 'edit':
                edit(user_info)
            elif command == 'del':
                delete(user_info)
            elif command == 'exit':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')


def display_menu():
    print('COMMAND MENU')
    print('view - View username')
    print('add - Add a new user')
    print('edit - Edit an existing user')
    print('del - Delete a user')
    print('exit - Exit program')
    print()


def view(user_info):
    display_codes(user_info)
    user_name = input('Enter username to view: ')
    user_name = user_info.get(f'{user_name}', 'No such entry')
    print(user_name)

    # This is how the code looks without the .get() method
    # if user_name in user_info:
    #     user_name = user_info[user_name]
    #     print('Country name: ' + user_name + '.\n')
    # else:
    #     print('There is no country with that code. \n')


def add(user_info):
    display_codes(user_info)
    user_name = input('Enter new username to add: ')
    user_name = user_name.upper()
    if user_name in user_info:
        user_name = user_info[user_name]
        print(user_name + ' is already using this nem. \n')
    else:
        user_name = input('Enter user full name: ')
        user_name = user_name.title()
        user_info[user_name] = user_name
        print(user_name + ' was added. \n')

def edit(user_info):
    display_codes(user_info)
    user_name = input('Please enter the username of the user you would like to change: ').upper()
    if user_name in user_info:
        user_info[user_name] = input(f'You have entered {user_info[user_name]}. Please enter new name: ').title()
        # user_info[user_name] = new_country
        print(f'{user_name} is now associated with {user_info[user_name]}.')
    else:
        print("Username not recognized")
    print()

def delete(user_info):
    display_codes(user_info)
    user_name = input('Enter username to delete: ')
    user_name = user_name.upper()
    if user_name in user_info:
        user_name = user_info.pop(user_name)
        print (user_name + ' was deleted. \n')
    else:
        print ('There is no user with that name. \n')


def display_codes(user_info):
    user_names = list(user_info.keys())
    user_names.sort()
    line = 'User names: '
    for user_name in user_names:
        line += user_name + ' '
    print(line)


if __name__ == '__main__':
    main()


