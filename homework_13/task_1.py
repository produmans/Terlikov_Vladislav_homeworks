"""
Напишите программу, которая запрашивает у пользователя информацию о различных книгах и сохраняет их данные в файл формата CSV.
Требования: Программа должна запрашивать у пользователя информацию о каждой книге, включая название,
 автора и год издания.
Информация о каждой книге должна быть сохранена в отдельной строке файла CSV.
Файл CSV должен иметь следующие заголовки столбцов: "Название", "Автор", "Год издания".
 Программа должна продолжать запрашивать информацию о книгах до тех пор, пока пользователь не введет команду "stop" для завершения.
В конце выполнения программы должно быть выведено сообщение о успешном сохранении данных.
"""
import csv
with open('databooks.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Название', 'Автор', 'Год издания'])
    while True:
        call = input("Введите название книги или 'stop' для завершения: ")
        if call == 'stop':
            break
        author = input("Введите автора книги: ")
        year = input("Введите год написания книги: ")
        writer.writerow([call, author, year])
print('Данные о кгнигах успешно сохранены')

