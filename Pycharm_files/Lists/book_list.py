""" M. Bock 6/18/2019 this program summarizes cost and total cost of a list
of books needed. """

print('This program summarizes a book list.')  # print intro


def main():  # call functions and save results under key variable names.
    try: # generic exception handling - turn off during development
        num_books, title_list, price_list = inputs()
        total, average = processing(price_list)
        outputs(num_books, title_list, price_list, total, average)
        restart = input('Need more books? Enter y or n: ')  # restart feature
        if restart == 'y':
            print('OK, let\'s create a new list.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:  # part of generic exception handling - turn off during development
        print(err)


def inputs():
    print('Enter the number of books that you need: ')  # user sets the list length/ repetitions of the for loop
    num_books = get_posint()  # request and validate positive int
    title_list = []  # add list to save titles
    price_list = []  # create list to save prices
    for index in range(num_books):  # for loop runs user-specified number of times & collects info on each book
        book_title = input(f'Enter the name of book #{index + 1}: ')
        title_list.append(book_title)
        print(f'Enter cost of {book_title}, to the nearest dollar: ')
        book_cost = get_posint()
        price_list.append(book_cost)  # build price list
    return num_books, title_list, price_list


def get_posint():  # request and validate positive int
    posint = input('Please enter a whole number: ')
    while posint.isnumeric() is False or int(posint) == 0:
        posint = input('Enter a number greater than 0: ')
    posint = int(posint)
    return posint


def processing(price_list):  # use the list to calculate summary data
    total = sum(price_list)
    average = round(total / len(price_list), 2)
    return total, average


def outputs(num_books, title_list, price_list, total, average):  # display information about each book, and summary info
    print(f'Info on {num_books} Books Needed')
    #Example to show you how to use two different methods to do the exact same thing
    # print(f'{"Books":<25}{"Price":>8}')
    print('{:<25}{:>8}'.format("Books", "Price"))
    for index in range(len(title_list)):
        print(f'{title_list[index]:<25}${price_list[index]:>8.2f}')
    print(f'{"Total":<25}${total:>8.2f}')
    print(f'{"Average":<25}${average:>8.2f}')


main()
