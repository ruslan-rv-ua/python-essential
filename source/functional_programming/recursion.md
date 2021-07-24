# Рекурсія

*Замість епіграфу: щоб зрозуміти рекурсію треба спочатку зрозуміти рекурсію.*

> ***Рекурсія*** — випадок, коли функція викликає сама себе. 

### Стек викликів

> ***стек викликів (call stack)*** — це структура даних у вигляді стека, яка зберігає інформацію про активні підпрограми комп'ютерної програми. Такий тип стека також відомий під назвами стек виконання, стек управління або рантайм стек, часто скорочується до просто "стек". Хоча підтримка функціонування стека викликів дуже важлива для будь-якої програми, деталі роботи зі стеком зазвичай приховані під час роботи з високорівневими мовами програмування. 

Стек викликів використовується для декількох пов'язаних цілей, але головне його призначення — відслідковувати точку повернення з кожної активної підпрограми, тобто адресу інструкції куди має бути повернуте виконання після завершення підпрограми. (Активними підпрограмами вважаються такі, що були виликані, але ще не завершили виконання поверненням.) 

	:::python
	def a(param):
		return b(param)
		
	def b(param):
		return c(param)
		
	def c(param):
		return 1 / param

	a(0)
	
У зв'язку з тим, що стек викликів влаштований як стек, підпрограма, що викликає заштовхує адресу повернення на верхівку стека, а підпрограма яку викликають, після завершення своєї роботи, виштовхує адресу повернення зі стека і повертає керування інструкції за цією адресою. Якщо підпрограма, яку викликали викликає іншу підпрограму або рекурсивно саму себе, тоді вона заштовхує наступну адресу повернення на верхівку стека, і т.д. Якщо розмір стека поглинає увесь виділений під стек простір, тоді виникає помилка ***переповнення стека*** (stack overflow), яка зазвичай призводить до краху програми. Додавання запису про підпрограму іноді називається ***намотування*** (winding); відповідно, видалення запису — ***розмотування*** (unwinding). 

Стек викликів може мати додаткові призначення, залежно від мови програмуання і архітектури комп'ютера. Серед них можуть бути: 

* Локальне сховище даних – Підпрограма часто потребує пам'ять для збереження значень локальних змінних, змінних значення яких відомі тільки під час виконання підпрограми і не зберігаються по виході з неї. Часто буває зручно виділяти для таких змінних місце просто рухаючи верхівку стека достатньо, щоб забезпечити необхідний простір. Це дуже швидке рішення у порівнянні з розташуванням в купі. Зауважимо, що кожна окрема підпрограма має свій окремий простір у стеку для локальних змінних.
* Передача параметрів – Підпрогами часто вимагають від коду, що їх викликає параметри, і розташування значень цих параметрів у стеку не є незвичним рішенням. Якщо параметрів всього декілька і їхній розмір малий, тоді для передачі їх в підпрограму можна використати регістри процесора, але якщо розмір парамерів не дозволяє зужиткувати цей спосіб передачі, буде необхідний простір в пам'яті. Стек добре працює для передачі таких параметрів, особливо через те, що з кожним викликом наступної підпрограми значення параметрів змінюються, щоразу для них виділяється окреме місце.
* Стек обчислення – Операнди арифметичних або логічних операцій зазвичай розташовують в регістрах і тоді провадять над ними певні дій. Однак, в деяких ситуаціях операнди можуть накопичуватися до довільної глибини, тоді постає питання використання чогось відмінного від регістрів. Стек подібних операндів, скоріше схожий на RPN калькулятор, називається стеком обчислення, і може розташовуватися у стеку викликів.
* Вказівник на поточний об'єкт - Деякі об’єктозорієнтовані мови програмування (наприклад, C++),при виклику функції зберігають вказівник this разом з аргументами функції у стеку. Вказівник this вказує на об'єкт пов'язаний з методом, що викликається.

та інші.





### Рекурсивні виклики функцій



Рекурсі буває:

* **проста**, коли функція викликає сама себе безпосередньо
* **непряма** або складна, коли функція викликає себе через іншу функцію, наприклад функція A викликає функцію B, а функція B викликає функцію A.

Кількість вкладених викликів функції називають *глибиною рекурсії*.

Реалізація рекурсивних викликів функцій у мовах програмування, за правило, опирається на механізм стека викликів — адреса повернення і локальлні
змінні функції, записуються у стек, завдяки чому кожен наступний
рекурсивний виклик цієї функції використовує свій набір локальлних змінних  і
за рахунок цього працює корректно. Оборотною стороною цього досить простого по
структурі механізму є те, що на кожен рекурсивний виклик потрібно
деяка кількість оперативної пам'яті комп'ютера, і при надвеликій
глибині рекурсії може статися переповнення стека викликів.

