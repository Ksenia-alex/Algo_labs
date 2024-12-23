# Задача 9 по выбору: поликлиника
___
Студентка ИТМО, Толстухина Ксения Александровна 467733

## Вариант 20
___

## Описание
Этот код обрабатывает команды для работы с очередью в поликлинике, 
читает входные данные из файла, выполняет операции добавления и 
удаления элементов, записывает результаты в выходной файл 
и выводит информацию о времени работы и затраченной памяти программы.

## Структура проекта
- `Task9/` - папка со всеми файлами для номера
- `src/` — исходный код программы.
- `tests/` - тесты для проверти работы
- `txtf/` - папка с файлами input.txt и output.txt
- `README.md`

## Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит одно число n (1 ≤ n ≤ 10^5) — число команд.

## Формат выходных данных
- В выходном файле output.txt должны содержаться числа, 
которые удаляются из очереди с помощью команды “–”, 
по одному в каждой строке.


## Input/Output
| input                                                                       | output                            |
|-----------------------------------------------------------------------------|-----------------------------------|
| 7  <br/>+ 1  <br/>+ 2 <br/> - <br/> + 3 <br/> + 4 <br/> - <br/> -           | 1 <br/> 2 <br/> 3                 |
| 10  <br/>+ 1  <br/>+ 2 <br/>* 3 <br/> - <br/> + 4 <br/> * 5 <br/> - <br/> -<br/> - <br/> - | 1 <br/> 3 <br/> 2 <br/> 5 <br/> 4 |


## Запуск проекта
1. Клонируйте репозиторий:
```bash
git clone https://github.com/Ksenia-alex/Algo_labs
```

2. Перейдите в папку проекта
```bash
cd Algo_labs/lab4/Task9
```

3. Запустите тесты из tests
