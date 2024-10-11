
import re


def removeText():
    enterText = input('Enter any text with numbers  =  ')
    num = re.sub('[^0-9]','',enterText) 
    
    if num and num != None and num != '':
        return {
            'status' : 'success',
            'result' :  num,
        }
    else :
        return {
            'status' : 'error',
            'result': 'Enter text with numbers'
        }
       
        