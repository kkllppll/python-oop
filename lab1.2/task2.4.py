class Workfile():
    def __init__(self, number_of_characters = 0, number_of_words = 0, number_of_sentences = 0 ):
        self._number_of_characters = number_of_characters 
        self._number_of_words = number_of_words 
        self._number_of_sentences = number_of_sentences 

        
    def words(self):
        try:
            file = open('texttask.txt.txt', 'r')
        except(FileExistsError, FileNotFoundError):
            raise Exception("The file cannot be opened")

        data = file.read()
        words = data.split()
        self._number_of_words += len(words)
        file.close()
        return self._number_of_words

    def characters(self):
        try:
            file = open('texttask.txt.txt', 'r')
        except(FileExistsError, FileNotFoundError):
            raise Exception("The file cannot be opened")

        data = file.read()
        characters = data.strip()
        self._number_of_characters += len(characters) - characters.count(' ')
        file.close()
        return self._number_of_characters


    def sentences(self):
        try:
            file = open('texttask.txt.txt', 'r')
        except(FileExistsError, FileNotFoundError):
            raise Exception("The file can't be opened")

        data = file.read()
        for data in file:
            data = data.replace('!?', '.').replace('?!', '.').replace('...', '.').replace('?\n', '?').replace('.\n', '.') 
        self._number_of_sentences += len([i for i in data.split('. ')])
    
        file.close()
        return self._number_of_sentences


task = Workfile()
print("Words in a file:", task.words())
print("Characters in a file:", task.characters())
print("Sentences in a file:", task.sentences())



