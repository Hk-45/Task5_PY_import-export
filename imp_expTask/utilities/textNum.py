
import re


def removeText(enterText):
    enterText = input('Enter any text =  ')
    num = re.sub('[^0-9]','',enterText) 
    
    if isinstance(enterText, str and int):
        return {
            'status' : 'success',
            'result' :  num,
        }
    else :
        return {
            'status' : 'error',
            'result': 'Enter the text'
        }
       
        