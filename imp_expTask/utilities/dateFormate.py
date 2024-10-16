from datetime import date
import re
#yyyy-mm-dd
def customDate():
    enterDate = input('Enter Date in yyyy-mm-dd or mm-dd-yyyy format only = ')
    #yyyy-mm-dd
    if re.match(r'\d{4}-\d{2}-\d{2}',enterDate) :
        output = re.sub(r'(\d{4})-(\d{2})-(\d{2})',r'\3-\2-\1',enterDate)
        return{
            'status' :'success',
            'result' : output
        }
    #mm-dd-yyyy
    elif re.match(r'\d{2}-\d{2}-\d{4}',enterDate):
        output = re.sub(r'(\d{2})-(\d{2})-(\d{4})',r'\2-\1-\3',enterDate)
        return{
            'status' : 'success',
            'result' :  output
        }
    else :
        return {
            'status' : 'error',
            'result' : 'Enter Date in yyyy-mm-dd or mm-dd-yyyy format only'
        }  

if __name__ == '__main__':
    customDate()