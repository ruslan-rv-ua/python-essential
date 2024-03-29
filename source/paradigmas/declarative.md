---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

> ***Декларативне програмування*** — це парадигма програмування, відповідно до якої програма деяким чином описує що потрібно отримати як результат, а не як це треба зробити.
 
Тому декларативне програмування часто називаютьописовим. 
Тут головним є чітке формулювання мети і результатів роботи задачі, а не послідовність отримання цього результату. Вибір і застосування необхідного для вирішення задачі алгоритму — проблема виконуючої системи (алгоритм роботи з даними "зашитий" в неї).

Так, декларативними є:
- опис web-сторінок на HTML — вони описують, що містить сторінка та що має відображатись (заголовок, шрифт, текст, зображення), але не містять інструкцій як її слід відображати; 
- опис SQL-запитів, які конкретизують властивості даних, які слід отримати від бази даних, але не процес отримання цих даних; 
- опис XML-документів тощо.

Такий підхід має високий ступінь абстракції і легко формалізується математичними засобами. Фактично програміст оперує не набором інструкцій, а абстрактними поняттями, часто досить узагальненими.

Декларативні мови найкраще використовувати у випадках, коли "дані управляють програмою": 
при написанні експертних систем, при конструюванні трансляторів з мов програмування, для більшості задач штучного інтелекту. Саме там їх використання призводить до найбільшої ефективності.

Різновидами декларативного програмування є функціональне та логічне програмування.

## Функціональне програмування

> ***Функціональне програмування*** — це підхід до побудови програм, який грунтується на абстракції математичної функції і передбачає, що програма є сукупністю визначень математичних функцій, а її виконання полягає в обчисленні відповідних виразів. 

При цьому функції можуть визначатися через інші функції 
(як композиція3 функцій) або рекурсивно (через самих себе). 
У процесі виконання програми функції отримують параметри, обчислюють і повертають результат, у разі необхідності обчислюючи значення інших функцій. 

Слід зазначити, що існують відмінності в розумінні математичної функції у функціональному програмуванні і функції в процедурному програмуванні. Зокрема, функція в математиці не може змінити викликаючого її оточення і запам'ятати результати своєї роботи, а тільки надає результат обчислення функції. Тобто, у функційному програмуванні програму можна представити як обчислення послідовності функцій без станів. 

На відміну від імперативного програмування, де існує поняття поточного кроку виконання і поточного стану, що змінюється у часі, у функціональному програмуванні поняття часу відсутнє. Ще однією особливість функціональних мов є їх безтиповість (відсутність типів даних). 

Таким чином, функціональне програмування є способом створення програм, в яких єдиною дією є виклик функції, єдиним способом розбиття програми є створення нового імені функції та задання для цього імені виразу, що обчислює значення функції, а єдиною операцією, що використовується при визначенні функцій, — композиція функцій. Такий підхід дає можливість прозорого моделювання тексту програм математичними засобами. Основна специфіка функціональних мов програмування полягає в тому, що функції обмінюються між собою даними безпосередньо, тобто без використання проміжних змінних і присвоювань. 

До відомих функціональних мов програмування належить LISP (List Processing), що розглядається фахівцями як основна мова програмування систем штучного інтелекту, Mathematica (символьні обчислення), XSLT (XML), Haskell, Scheme та ін. 

Наприклад, обчислення факторіала числа на LISP: 

	:::lisp
	;; обчислення факторіала
	(define (fact n)
	(cond ((= n 1) 1)
	((> n 1) (* n (fact (- n 1))))))
	;; виведення значення 5!
	(print (fact 5))

