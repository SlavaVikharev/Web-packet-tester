Web-packet-tester
=================

Для поиграться
--------------
+ Запускаем tester.py
+ Обязательно наличие папки tests</br>
  в которой лежат все тесты с расширением *.anq
+ Вообще говоря наличие всех файлов из zip-a необходимо,</br>
  ну кроме, разумеется, ридми и гитигнор...

Тесты
-----
Пишем в формате:
```
# если хочется комментов
hex
    Some hex data.
    May be multiline.
    0011 or
    00 11 or
    0 0 1 1 or even
    00 1 1
    Doesn't matter.
field 1
    value 1
field 2
    value 2
    
# следующий тест
# обязательно через пустую строку
hex
    00 11 11 00 11 22 33
    11 00 af 22 00 11 0f
a
    11 00
b
    af 22 00 11
c
    0f

```
 
+ расширение файла *.anq
+ hex должен быть обязательно
+ пробелов в начале должно быть не обязательно 4
  + нет пробелов - имя поля
  + хоть один пробел - данные
+ пустые строки разделяют тесты
 
нифига про безопасность не знаю</br>
баги можно не искать - сами вылезут 

*&copy; Slava Vikharev 2016*
