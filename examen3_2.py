def palidrom(word):
    word1=word[::-1]
    if word1==word:
        print('Yes')
    else:
        print('No')

word=input('Введите слово: ').lower()
palidrom(word)