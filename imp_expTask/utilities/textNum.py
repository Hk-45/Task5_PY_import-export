
import re


def removeText():
    enterText = input('Enter any text =  ')
    num = re.sub('[^0-9]','',enterText) 
    
    if isinstance(enterText, str):
        return {
            'status' : 'success',
            'result' :  num,
        }
    else :
        return {
            'status' : 'error',
            'result': 'Enter the text'
        }
       
        