# Життєвий цикл об'єкта

## Час життя Python-об'єкта

При створенні екземпляра класа Python створює в пам'яті відповідний об'єкт. 
Пригадаємо основні характеристики об'єкта:

- значення (дані, стан об'єкта)
- тип даних
- ідентифікатор

Для знищення об'єктів Python використовує алгоритм підрахунку посилань. Об'єкти видаляються як тільки на них більше немає посилань.

В Python змінні не зберігають значення, а виступають в ролі посилань на об'єкти. 
Тобто коли ви присвоюєте значення новій змінній, то спочатку створюється об'єкт з цим значенням, а вже потім змінна починає посилатись на нього. На один об'єкт може посилатись багато змінних.

У Python-об'єкта є ще одна характеристика — лічильник посилань на об'єкт (reference counter). 
Як тільки хтось посилається на об'єкт, лічильник посилань збільшується на 1. Якщо з будь-якої причини посилання пропадає, то це поле зменшується на 1.

Приклади, коли кількість посилань збільшується:

* оператор присвоєння
* передача аргументів
* вставка нового об'єкта в `list` (збільшується кількість посилань для об'єкта)
* вираз виду `foo = bar` (`foo` починає посилатись на той самий обєкт, що і `bar`)

В інтрерпретаторі Python є спеціальний механізм — збиральник сміття (garbage collector). 
Спрощено це працює так: у певні моменти часу збиральник сміття "пробігається" по усім об'єктам в пам'яті, 
і якщо лічильник посилань певного об'єкта дорівнює 0, то цей об'єкт знищується — пам'ять, яку займав об'єкт, звільняється і у подальшому може використовуватись повторно. 

Якщо видалений об'єкт містив посилання на інші об'єкти, то ці посилання також видаляються. Таким чином, видалення одного об'єкта може спричинити видалення інших.

Наприклад, якщо видаляється список, то лічильник посилань у всіх його элементах зміншується на 1. Якщо усі об'єкти всередині списка більше ніде не використовуються, то їх тетакож будеь видалено.

Змінні, які оголошено поза функціями, називаются глобальными. Як правило, життєвий цикл таких змінних дорівнює життю Python-процеса. Таким чином, кількість посилань на об'єкти на котрі посилаються глобальні змінні ніколи не падає до 0.

Змінні, котрі оголошено всередині функції, мають локальну видимість. Як тільки інтерпретатор виходить з функції івн знищує усі посилання створені локальними змінними всередині неї. 

Дізнатись кількість посилань на об'єкт можна за допомогою функції getrefcount з модуля sys:

	>>> from sys import getrefcount
	>>> list1 = []
	>>> getrefcount(list1)
	2
	>>>
	
На список є два посилання:

1. змінна `list1`
1. у момент виклику `getrefcount()` їй передається аргумент, це теж посилання

## Список атрибутів об'єкта

В Python є вбудована функція `dir()` за допомогою якої можна отримати список імен усіх атрибутів об'єкта 
у вигляді списка. 
Оскільки "в Python все є об'єкт" функції `dir()` можна передати практично будь-яку сутність, 
будь то клас, екземпляр класа, модуль чи навіть функція: 

	:::python
	>>> import math
	>>> dir(math)
	['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
	>>> 'cos' in dir(math)
	True
	>>>

## Спеціальні атрибути

Атрибути, імена яких починаються і закінчуються двома знаками підкреслення, 
є "внутрішніми" для Python. 
Вони задають особливі властивості об'єктів. 

Приклади імен таких атрибутів:

- `__doc__`
- `__class__`
- `__init__`
- `__bool__`


Серед спеціальних атрибутів є як дані, так і методи. 
У документації Python такі методи називаються "метод зі спеціальними іменами", 
однак у спільноті розробників найчастіше такі методи називають: 

- магічний метод (magic method) 
- спеціальний метод (special method) 
- dunder method (від англ. Double UNDERscore — подвійний знак підкреслення)

Спеціальні методи задають особливу поведінку об'єктів і як правило не викликаються напряму. 
Їх викликає «у потрібні моменти часу» інтерпретатор. 
Але при створенні класа ми можемо визначити свій власний спеціальний метод, іншими словами перевизначити метод. Це дозволяє, наприклад, змінити поведінку вбудованих функцій і операторів для екземплярів певного класа. 


Коли ви створюєте власний клас, а потім екземпляр цього класа, 
то щойно створений екземпляр вже буде мати певну кількість атрибутів з подібними іменами:

	:::python
	>>> class SomeClass:
	...     pass
	...
	>>> obj = SomeClass()
	>>> dir(obj)
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
	>>>

Звідки беруться усі ці спеціальні атрибути ми дізнаємось у подальшому.

Не слід створювати свої власні (нестандартні) спеціальні атрибути!

## Життєвий цикл екземпляра класа

При створенні екземпляра класа інтерпретатор автоматично викликає послідовно два спеціальних метода: 
`__new__` та `__init__`. 
На іншому кінці життєвого цикла об'єкта знаходиться метод `__del__`. 
Давайте детальніше розглянемо ці три магічних метода. 

### `__new__(cls, [...])`

Це перший метод, який буде викликано при створенні об'єкта. 
Власне це і є "створювач" екземплярів класа. 
В парадигмі ООП такий метод називається конструктором. 

Конструктор приймає в якості параметрів клас і потім будь-які інші аргументи, 
які було вказано при створенні екземпляра. 
Наприклад:

	x = SomeClass(10, 'foo')
	
Конструктору буде передано: 

- клас SomeClass
- значення 10 типу int
- значення 'foo' типу str

Усі аргументи у подальшому буде передано спеціальному методу `__init__()`. 

В Python конструктор перевизначається вкрай рідко, лише для вирішення певних спеціальних задач. 

### `__init__(self, [...)`

Ініціалізатор класа. 
Йому передається екземпляр класа а також усе, з чим було викликано конструктор. 

Ініціалізатор майже повсемістно використовується при визначенні класів. 
Майже завжди цей метод помилково називають конструктором. 

### `__del__(self)`

Викликається при знищенні екземпляра. 
В парадигмі ООП такий метод називається деструктором. 

Деструктор не визначає поведінку для оператора `del`. 
Він визначає поведінку об'єкта у той час, коли за об'єкт береться збиральник сміття. 
Тому наступні рядки коду не є еквівалентними: 

	del x
	x.__del__()

<!--
Це може бути доволі зручно для об'єктів, які можуть потребувати додаткових "чисток" під час видалення, наприклад сокети чи файлові об'єкти. 
Однак пам'ятайте, що `del` не може слугувати заміною для хороших програмістських практик. 
Завжди завершуйте з'єднання, якщо закінчили з нми працювати і так далі! 
-->
Фактично, через відсутність гарантії виклику у визначений момент, 
деструктор в Python не повинен використовуватись майже ніколи. 
Використовуйте його з обережністю! 
