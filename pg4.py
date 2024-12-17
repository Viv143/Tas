'''Write a Python program that uses a set to store unique words from a text input. 
The program should ignore cases and count the number of unique words.'''


class Unique_words:
    def __init__(self):
        self.words=set()   # To store unique words in set

    def adding_text(self,text):
        self.words.update(text.lower().split())  # Adding words form input text in set 

    def unique_word_count(self):                 # Counting Unique Words
        return len(self.words)
    
    def disp_unique_words(self):                 # Display unique words
        print("Unique Words:",self.words)


text=input("enter some text:")
U1=Unique_words()
U1.adding_text(text)
U1.disp_unique_words()
print("Number of unique words:",U1.unique_word_count())

