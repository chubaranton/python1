Code

Encryption(шифрование) - процесс преобразования информации с использование алгоритма.
Есть такие алгоритмы: Цезаря (в котором есть возможность взлома(взлом выполняется метода
частотного анализа), Виженера и Вернама. Каждая функция подднрживает как кодировку входный данных, так и раскодировку.

    -inp <path\to\file> - путь к файлу с исходным текстом
    -out <path\to\file> - путь к файлу, в который будет записан текст (если файл не существует, то по
    переданному пути будет создан файл с переданным именем)
    doc <code or decode> - булева переменная.“code”:шифровать, “decode”:дешифрования
    -fa <1 or None» - булева переменная, “1”, она же "Тrue“: применить алгоритм частотного анализа
    -t - ‘caesar’- шифровать с помощью Цезаря, ‘vigenere’- шифровать с помощью Виженера, ‘vernam’ - шифровать с помощью Вернама
    -k <path\to\file> - путь к файлу, в котором хранится ключ

