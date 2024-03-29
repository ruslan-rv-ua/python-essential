При розробці Python-застосунків або використанні рішень на Python створених іншими розробниками може виникнути ряд проблем, пов'язаних з використанням бібліотек різних версій. 

1. Різні застосунки можуть використовувати одну і ту ж біблиотеку, 
але при цьому кожному застосунку потрібна бібліотека певної версії.
1. Може виникнути необхідність заборонити вносити зміни в застосунок на рівні бібліотек. 
Тобто ви встановили застосунок і хочете щоб він працював незалежно від того, поновлюються у вас бібліотеки чи ні. 
Як зрозуміло, якщо він буде використовувати бібліотеки з глобального сховища, 
то з часом можуть виникнути проблеми. 
1. У вас просто може не бути доступу до каталогу зі встановленими бібліотеками.

Для вирішення подібних ситуацій використовується підхід, 
який основано на побудові віртуальних оточень. 

> ***Віртуальне оточення*** — ізольоване оточення середовища (у нашому випадку це оточення Python), 
яке дозволяє використовувати певні версії застосунків. 

Іншими словами  — це своєрідна пісочниця, 
в межах якої запускається застосунок з своїми бібліотеками, 
поновлення і зміна яких не зачіпає інші застосунки, котрі використовують ті ж бібліотеки.

Вміння користуватись віртуальними оточеннями — неообхідна річ!

Програмне забезпечення, яке дозволяє створювати віртуальні оточення в Python 
можна розділити на ті, 
що входять у стандартну бібліотеку Python і зовнішні. 

***`virtualenv`***. 
Це, напевне, один з самих популярних інструментів для створення віртуальних оточень. 
Він простий у встановленні і використанні. 

***pyenv***. 
інструмент для ізоляції версій Python. 
Найчастіше використовується у випадках, коли на одній машині неообхідно мати декілька версій інтерпретатора для тестування ПЗ. 

***virtualenvwrapper***. 
Це обгортка для `virtualenv`. 
Дозволяє зберігати усі ізольовані оточення в одному місці. 
Надає зручний спосіб переключення між оточеннями і можливість розширювати функціонал за допомогою плагінів. 

***venv***. 
Цей модуль з'явився в Python 3 і його не може бути використано разом з Python 2. 
По своєму функціоналу дуже схожий на `virtualenv`. 
Якщо плануєте працювати з Python 3, то можете сміливо використовувати цей інструмент. 

### `venv`

Встановлювати `venv` не потрібно, він входить в стандартну бібліотеку Python. 
Зауважте: `venv` працює тільки в Python 3! 

Для створення віртуального оточення з іменем `env` виконуємо команду: 

	python -m venv .env
	
В результаті буде створено каталог `.env`. 
Разберемо детальніше його вміст. 

***`.venv/scripts/`*** — містить скрипти для активації/деактивації оточення, 
інтерпретатор Python, використовуваний в межах даного оточення, менеджер `pip` і ще декілька інструментів,  які забезпечують роботу з пакетами Python. 

***`.env/include/`*** і ***`.env/lib/`*** – містять біблиотечні файли оточення. 
Нові пакети буде встановлено в каталог `.env/lib/python3.6/site-packages/`. 

Щоб можна було використовувати віртуальне оточення його спочатку треба активувати. 
Для цього виконаємо автоматично створений файл `activate.bat` який розташовано у `.env/scripts/`: 

	.env\scripts\activate
	
Якщо усе пройшло успішно, то перед запрошенням у командному рядку з'явився додатковий напис який співпадає з іменем віртуального оточення:

	(.env) c:\...
	
При цьому в змінну середовища `PATH`, в самий початок, буде додано шлях до директорії `scripts`. 

Тепер ми можемо встановлювати необхідні нам пакети за допомогою `pip` і, власне, запустити інтерпретатор командою: 

	python

Щоб вийти з віртуального оточення або ж його деактивації скористаємось командою:
 
	deactivate

Також можна запустити певний файл у віртуальному оточенні без його активації/деактивації. 
Для цього достатньо вказати інтерпретатор Python, 
який розташовано саме у потрібному віртуальному оточенні:

	c:\dev\project\.env\scripts\python.exe my_app.py
	
	
### `pipenv`

`Pipenv` — це набираючий популярність пакет керування віртуальним оточенням для Python, який вирішує деякі розповсюджені проблеми, пов'язані з типовим робочим процесом, в якому використовуються `pip`, `virtualenv` і старий добрий файл `requirements.txt`. 

Почнемо зі встановлення `pipenv`:

	>pip install pipenv
	
Перейдемо в папку з нашим проектом і створимо віртуальне оточення з Python третьої версії:

	>cd project
	>pipenv --three
	Creating a virtualenv for this project…
	...
	Successfully created virtual environment!
	Virtualenv location: C:\Users\UserName\.virtualenvs\project-ONobu
	Creating a Pipfile for this project…
	
Активуємо віртуальне оточення проекта:

	>pipenv shell
	Launching subshell in virtual environment…
	Microsoft Windows [Version 10.0.17763.503]
	(c) Корпорация Майкрософт (Microsoft Corporation), 2018. Все права защищены.

	(project-ONobupft) c:\dev\project>

Дізнатись розташування проекта:

	>pipenv --where
	C:\dev\project
	(project-ONobupft) c:\dev\project>
	
Дізнатись розташування віртуального оточення: 

	>pipenv --venv
	C:\Users\UserName\.virtualenvs\project-ONobupft
	(project-ONobupft) c:\dev\project>

Зауважте: віртуальні оточення зберігаються в домашній теці користувача. 

Дізнатись розташування інтерпретатора: 

	>pipenv --py
	C:\Users\UserName\.virtualenvs\project-ONobupft\Scripts\python.exe
	(project-ONobupft) c:\dev\project>

Окей, давайте встановимо декілька пакетів: 

	>pipenv install flask requests
	Installing flask…
	Adding flask to Pipfile's [packages]…
	Installation Succeeded
	Installing requests…
	Adding requests to Pipfile's [packages]…
	Installation Succeeded
	Pipfile.lock not found, creating…
	Locking [dev-packages] dependencies…
	Locking [packages] dependencies…
	Success!
	Updated Pipfile.lock (8d87f5)!
	Installing dependencies from Pipfile.lock (8d87f5)…
	  ================================ 11/11 - 00:00:08

Буде створено спеціальні файли `Pipfile` і `Pipfile.lock`, у яких міститься інформація про встановлені пакети. 

Відобразити встановлені пакети разом з їх залежностями у вигляді деревоподібної структури: 

	>pipenv graph
	Flask==1.0.3
	  - click [required: >=5.1, installed: 7.0]
	  - itsdangerous [required: >=0.24, installed: 1.1.0]
	  - Jinja2 [required: >=2.10, installed: 2.10.1]
		- MarkupSafe [required: >=0.23, installed: 1.1.1]
	  - Werkzeug [required: >=0.14, installed: 0.15.4]
	requests==2.22.0
	  - certifi [required: >=2017.4.17, installed: 2019.3.9]
	  - chardet [required: >=3.0.2,<3.1.0, installed: 3.0.4]
	  - idna [required: >=2.5,<2.9, installed: 2.8]
	  - urllib3 [required: >=1.21.1,<1.26,!=1.25.1,!=1.25.0, installed: 1.25.3]

Ну і залишити віртуальне оточення: 
	
	>exit
	

















## Додаткові матеріали

- [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)
- [virtualenv](https://virtualenv.pypa.io/en/stable/)
- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- [Pipenv: Python Dev Workflow for Humans]()