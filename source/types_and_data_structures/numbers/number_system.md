# Системи числення

Ми зазвичай ведемо рахунок десятками (10 одиниць утворює десятку, 10 десятків - сотню і т.д.), тобто ведемо рахунок у десятковій системі числення. Але існують і інші системи числення.

> Система числення — сукупність правил зображення чисел цифровими знаками. 

Розрізняють позиційні й непозиційні системи числення. 

У непозиційних системах числення вага знака не залежить від його положення по відношенню до інших знаків у числі. 
Наприклад у [римській системі числення](roman_numerals.md): 

- I - 1
- V - 5
- X - 10 і так далі. 

В одиничній системі числення число сім представляється сімома одиничками: (7)<sub>10</sub> = (1111111)<sub>1</sub>. 
Недоліками непозиційних систем числення є: 

- громіздкість зображення чисел; 
- труднощі у виконанні операцій.

Для позиційних систем числення характерні наочність зображення чисел і відносна простота виконання операцій. 

Система числення називається позиційною, якщо під час запису числа одна і таж цифра має різне значення, яке визначається місцем (позицією), на якому вона знаходиться. 

У позиційній системі для запису числа використовується обмежена кількість знаків - цифр, яка визначає назву системи числення і називається її основою. Араби взяли за основу число 10, тому що в якості обчислювального пристрою вони використовували 10 пальців рук. В десятковій системі для запису числа використовується десять цифр від 0 до 9 і основою є число 10. Число у цій системі числення можна представити у вигляді степенів десяти: 

> (237)<sub>10</sub> = 2*10<sup>2</sup>+3*10<sup>1</sup> + 7*10<sup>0</sup>

## Системи числення, що використовуються в комп'ютерах 

Система числення з основою N=2 є позиційною системою числення і нічим не відрізняється від позиційної система числення з будь-якою основою. Але для комп'ютера ця система числення має перевагу - її алфавіт має всього два символи. Тобто, для фіксації її символів достатньо мати деякий пристрій, що може мати два суттєво різних і стійких стани. 

Людині більш звична десяткова система, у якій відпрацьовані прийоми записування чисел по його імені, визначення імені по запису, визначення ваги числа по його запису й імені, відпрацьовані прийоми додавання, віднімання, множення й ділення будь-яких чисел. У двійковому записі числа важко одразу визначити його значення, немає поняття імені саме двійкового числа, важко зіставити ланцюжок 1 і 0 із його змістом. Таким чином виникає потреба перетворювати двійкові записи у десяткові і навпаки. 

Приклади: 

> (5)<sub>10</sub> = (101)<sub>2</sub>

У програмуванні вагоме місце займають вісімкова й шістнадцяткова системи числення, які використовуються для скороченого запису двійкових кодів. 

У вісімковій системі числення в якості цифр використовують цифри: 0, 1, 2, 3, 4, 5, 6, 7. В шістнадцятковій системі потрібно 16 символів, в якості яких використовують арабські цифри і п'ять букв латинського алфавіту, що утворюють послідовність: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, А, В, C, D, E, F. Десяткові еквіваленти символів A, B, C, D, E, F:

	A = 10, B = 11, C = 12, D = 13, E = 14, F = 15

<!--- https://www.ua5.org/osnprog/28-ponjattja-sistemi-chislennja.html  --->