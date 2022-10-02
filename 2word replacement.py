# program to illustrate the function replace in python
  
  
def replace_word():
    str="Hi i am Susan and i like python ,i,i"
    word_to_replace=input("Enter the word to replace:")
    word_replacement=input("Enter the word replacement:")
    print(str.replace(word_to_replace,word_replacement))

replace_word()
