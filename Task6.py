def int_func(words):
    words_list = words.split(" ")
    words =""
    for i in range(len(words_list)):
        letters = list(words_list[i])
        letters[0] = chr(ord(letters[0])-32)
        word =""
        for n in letters:
            word = word + str(n)
        words_list[i] = word
        words = words + word + " "
        
    return words

test_text = "under the ocean, green and deep \
lie the fishes fast asleep, \
under the arm and over the shoe, \
top on the head, and out goes you"
        
print(int_func(test_text))

# Решение через функцию в функции

def external_func(words):
    
    def internal_func(word):
        letters = list(word)
        letters[0] = chr(ord(letters[0])-32)
        word =""
        for i in letters:
            word = word + str(i)
        return word
    
    words_list = words.split(" ")
    words =""
    for i in range(len(words_list)):
        words = words + internal_func(words_list[i]) + " "
        
    return words

print(external_func(test_text))