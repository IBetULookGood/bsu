# Задание 7

### Модели создания и функционирования потоков. Разработка многопоточных приложений на языке С++

[Хьюз, К. Параллельное и распределенное программирование с 
использованием C++ / К. Хьюз, Т. Хьюз. – М.: Вильямс, 2004. – 672с](https://github.com/IBetULookGood/bsu/blob/master/Parallel%20Systems%20(%D0%A0%D0%B0%D1%81%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%B8%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BB%D0%BB%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B)/lab_7/theory1.djvu)

4.5 Модели создания и функционирования потоков

4.11 Разбиение программы на несколько потоков

__Задание 7.1.__ Изучаем модель Производитель/Потребитель

__Задание 7.2__ Задача «reverse word». Задан текстовый файл. Каждое слово этого файла записать в выходной файл в обратном порядке букв. Написать последовательную программу.

[Галовиц Я. С++17 STL. Стандартная библиотека шаблонов. - СПб.: Питер, 2018. - 432с.](https://github.com/IBetULookGood/bsu/blob/master/Parallel%20Systems%20(%D0%A0%D0%B0%D1%81%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%B8%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BB%D0%BB%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B)/lab_7/theory2.pdf)

Глава 9. Параллелизм и конкурентность
+ Реализуем идиому «производитель/потребитель» с использованием std::condition_variable

__Глава 7.3.__ Параллельная реализация
+ Реализовать модель Производитель/Потребитель 1+1 в варианте Я.Галовица.
+ Выполнить вычислительные эксперименты для определения ускорения и эффективности параллельной программы.

__Отчет__
+ По заданию 7.2 - текст программы.
+ По заданию 7.3 - текст программ и таблица с результатами экспериментов.
+ Разместить на портале.