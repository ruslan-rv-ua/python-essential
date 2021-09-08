# Булевий тип даних

Має усього два значення: `False` та `True`. 

Тип `bool` успадковано від `int`: 

    :::python
    >>> bool.mro()
    [<class 'bool'>, <class 'int'>, <class 'object'>]
    >>>

Успадковуватись від `bool` не можна: 

    :::python
    >>> class A(bool):pass
    ...
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: type 'bool' is not an acceptable base type
    >>>

Літералам `False` та `True` відповідають цілі числа `0` і `1`. 

    :::python
    >>> True == 1
    True
    >>> True is 1
    <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
    False
    >>> True * 7
    7
    >>>

## Створення об'єктів

- за допомогою літералів
- bool() без аргументів повертає `False`

## Приведення інших типів до `bool`

    bool(x)

Функція повертає `False` у наступних випадках: 

- якщо у об'єкта `x` визначено метод `__bool__()` і він повертає `False`
- якщо у об'єкта `x` визначено метод `__len__()` і він повертає `0`
- якщо значення `x` числового типу дорівнює нулю (0, 0.0, 0j, ...)
- якщо об'єкт `x` — пустий контейнер (list, str, tuple, dict, ...)
- якщо значення об'єкта `x` — одне з `None` чи `False`

У всіх інших випадках результатом функції буде `True`.

    :::python
    >> bool(0)
    False
    >>> bool(1)
    True
    >>> bool('string')
    True
    >>> bool('')
    False
    >>> bool()
    False
    >>> class MyClass:          f):
    ...     def __bool__(self):::::
    ...         return False
    ...
    >>> c = MyClass()
    >>> bool(c)
    False
    >>> class AlwaysTrue: pass
    ...
    >>> c = AlwaysTrue()
    >>> bool(c)
    True
    >>>

### Булевий контекст

Значення об'єктів можна розглядати як 
істині (truthy) і хибні (falsy). 

- `x` є falsy, якщо `bool(x)==False`
- `x` є truthy, якщо `bool(x)==True`

Коли ми використовуємо значення у логічних виразах 
або при перевірці умов в інструкціях `if` та `while`, 
ми використовуємо їх у ***булевому контексті***. 

Приклад. Функції передається непустий список цілих чисел. 
Функція виводить лише парні числа з цього списка. 

    :::python
    def print_even(data):
        if not data: # if len(data) == 0:
            raise ValueError("The argument data cannot be empty")
        for value in data:
            if not value % 2: # if value % 2 == 0:
                print(value)


## Логічні операції

Оператори у порядку збільшення пріорітету: 

|Операція|Результат|
|-|-|
|`x or y`|`y` якщо `bool(x) is False`, інакше `x`|
|`x and y`|`x` якщо `bool(x) is False`, інакше `y`|
|`not x`|`Ture` якщо `bool(x) is False`, інакше `False`|

Приклади: 

    :::python
    >>> 7 or 5
    7
    >>> 'string' or None
    'string'
    >>> None or 'string'
    'string'
    >>> def f(list_=None): # аргумент з дефолтним значенням [] мутабельного типу — не найкраща ідея, тому None
    ...     new_list = list_ or []
    ...     return new_list
    ...
    >>> f()
    []
    >>> f([1,2])
    [1, 2]
    >>>
    >>> 7 and 5
    5
    >>> 'string' and False
    False
    >>> False and 'string'
    False
    >>>

Оператор `not` має нижчий пріорітет ніж інші "нелогічні" оператори. 
Тому вираз 

    not a == b
    
інтерпретується як

    not (a == b)
    
Наступний вираз: 

    a == not b
    
не є коректним і призведе до `SyntaxEroor`. 

### "Ліниві" логічні обчислення

Операція `or` є "лінивою". 
Значення другого операнда обчислюється лише тоді, коли перший операнд є falsy: 

    :::python
    >>> l = [1, 2]
    >>> l.pop() or l.pop()
    2
    >>> l
    [1]
    >>> l = [1, 0]
    >>> l.pop() or l.pop()
    1
    >>> l
    []
    >>>

Операція `and` є "лінивою". 
Значення другого операнда обчислюється лише тоді, коли перший операнд є truthy: 

    :::python
    >>> l = [1, 0]
    >>> l.pop() and l.pop()
    0
    >>> l
    [1]
    >>> l = [1, 2]
    >>> l.pop() and l.pop()
    1
    >>> l
    []
    >>>

## Операції порівняння

Усього в Python є вісім операцій порівняння. 
Усі операції порівняння мають однаковий пріорітет. 
У операцій порівняння пріорітет вищий ніж у логічних операцій. 

|Операція|Що означає|Спеціальний метод|
|-|-|-|
|<|строго меньше|`__lt__()`|
|<=|меньше або дорівнює|`__le__()`|
|>|строго більше|`__gt__()`|
|>=|більше або дорівнює|`__ge__()`|
|==|дорівнює|`__eq__()`|
|!=|не дорівнює||
|is|ідентичне||
|is not|неідентичне||

Об'єкти різних типів, за винятком числових, при порівнянні на рівність завжди дають `False`. 

    :::python
    >>> [1,2] == '12'
    False
    >>> 1 == 1.0
    True
    >>>

Об'єкти одного класа за замовчуванням не рівні між собою: 

    :::python
    >>> class MyClass:
    ...     def __init__(self, value):
    ...             self.value = value
    ...
    >>> c1 = MyClass(1)
    >>> c2 = MyClass(1)
    >>> c1 == c2
    False
    >>>

Для порівняння на рівність клас має реалізувати відповідний магічний метод: 

    :::python
    >>> class MyClass:
    ...     def __init__(self, value):
    ...             self.value = value
    ...     def __eq__(self, other):
    ...             return self.value == other.value
    ...
    >>> c1 = MyClass(1)
    >>> c2 = MyClass(1)
    >>> c1 == c2
    True
    >>>

Щоб об'єкти одного класа можна було впорядкувати (наприклад, відсортувати), 
клас має реалізувати відповідні магічні методи: 
`__lt__(), __le__(), __gt__() і __ge__()`. 
Але, як правило, достатньо щоб клас реалізував `__lt__()` та `__eq__`. 

    :::python
    >>> class V:
    ...     def __init__(self, value):
    ...         self.value = value
    ...     def __eq__(self, other):
    ...         return self.value == other.value
    ...     def __lt__(self, other):
    ...         return self.value < other.value
    ...     def __repr__(self):
    ...         return f'{self.__class__.__name__}({self.value})'
    ...
    >>>
    >>> v1 = V(1)
    >>> v2 = V(1)
    >>> v3 = V(2)
    >>> l = [V(777), v3, v2, v1, v3]
    >>> l
    [V(777), V(2), V(1), V(1), V(2)]
    >>> l.sort()
    >>> l
    [V(1), V(1), V(2), V(2), V(777)]
    >>>

Поведінка `is` та `is not` не може бути перевизначена. 
Ця операція працює з об'єктами будь-яких класів і ніколи не піднімає винятків. 

    :::python
    >>> a=1
    >>> s='s'
    >>> a is s
    False
    >>>

### Згортання операцій порівняння

Наступний вираз:

    x < y <= z

є еквівалентом виразу:

    x < y and y <= z
    
Зауважте: значення `y` обчислюється лише один раз. 
