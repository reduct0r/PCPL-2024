### Вариант 28Д
# Задание
  1. Необходимо разработать два класса данных, которые иллюстрируют предметную область, связанную отношениями один-ко-многим и многие-ко-многим. Примером могут служить классы «Сотрудник» и «Отдел», которые описаны ниже:
   
   - Класс «Сотрудник», который включает следующие поля:
     - ID записи о сотруднике;
     - Фамилия сотрудника;
     - Зарплата (количественный показатель);
     - ID записи об отделе (для реализации связи один-ко-многим).
   
   - Класс «Отдел», содержащий поля:
     - ID записи об отделе;
     - Наименование отдела.
   
   - Класс «Сотрудники отдела» (для связи многие-ко-многим), объединяющий:
     - ID записи о сотруднике;
     - ID записи об отделе.

2. **Создание списков объектов с тестовыми данными:**
   Создайте списки объектов этих классов с тестовыми данными (3-5 записей). Убедитесь, что первичные и вторичные ключи связаны по идентификаторам.

3. **Разработка запросов:**
   Запросы должны быть сформулированы в терминах вышеописанных классов. Используйте функциональные возможности языка Python для их реализации, включая list/dict comprehensions и функции высших порядков.
   
   - Для второго запроса вводится количественный признак, например, «зарплата сотрудника».

# Запросы
1. **Отношение один-ко-многим:**
   Выведите список сотрудников, фамилии которых заканчиваются на «ов», вместе с названиями их отделов.

2. **Средняя зарплата:**
   Отобразите список отделов с указанием средней зарплаты в каждом из них, отсортированный по этому показателю. (Необходимо использовать комбинацию функций вычисления суммы и количества значений, так как отдельной функции для среднего значения в Python нет).

3. **Отношение многие-ко-многим:**
   Перечислите отделы, чьи названия начинаются с буквы «А», и список сотрудников, работающих в них.

# Предметная область
Студенческая группа, Кафедра.