Цей приклад використовує рекурсивне визначення факторіала. Вирази в LISP визначаються за дужками і можуть записуватися в кілька рядків. Визначення функції здійснюється з використанням `defun`. Математичні вирази записуються у префіксній формі, тобто вираз `а+b*x` має вид: `+(а,*(b,х)). Стандартна функція `cond` служить для організації умовного виконання, `print` — для виведення. 

Функціональне програмування застосовується для вирішення задач, які важко сформулювати в термінах послідовних операцій — переважно задач, пов'язаних з розпізнаванням образів, спілкуванням на природній мові, реалізацією експертних систем, автоматизованим доведенням теорем, символьними обчисленнями, тобто задач, які традиційно відносять до області штучного інтелекту. 

## Логічне програмування

> ***Логічне програмування*** — це підхід до побудови програм, який грунтується на логіці предикатів і передбачає, що програма являє собою опис відомостей про задачу (фактів), припущень, достатніх для її вирішення (правил виведення), і твердження, яке потрібно довести. Виконання програми полягає у доведенні цього твердження.

Факти (аксіоми) і правила виведення, які утворюють базу знань певної предметної області, виражаються в термінах предикатів. Твердження, яке вимагається довести, вводиться в програму як цільова функція. Виконання програми полягає у тому, щоб визначити за допомогою механізмів логічного виведення, чи витікає задане цільове твердження (запит) з наявних фактів і правил. Для виконання програми (логічного виведення результату) використовується вбудована система автоматичного пошуку. 

Таким чином, у логічній програмі має місце умовний поділ на дані (факти) і код (правила, запити). Але цей поділ досить умовний: факти, правила і запити мають одну і ту ж форму запису — у вигляді предикатної функції. 

Також слід зазначити, що програма на логічній мові програмування описує неалгоритм вирішення задачі, а логічну модель предметної області — деякі факти щодо властивостей предметної області і відношенняміж цими властивостями, а також правила виведення нових властивостей і відношень з уже заданих. Рішення задачі (отримання відповіді на запит) здійснються не шляхом виконання команд, а за допомогою механізмів керованого логічного виведення нових фактів на основі заданих фактів і правил виводу, які реалізуються програмною системою автоматично. 

<!--
Це свідчить про декларативність мови логічного програмування, яка влучно виражена у формулі Р.Ковальского: «алгоритм = логіка + керування». 
-->

Основне завдання програміста — вдало описати у вигляді системи логічних формул предметну область і таку множину відношень на ній, які з достатнім ступенем повноти описують задачу. 

Найбільш поширеною мовою логічного програмування є мова ***`PROLOG`*** (PROgramming in LOGic — програмування в термінах логіки). До мов логічного програмування також відносять Planner, Mercury, Fril та ін. 

Наприклад, на основі декількох аксіом про те, що полюбляє Мері і на основі пари правил робиться висновок про те, що полюбляє Бет:

	:::prolog
	predicates
	  nondeterm likes(symbol, symbol)
	  nondeterm fruit(symbol)
	  nondeterm color(symbol, symbol)
	   
	clauses
	  % що полюбляє Мері
	  likes(mary, pears).
	  likes(mary, popcorn).
	  likes(mary, apples).

	  % що полюбляє Бет
	  % Бет полюбляє те, що полюбляє Мері, якщо це фрукт і якщо він червоний
	  likes(beth, X):-likes(mary, X), fruit(X), color(X, red).
	  % Бет полюбляє те, що полюбляє Мері, якщо це кукурудза
	  likes(beth, X):-likes(mary, X), X=popcorn.

	  % дані
	  fruit(pears).  
	  fruit(apples).

	  color(pears, yellow).
	  color(oranges, orange).
	  color(apples, red).
	  color(apples, yellow).

Відповіддю на запит:
 
	:::prolog
	goal
	  likes(beth, apples).
	  
буде: 

	Yes
	
тобто істина (хоча в явному вигляді цього факту описано не було). 

Логічні програми відрізняються принципово низькою швидкодією, так як обчислення здійснюються методом проб і помилок (за допомогою пошуку з поверненнями). Однак, важливою перевагою такого підходу є достатньо високий рівень машинної незалежності, а також можливість відкатів — повернення до попередньої підцілі при негативному результаті аналізу одного з варіантів в процесі пошуку рішення (скажімо, чергового ходу при грі в шахи), що позбавляє від необхідності пошуку вирішення шляхом повного перебору варіантів і збільшує ефективність реалізації. 

<hr>

Декларативні мови найкраще використовувати у випадках, коли "дані керують програмою": при написанні експертних систем, при конструюванні трансляторів з мов програмування, для більшості задачштучного інтелекту. Саме там їх використання призводить до найбільшої ефективності. 




	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	











<!-- https://studfiles.net/preview/5994723/ -->