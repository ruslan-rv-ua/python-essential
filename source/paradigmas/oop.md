# Об'єктно-орієнтоване програмування

> ***Об'єктно-орієнтоване програмування*** — це підхід до побудови програм, що використовує об'єктну декомпозицію задачі, при якій структура системи описується в термінах об'єктів і зв'язків між ними, а поведінка — в термінах обміну повідомленнями між об'єктами.

Об'єкт представляє собою цілісну модель і природну імітацію діяльності деякого елемента реального світу. Об'єкти, як і реальні сутності навколишнього світу характеризуються тим, що вони мають певний набір властивостей, здатні різними способами змінювати ці властивості і можуть реагувати на події, які виникають як у навколишньому світі, так і усередині самого об'єкта. Об'єкт, як правило, включає деякі дані, які характеризують стан об'єкта, та функції обробки цих даних, які описують поведінку об'єкта. Функції об'єкта, які у об'єктно-орієнтованому програмуванні (ООП) називають методами, зазвичай призначені для доступу до даних об'єкта та виконання певних дій над ними.

Поєднання даних і дій, що виконуються над ними, в єдине ціле, яке називають об'єктом, і є концептуальною ідеєю ООП.

Кожен об'єкт є екземпляром певного класу. Клас в ООП - це в чистому вигляді абстрактний тип даних, що створюється програмістом. Клас представляє собою множину об'єктів зі схожою структурою і схожою поведінкою. Усі об'єкти, які є екземплярами одного класу, можуть виконувати одні й ті ж самі дії. Поняттяоб'єкта такласу є фундаментальними в ООП.

Об’єкти взаємодіють між собою шляхом надсилання повідомлень. Повідомлення — це запит на виконання дії, доповнений набором аргументів які можуть знадобитися при її виконанні. Об'єкт, що приймає повідомлення, реагує на нього особливим, тільки йому відомим чином. При цьому він може послати повідомлення іншим об'єктам, отримати від них відповіді, змінити свій стан і, нарешті, повернути відповідь тому об'єкту, який послав йому повідомлення. Всі дії та розрахунки в об'єктно-орієнтованих програмах виконуються шляхом взаємодії (обміну даними) між об'єктами за допомогою механізму передачі повідомлень.

ООП ніяк не пов'язане з процесом виконання програми, а є тільки способом її ефективної організації. Основою такої організації є використання принципів:
* інкапсуляції
* успадкування
* поліморфізму

***Інкапсуляція*** визначає спосіб опису, який передбачає об'єднання в межах класу даних і методів їхньої обробки, а також приховування деталей реалізації класу: користувач повинен бачити і використовувати для доступу до об'єкту і маніпулювання ним виключно інтерфейсну частину класу (список декларованих властивостей і методів). Це дозволяє забезпечити захист даних від зовнішнього втручання. 

***Успадкування*** — це механізм породження нових класів з уже існуючих. Породжений клас успадковує властивості та поведінку класу-предка і може доповнити їх своїми власними. Механізм успадкування дозволяє організовувати класи у єдину деревоподібну структуру із загальним коренем, яка називається ієрархією успадкування і характеризуються тим, що властивості та поведінка, зв'язані з екземплярами деякого класу, автоматично доступні будь-якому класу, розташованому нижче в ієрархічному дереві. Це дає змогу будувати похідні поняття на основі базових і таким чином створювати модель як завгодно складної предметної області із заданими властивостями.

***Поліморфізм*** — це механізм, що дозволяє мати різні реалізації для одного і того ж методу, які будуть вибиратися залежно від типу об'єкту, переданого до методу при його виклику. Поліморфізм означає, що певні одноіменні дії можуть відрізнятися в залежності від того, до якого із класів вони відносяться. Наприклад, для трьох різних об'єктів або класів - двигун автомобіля, електричне світло в кімнаті і комп'ютер, можна визначити операцію "вимкнути". Проте сутність цієї операції буде відрізнятися для кожного із розглянутих об'єктів. Так для двигуна автомобіля виклик дії "вимкнути двигун" означає припинення подачі палива і його зупинку. Виклик дії "вимкнути світло" означає просте клацання вимикача, після чого кімната зануриться в темряву. В останньому випадку дія "вимкнути компьютер" може бути причиною втрати даних, якщо виконується нерегламентованим чином. Використання поліморфізму робить програмне забезпечення більш гнучким і універсальним.

Таким чином, на відміну від імперативного програмування, що базується на алгоритмічній декомпозиції програми, а також роз'єднанні у програмах даних і процедур їхньої обробки, у об'єктно́-орієнтованих програмах має місце об'єктна декомпозиція програми і об’єднання даних та функцій їхньої обробки в межах певного класу. Первинними в ООП є дані (об'єкти), а не код. Об'є́ктно-орієнто́вана програма фактично є описом структури і поведінки окремих об'єктів, які взаємодіють між собою таким чином, щоб забезпечити певну поведінку системи.

Стійкість та керованість об'єктно-орієнтованої програми забезпечуються за рахунок чіткого розподілу відповідальності об’єктів (за кожну дію відповідає певний об’єкт), однозначного означення інтерфейсів міжоб’єктної взаємодії та повної ізольованості внутрішньої структури об’єкта від зовнішнього середовища (інкапсуляції).

Роль програміста при написанні об'єктно́-орієнтованої програми полягає у формуванні і реалізації такої ієрархії об'єктів, взаємодія яких після запуску програми приведе до досягнення необхідного кінцевого результату. Використання раніше розроблених (можливо, іншими колективами програмістів) бібліотек об'єктів дозволяє значно заощадити трудовитрати при розробці програмного забезпечення, особливо типового.

Слід зауважити, що переваги ООП повною мірою виявляються лише при розробці досить великих програмних систем. Особливо зручно і легко в об'єктах виразитивзаємодіюміж різними елементами графічного інтерфейсу користувача. Спроби використовувати ООП для програмування нескладних алгоритмів, пов'язаних, наприклад, з розрахунками за готовими формулами, найчастіше виглядають штучними нагромадженнями непотрібних мовних конструкцій. Їх простіше і зручніше розробляти, застосовуючи імперативне програмування.

Об'єктно-орієнтовані мови можна розділити на три групи:

* *Чисті мови*, які в найбільш класичному вигляді підтримують тільки одну об'єктно-орієнтовану парадигму програмування. Такі мови містять невелику мовну частину і істотну бібліотеку, а також набір засобів підтримки часу виконання.
* *Гібридні мови*, які з'явилися в результаті впровадження об'єктно-орієнтованих конструкцій в популярну імперативну мову програмування.
* *Урізані мови*, які з'явилися в результаті видалення з гібридних мов найбільш небезпечних і непотрібних з об'єктно-орієнтованої точки зору конструкцій.
