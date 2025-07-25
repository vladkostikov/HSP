# Определение границ разрабатываемой системы (анализ)

### Что будет включено в систему:
Игровое поле с элементами\
Обработка пользовательского ввода и перестановка элементов\
Проверка и удаление комбинаций\
Генерация новых элементов для заполнения пустых мест\
Подсчёт очков\
Бонусы за сложные комбинации


### Что точно не будет включено в систему:
Графический интерфейс\
Мультиплеер\
Сохранение/загрузка прогресса

### Главные подсистемы:
Модуль управления игрой\
Модуль отображения игрового поля и элементов\
Модуль обработки ходов и проверки комбинаций\
Модуль статистики\
Модуль бонусов

### Пользовательские метафоры:
Игровое поле - сетка, в которой размещаются элементы.\
Элемент - базовая единица на поле, латинская буква.\
Ход - перестановка двух соседних элементов.\
Комбинация - три или более одинаковых элемента по прямой линии.\
Очки - числовая метрика, увеличивающаяся за создание комбинаций.\
Бонус - особое действие, активируемое за создание расширенных комбинаций.

### Функциональность:
Начало игры - отображение игрового поля с элементами.\
Ввод хода - пользователь вводит координаты двух элементов для перестановки.\
Обработка хода - проверка ввода на допустимость, поиск комбинаций.\
Реакция системы - исчезновение совпавших элементов, начисление очков, генерация новых элементов.\
Повторная проверка - поиск комбинаций и реакция системы, если образовались новые комбинации.\
Обработка бонусов - активация и применение дополнительных действий за создание комбинаций из 4+ элементов.\
Окончание игры - вывод статистики при отсутствии доступных ходов.

### Библиотеки повторного использования:
Рандомизатор для генерации случайных элементов.\
Ввод/вывод для взаимодействия с пользователем.\
Форматирование для модификации вывода.
