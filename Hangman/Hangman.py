tries = -1
old_letters = []
HANGMAN_PHOTOS = {0:'x-------x\n|\n|\n|\n|\n|',
                  1:'x-------x\n|\t|\n|\t0\n|\n|\n|',
                  2:'x-------x\n|\t|\n|\t0\n|       | \n|\n|',
                  3:'x-------x\n|\t|\n|\t0\n|      /| \n|\n|',
                  4:'x-------x\n|\t|\n|\t0\n|      /|\ \n|\n|',
                  5:'x-------x\n|\t|\n|\t0\n|      /|\ \n|      /\n|',
                  6:'x-------x\n|\t|\n|\t0\n|      /|\ \n|      / \ \n|',}
def print_start():
    print(''' _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
|  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                    |___/''')

def choose_word(file_path, index):
    """Get a word from a file
    :param file_path: the file path
    :param index: the index of the word in the text
    :type file_path: string
    :type index: int
    :return: the word from the file
    :rtype: string
    """
    f = open(file_path, 'r')
    lst = f.read().split()
    f.close()
    while(index > len(lst)):
        index -= len(lst)
    return lst[index-1]

def print_hangman(num_of_tries):
    """print hangman according to numbers of wrong tryies
    :param num_of_tries: number of bad trys
    :type num_of_tries: int
    :return: None
    :rtype: None
    """
    print(HANGMAN_PHOTOS[num_of_tries])
        
    #word for game
def is_valid_input(letter_guessed, old_letters_guessed):
    """Check if letter that have been entred is valid
    :param letter_guessed: The letter that have been guesed
    :param old_letters_guessed: the letters the user guessed already
    :type letter_guessed: string
    :type old_letters_guessed: string
    :return: return if letter is valid
    :rtype: boolean
    """
    if((len(letter_guessed) > 1) or (letter_guessed.isalpha() == False) or ((letter_guessed in old_letters_guessed) == True)):
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed, word):
    """Get a new guess letter
    :param letter_guessed: The letter that have been guesed
    :param old_letters_guessed: the letters the user guessed already
    :param word: word need to guess
    :type letter_guessed: string
    :type old_letters_guessed: string
    :type word: string
    :return: return if succed to update letter guessed
    :rtype: boolean
    """
    if(is_valid_input(letter_guessed, old_letters_guessed)):
        old_letters.append(letter_guessed.lower())
        if(letter_guessed.lower() not in list(word)):
            global tries
            print(':(')
            tries += 1
            print_hangman(tries)
        return True
    else:
        print("X")
        old_letters_guessed.sort()
        print("->".join(old_letters_guessed[:len(old_letters_guessed)]))
        return False

def get_letter(word):
    """Get a new guess letter
    :param word: word need to guess
    :type word: string
    :return: return new def to get a correct input
    :rtype: def
    """
    lguess = input('Guess a letter: ').lower()
    if(is_valid_input(lguess,old_letters)):
        try_update_letter_guessed(lguess, old_letters, word)       
    else:
        try_update_letter_guessed(lguess, old_letters, word) 
        return get_letter(word)

def show_hidden_word(secret_word, old_letters_guessed):
    """Show Hidden word.
    :param secret_word: word need to guess
    :param old_letters_guessed: the letters the user guessed already
    :type secret_word: string
    :type old_letters_guessed: list
    :return: a String with the letters that have been guested.
    :rtype: String
    """
    li = list(secret_word.lower())
    hidden = ""
    for i in range(len(secret_word)):
        if li[i] in old_letters_guessed:
            hidden += (li[i]+" ")
        else:
            hidden += "_ "
    return hidden

def check_win(word, old_letters):
    """Check if User Win.
    :param word: word need to guess
    :param old letters: the letters the user guessed already
    :type base: string
    :type exponent: list
    :return: The result if the user win or not
    :rtype: Boolean
    """
    if(show_hidden_word(word, old_letters).find("_")!=-1):
        return False
    return True
            
def main():
    global tries
    print_start()
    path = input('Enter a file path: ')
    usernum = int(input('Enter a number: '))
    word = choose_word(path,usernum)
    print('Lets start!!! \n\n')
    print('x-------x')
    while(check_win(word, old_letters)==False):
        print(show_hidden_word(word, old_letters))
        get_letter(word)
        if(tries == 6):
            print('Lose')
            break
    if(tries < 6):
        print(show_hidden_word(word, old_letters))
        print('WIN')

if __name__ == "__main__":
    main()
