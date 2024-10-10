from datetime import date
import re
#yyyy-mm-dd
def customDate():
    enterDate = str(input('Enter date = '))

    dateToday = date.fromisoformat(enterDate)
#convertDate = re.sub('[^dd][mm][yyyy]','-',enterDate)

    print(f'Date = {dateToday}')
    convertDate = dateToday.strftime('%d'),dateToday.strftime('%B'),dateToday.strftime('%Y')
    return {convertDate}
    


if __name__ == '__main__':
    customDate()