import nltk
from nltk.tokenize import word_tokenize
# nltk.download('punkt')
import pickle as pkl

def add(a,b):
    return a+b

def div(a, b):
    # try:
    #     c = a/b
    #     return c
    # except ZeroDivisionError as error:
    #     return "Error"
    if b ==0:
        raise ValueError("Cant be zero")
    return a/b

def tokenize(some_str):
    return word_tokenize(some_str)
# print(tokenize("This is a very long string please tokenize me"))


def load_pkl(pkl_path):
    with open("dcit.pkl", "rb") as pkl_file:
        adict = pkl.load(pkl_file)
    return adict


class SomeFunc():
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    def some_func(self):
        pass
    def _add(self):
        return f"{self.a} : {self.b}"

class Complex():
    def __init__(self,real,img):
        self.re=real
        self.imz=img
    
    def __str__(self):
        return f"{self.re}+ {self.imz}i"
    
    def __add__(self,other):
        return f"{self.re+other.re} + {self.imz+other.imz}i"

