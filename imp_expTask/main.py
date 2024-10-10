from utilities.textNum import removeText
from utilities.dateFormate import customDate
def main():
    print('main function')
    userText = removeText(str)
    print(f'onlyReturnsNumbers = {userText}')

    print()
    userDate = customDate()
    print(f'convertDate = {userDate}')
   

if __name__ == '__main__':
    main()

