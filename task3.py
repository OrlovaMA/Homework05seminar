# Задача 3. 
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

# запись в файл изначального текста, открытие его для чтения
with open('text_original_1.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст для сжатия: '))
with open('text_original_1.txt', 'r') as file:
    text_original = file.readline()
    text_compression = text_original.split()

# сжатие и запись в новый файл
coding = ''
prev_symbol = ''
count = 1
for symbol in text_original:
    if symbol != prev_symbol:
        if prev_symbol:
            coding += str(count) + prev_symbol
        count = 1
        prev_symbol = symbol
    else:
        count += 1
else:
    coding += str(count) + prev_symbol
    
print(text_original)
print(coding)
with open('text_coding.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{coding}')


# воостановление и запись в новый файлв
with open('text_coding.txt', 'r', encoding='utf_8') as file:
    text = file.read()

number = ''
text_restored = ''
for i in text:
    if i.isdigit():
        number = number + i
    else:
        text_restored += int(number)*i
        number = ''

print(text_restored)
with open('text_original_2.txt', 'w', encoding='utf_8') as file:
    file.write(text_restored)

