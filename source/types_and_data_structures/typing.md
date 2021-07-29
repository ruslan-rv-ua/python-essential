Мови програмування по типізації прийнято ділити на два великих табори — типізовані і нетипізовані (бестипові). До першого наприклад належать C, Python, Scala, PHP і Lua, а до другого — мова асемблера, Forth і Brainfuck.

Так як «бестипова типізація» по своїй суті дуже проста, далі вона ні на які інші види не ділиться. А ось типізовані мови разділяються ще на декілька категорій:




### Явна (explicit) і неявна (implicit) типізація

Явно-типізовані мови відрізняються тим, що тип нових змінних, функцій і їх аргументів треба задавати явно. Відповідно мови з неявною типізацією перекладають цю задачу на компілятор чи інтерпретатор.

Переваги явної типізації:

- Наявність у кожної функції сигнатури (наприклад int add(int, int)) дозволяє без проблем вивзначити, що функція робить.
- Програміст одразу ж записує, якого типа значення можутб зберігатись у конкретній змінній, що знижує необхідність запам'ятовувати це.

Переваги неявної типізації:

- Скорочення запису.
- Стійкість до змін. Наприклад якщо в функції тимчасова змінна була того ж типу, що і вхідний аргумент, то в явно типізованій мові при зміні типа вхідного аргумента потрібно буде змінити ще й тип тимчасової змінної.








### Статична (static) і динамічна (dynamic) типізація

Статична визначається тим, що кінцеві типи змінних і функцій встановлюються на етапі компіляції, в цей же момент відбувається перевірка типів. Тобто вже компілятор на 100% впевнений, який тип де знаходиться. В динамічній типізації усі типи з'ясовуються вже під час виконання програми. 

Зауважте, що неявна типізація не рівносильна динамічній, а явна — статичній.

Переваги статичної типізації:

- Перевірки типів відбуваються тільки один раз — на етапі компіляції. А це означає, що нам не треба буде постійно з'ясовувати, чи не намагаємось ми поділити число на рядок (і або видати помилку, або ж виконати перетворення).
- Швидкість виконання. З попереднього пункта ясно, що статично типізовані мови  практично завжди швидше динамічно типізованих.
- При деяких додаткових умовах дозволяє виявляти потенційні помилки вже на етапі компіляції.
- Прискорення розробки при підтримці IDE (відсіювання вариантів, які заздалегіть не підходять по типу).

Переваги динамічної типізації:

- Простота створення універсальних колекцій.
- Зручність опису узагальнених алгоритмів (наприклад сортування масива, яке буде працювати не тільки на списках цілих чисел, але і на списках символьних рядків).
- Легкість в освоєнні — мови з динамічною типізациєю зазвичай дуже непогані для того, щоб почати програмувати.




### Сильна (сувора, strong) і слабка (несувора, weak) типізація

Сильна типізація виділяється тим, що мова не дозволяє змішувати у виразах різні типи і не виконує автоматичні неявні перетворення, наприклад не можна відняти з рядка множину. Мови зі слабкою типізацією виконують багато неявних перетворень автоматично, навіть якщо може відбутись втрата точності або перетворення неоднозначне.

Слабку типізацію часто плутають з динамічною, що зовсім неправильно. Динамічно типізована мова може бути і слабо і сильно типізована.

Переваги сильної типізації:

- Надійність — ви отримаєте вийняткову ситуацію або помилку компіляції, на противагу неправиьлної поведінки.
- Швидкість — замість прихованих перетворень, котрі можуть бути доволі затратними, з сильною типізацією необхідно писати їх явно, що заставлє програміста як мінімум знати, що ця ділянка кода може бути повільним.
- Розуміння роботи програми — знову ж таки, замість неявного приведення типів, програміст пише усе сам, отже хоча б приблизно розуміє, що порівняння тядка і числа виконується не само по собі і не чарівним способом.
- Визначеність — коли ви пишете перетворення вручну ви точно знаєте, що ви перетворюєте і в що саме. Також ви завжди будете розуміти, що такі перетворення можуть призвести до втрати точності і до невірних результатів.

Переваги слабкої типізації:

- Зручність використання змішаних виразів.
- Абстрагування від типізації і зосередженість на задачі.
- Скорочення запису








### Класифікація деяких мов програмування

|мова|типізація|
|-|-|
|Python|динамічна сильна неявна|
|JavaScript|динамічна слабка неявна|
|Ruby|динамічна сильна неявна|
|Java|статична сильна явна|
|PHP|динамічна слабка неявна|
|C|статична слабка явна|
|C++|статична слабка явна|
|Perl|динамічна слабка неявна|
|Objective-C|статична слабка явна|
|C#|статична сильна явна|
|Haskell|статична сильна неявна|
|Common Lisp|динамічна сильна неявна|
|D|статична сильна явна|
|Delphi|статична сильна явна|
|-|-|














## Додаткові матеріали

- [Система типов](https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_%D1%82%D0%B8%D0%BF%D0%BE%D0%B2)
- [типизации](http://progopedia.ru/typing/)



<!-- https://habr.com/post/161205/ -->