Рекурсивна програма дозволяє описувати обчислення, які повторюються, або ж навіть потенційно нескінченні обчислення, без явних повторів частин програми і
використання циклів.

Щоб рекурсія не стала "вічною" функція повинна мати *умову виходу*. Тобто умову, при виконанні якої функція повертає якийсь результат.

Розглянемо використання рекурсії на практиці.

## Обчислення факторіалу

Факторіал натурального числа `n`  — добуток натуральних чисел від одиниці до `n`  включно, позначається  `n!`.

Функцію обчислення факторіалу можна записати наступним способом:

> F(1) = 1  
> F(n) = n*F(n-1), n>1

Запишемо вищенаведене мовою Python:

	:::python
	def factorial(n):
		if n == 1: # умова виходу
			return 1
		else:
			return n * factorial(n-1)

## Числа Фібоначчі

Числа Фібоначчі — послідовність натуральних чисел, перші два члени якої — одиниці, а кожний наступний — сума значень двох попередніх чисел.

	1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, … 

Формально послідовність можна відобразити так:

> F(1) = 1  
> F(2) = 1  
> F(n) = F(n-1) + F(n-2), n>=2

Нам залишається тільки записати формальне відображення мовою Python:

	:::python
	def fib(n):
		if n == 1 or n == 2:
			return 1
		else:
			return fib(n-1) + fib(n-2)

Зауважимо, що такий алгоритм знаходження послідовності Фібоначчі не є ефективним, оскільки числа обчислюються декілька раз. Наприклад, якщо ми хочемо знайти число Фібоначчі з номером 5, то виклик функції `fib()` буде таким:

	fib(5)
		fib(4)
			fib(3)
				fib(2)
				fib(1)
			fib(2)
		fib(3)
			fib(2)
			fib(1)
		
Нескладно підрахувати, що функція `fib()`:

- з аргументом 2 викликалась 3 рази
- з аргументом 3 викликалась 2 рази
- з аргументом 1 викликалась 2 рази
- з аргументом 4 викликалась 1 раз
- з аргументом 5 викликалась 1 раз

Тобто усього було 9 викликів!

А чи можна зробити так, щоб уникнути повторних обчислень? Можна! Якщо ми будемо запам'ятовувати значення, які функція порахувала для певних аргументів, то ми можемо уникнути повторних рекурсивних викликів. Прийом називається "мемоізація".

> ***Мемоизация*** (memoization, запам'ятовування) — збережежння результатів виконання функцій для запобігання повторних обчислень. Це один з способів оптимізації, який застосовується для збільшення швидкості виконання комп'ютерних програм. 

Перед викликом функції перевіряється, чи викликалась функція раніше: 

- якщо не викликалась, функція викликається і результат її виконання зберігається;
- якщо викликалась, використовується збережений результат.

Найзручніше реалізувати мемоізацію за допомогою декоратора. Напишемо декоратор, який мемоізує конкретно нашу функцію, яка приймає лише один аргумент:

	:::python
	def memoize(f):
		def wrapper(n):
			if n not in wrapper.memo:
				wrapper.memo[n] = f(n)
			return wrapper.memo[n]
		wrapper.memo = {}
		return wrapper

	@memoize
	def fib(n):
		return fib(n-1) + fib(n-2) if n > 2 else 1
		
Тепер обчислення виконуються набагато швидше! Для прикладу знаходження 5-го числа Фібоначчі послідовність виклику функції `fib()` буде таким:

	fib(5)
		fib(4)
			fib(3)
				fib(2)
				fib(1)

Бібліотека Python вже має декоратор для мемоізації функцій, він знаходиться у модулі `functools`:

	:::python
	@lru_cache(maxsize=5)
	def fib(n):
		return fib(n-1) + fib(n-2) if n > 2 else 1



Взагалі питання про доцільність використання рекурсивних функцій у програмуванні неоднозначне: з одного боку, рекурсивна форма може бути структурно простіша і наочніше, особливо коли сам алгоритм, який треба реалізувати, по своїй суті рекурсивний. З іншого боку зазвичай рекомендується уникати рекурсивних програм, котрі призводять (або у деяких умовах можуть призводити) до занадто великої глибини рекурсії.

## «Ханойські вежі»

Однією з класичних задач, де рекурсія проявляється у всій своїй красі, є задача про Ханойські вежі.

Одна із прадавніх легенд говорить: «У непрохідних джунглях недалеко від міста Ханоя є храм бога Брами. У ньому перебуває бронзова плита із трьома алмазними стрижнями. На один зі стрижнів бог при створенні миру нанизав 64 диски різних діаметрів із чистого золота. Найбільший диск лежить на бронзовій плиті, а інші утворюють піраміду, що зужується догори. Це вежа Брами. Працюючи день і ніч, жерці храму переносять диски з одного стрижня на інший, дотримуючись законів Брами:  
1) диски можна переміщати з одного стрижня на іншій тільки по одному;  
2) не можна класти більший диск на менший;  
3) не можна відкладати диски убік, при переносі дисків з одного стрижня на інший можна використовувати проміжний третій стрижень, на якому диски повинні перебувати теж тільки у вигляді піраміди, що зужується догори.  
Коли всі 64 диска будуть перенесені з одного стрижня на інший, настане кінець світу».

