# "Підйом" винятків

Python автоматично генерує винятки при виникненні помилки під час виконання. 
Але також є можливість сгенерувати виняток програмно. 
Робиться це за допомогою ключового слова `raise`. 
Після нього вказують об'єкт винятка. 
При конструюванні екземпляра винятка зазвичай вказують повідомлення, 
яке більш детально описує проблему, 
а також деколи інші аргументи: 

	:::python
	>>> raise ZeroDivisionError('Вчіть математику!')
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ZeroDivisionError: Вчіть математику!
	>>>

Також можна вказати клас винятка, 
у цьому разі Python автоматично створить екземпляр класа викликавши відповідний конструктор без параметрів. 

	:::python
	>>> raise ZeroDivisionError
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ZeroDivisionError
	>>>

Зауважте, що `raise` може викидати у якості винятків тільки екземпляри класа `BaseException` 
і його похідних класів. 

## Створення власних винятків

При розробці програмного забезпечення, 
особливо якщо ви створюєте програмний продукт, 
який можуть використовувати інші розробники, 
може виникнути потреба створити власні винятки, 
які будуть обробляти якісь специфічні помилки. 
Хорошою практикою є створити базовий клас успадкувавши його від `Exception` або іншого стандартного, 
а вже потім від цього базового класа успадкувати класи для конкретних помилок чи ситуацій. 

Приклад визначення власних винятків і їх використання:

	:::python
	class CoolFrameworkException(Exception):
		pass
		
	class VeryRareError(CoolFrameworkException):
		pass
		
	class SomeStrangeError(CoolFrameworkException):
		pass
