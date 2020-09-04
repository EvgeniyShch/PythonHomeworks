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