Ця прадавня легенда покладена в основу завдання про Ханойську вежу: перемістити n дисків зі стрижня 1 на стрижень 3, використовуючи проміжний стрижень 2 дотримуючись законів Брами. 

Давайте спробуемо знайти алгоритм вирішення цієї задачі.

Якщо вежа складається з одного диска, то він переноситься за один хід: 1-3. 

Вежа із двох дисків переноситься за три ходи: 1—2, 1-3, 2-3. 

Для переносу вежі із трьох дисків буде потрібно вже сім ходів: 1-3, 1-2, 3-2, 1-3, 2-1, 2-3, 1-3. Зверніть увагу, за перші три ходи ми переносимо вежу із двох верхніх дисків на другий проміжний стрижень. Потім переносимо найбільший диск із першого стрижня на третій і ще раз проробляємо добре знайому нам операцію: переносимо вежу із двох дисків на третій диск. 

Отже, щоб перенести вежу із чотирьох дисків з першого стрижня на третій, необхідно діяти за планом: 

1. перенести вежу із трьох верхніх дисків з першого стрижня на другий (7 ходів);
1. найбільший диск перенести з першого стрижня на третій (1 хід); 
1. перенести вежу із трьох дисків із другого стрижня на третій (7 ходів).

Усього на перенос буде потрібно 15 ходів. 

Міркуючи аналогічним образом, порахуємо число ходів, необхідних для переносу вежі з п'яти дисків: 15 + 1 + 15 = 2 * 15 + 1 = 31. 

Для вежі з 6 дисків одержуємо: 2 * 31 + 1 = 63 і т.д. 

Розглянутий нами алгоритм рішення завдання «Ханойська вежа» має одну дивну властивість: у ході його виконання для вежі, що полягає з `n` дисків, ми використовуємо алгоритм для трохи більш простої ситуації — переносу вежі, що полягає з `n-1` дисків. У свою чергу, в алгоритмі для вежі з 'n-1' дисків використовується цей же алгоритм для `n-2` дисків і т.д. 

Давайте сформулюємо задачу: 

- є три стрижні умовно позначені `1`, `2`, `3`.
- на стрижні `1` знаходиться піраміда з `n` дисків
- треба перекласти піраміду зі стрижня `1` на стрижень `3` користуючись стрижнем `2` як допоміжним

Алгоритм вирішення буде таким:

- якщо на стрижні `1` лише один диск, то перекладаємо його на стрижень `3`, інакше:
* перекласти `n-1` дисків зі стрижня `1` на допоміжний стрижень `2`
* перекласти один диск зі стрижня `1` на стрижень `3`
* перекласти піраміду з `n-1` дисків зі стрижня `2` на стрижень `3` користуючись стрижнем `1` як допоміжним  

``

	:::python
	def hanoi(n, s1, s2, s3):
		if n == 1:
			print(s1, '-', s3) # просто перекласти 1 диск
		else:
			# перекласти `n-1` дисків зі стрижня `1` на стрижень `2`
			# користуючись стрижнем `3` як допоміжним
			hanoi(n-1, s1, s3, s2)
			# перекласти 1 диск
			print(s1, '-', s3)
			# перекласти `n-1` дисків зі стрижня `2` на стрижень `3`
			# користуючись стрижнем `1` як допоміжним
			hanoi(n-1, s2, s1, s3)
			
Цей код можна зробити трохи "компактнішим":

	:::python
	def hanoi(n, s1, s2, s3):
		if n != 0:
			hanoi(n-1, s1, s3, s2)
			print(s1, '-', s3)
			hanoi(n-1, s2, s1, s3)

Використовуємо:

	:::python
	>>> hanoi(1, '1', '2', '3')
	1 - 3
	>>> hanoi(2, '1', '2', '3')
	1 - 2
	1 - 3
	2 - 3
	>>> hanoi(3, '1', '2', '3')
	1 - 3
	1 - 2
	3 - 2
	1 - 3
	2 - 1
	2 - 3
	1 - 3
	>>>
	
	