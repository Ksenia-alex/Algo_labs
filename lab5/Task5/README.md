# Задача 5 по варианту: Планировщик заданий
___
Студентка ИТМО, Толстухина Ксения Александровна 467733

## Вариант 20
___

## Описание
Этот код обрабатывает входящие "задачи", кто будет делать и в какой время он начнет, 
читает входные данные из файла, записывает результаты в выходной файл 
и выводит информацию о времени работы и затраченной памяти программы.

## Структура проекта
- `Task5/` - папка со всеми файлами для номера
- `src/` — исходный код программы.
- `tests/` - тесты для проверти работы
- `txtf/` - папка с файлами input.txt и output.txt
- `README.md`

## Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит два числа n, m (1 ≤ n/m ≤ 10^5)
- Вторая строка m задач

## Формат выходных данных
- В выходном файле output.txt должны содержаться значения
  кто обрабатывал задачу и в какое время начал

## Ограничения
- Время выполнения: 6 секунд.
- Память: 512 МБ.

## Input/Output
| input                                      | output                                   |
|--------------------------------------------|------------------------------------------|
| 2 5  <br/>1  <br/>2 <br/>3  <br/>4  <br/>5 | 0 0 <br/>1 0 <br/>0 1  <br/>1 2 <br/>0 4 |


## Запуск проекта
1. Клонируйте репозиторий:
```bash
git clone https://github.com/Ksenia-alex/Algo_labs
```

2. Перейдите в папку проекта
```bash
cd Algo_labs/lab5/Task5
```

3. Запустите тесты из tests