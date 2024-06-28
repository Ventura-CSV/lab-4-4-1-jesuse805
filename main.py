def main():
    """
    ########################################
    Code Your Program here
    """
    number = 0
    while number <= 0 or number >= 100:
        number = int(input('Enter a value greater than 0 and less than 100: '))
        
    """
    ########################################
    """

    print(number)

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
