#Напишите функцию, которая принимает на вход строку и подсчитывает 
#в ней количество слов начинающихся на каждую букву алфавита.
#Возвращать функция должна словарь следующего вида:

#{'a': 10, 'b': 3, 'c': 0, ...}
#Для задания словаря используйте строку с алфавитом:

#alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
#Словарь с буквами создайте с помощью генератора.

#Не забудьте, что слова в предложении могут начинаться с большой буквы!

def words_count (text):
    punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
    for i in punctuation_list:
        text=text.replace(i,'')
    text=text.lower()
    text=text.split()
    new_list=[]
    alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
    
    for a in text:
        if a[0] not in alphabet_str:
            new_list.append(a[0])
            
    
    def dict_first_l_funk(new_list):
        first_later_dict={}
        for b in new_list:
            if b not in first_later_dict:
                first_later_dict[b]=1
            if b in first_later_dict:
                first_later_dict[b]+=1
        yield first_later_dict
        
    first_later_dict=dict_first_l_funk(new_list)
    print(first_later_dict)

text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

print(words_count(text_example))