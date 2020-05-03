import re
text = input('Введите слова через пробел: ')
pattern = r'\b[a-zA-Z]+\b'
text_list = re.findall(pattern, text)
text_list.sort(key=len)
print(text_list)
