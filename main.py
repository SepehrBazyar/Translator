#Written by: Sepehr Bazyar
import translators, logging
from typing import Callable

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)-10s - %(message)s')

def translator(func: Callable) -> Callable: #decorator without parameters
    def inner(*args, **kwargs):
        my_text = func(*args, **kwargs)
        if isinstance(my_text, str): my_text = [my_text] #output of func may be string
        translations = []
        for sentence in my_text:
            if sentence: translations.append(translators.bing(sentence, to_language = 'fa')) #sentence not empty
        return translations
    return inner

@translator
def text_spliter(path: str) -> list:
    try:
        with open(path) as fl:
            lines = fl.readlines()
        result = []
        for line in lines:
            result.extend(line.split('.')) #split and append each iter to answer
        result = [item.strip() for item in result if item.strip()] #remove space
        return result
    except:
        logging.error("File Not Found in this Path...!")
        return [] #empty list because translator decorator need to list answer

print(*text_spliter("C:\\Users\\sony\\Desktop\\Translation\\test.txt"), sep = '\n')
