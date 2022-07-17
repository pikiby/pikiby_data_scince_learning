#Test

def count_words(sentence_str):
    alphabet_str = "abcdefghijklmnopqrstuvwqyz"
    letters_dict = {letter: 0 for letter in alphabet_str}
    def lettets_dict (alphabet_str):
        for letter in alphabet_str:
            yield {letter:0}
    
    a=dict(letters_dict)
    words_list = sentence_str.lower().split()
    for word in words_list:
        a(word[0]) += 1
    return letters_dict

str_example = "Fibonacci numbers are strongly related to the golden ratio: Binet's formula expresses the nth Fibonacci number in terms of n and the golden ratio, and implies that the ratio of two consecutive Fibonacci numbers tends to the golden ratio as n increases."
print(count_words(str_example))