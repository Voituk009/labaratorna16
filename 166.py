#cd D:python/python/16
#166.py
#Напишите программу в которой ФИО вводятся 
#из текстового файла и затем выводятся на экран.

print("Чтение файла:\n")

File = open('file.txt', 'r')

for line in File:
	print(line)