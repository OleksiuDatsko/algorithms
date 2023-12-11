# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконав: Дацко Олексій Романович (Група ІР-25)

### Лабораторна №1 (Варіант 1 рівень 3)
#### Код
 1. [code](https://github.com/OleksiuDatsko/algorithms/tree/lab1-v1-l3)
#### Завдання


Потрібно написати програму для обходу двовимірного масиву розміром NxM у форматі "зігзагу". 
Зігзаговий обхід означає, що спочатку ми рухаємось по діагоналях масиву, пчинаючи з лівої верхньої точки.  
Другим елементом буде виведено елемент, який знаходиться справа, потім  знизу і ліворуч, далі ще крок вниз і рухаємось по діагоналі знову вправо. Для масиву розміром 3x3 обхід у форматі зігзагу виглядає так (де номер у клітинці відповідає порядку її відвідин):
​
```
1 2 6
3 5 7
```


Для масиву 3 х 5 це матиме вигляд:

```
1  2  6   7  12
3  5  8  11  13
4  9  10 14 15
```

Реалізуйте алгоритм, який отримає на вхід масив розміром m та n та поверне одномірний масив з значеннями елементів вхідного масиву при обході його у порядку, зазначеному вище у задачі
​
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` .
Ваш тести мають перевірити роботу алгоритму при значеннях m == n == 5, m =2, n =4, n = 1, m = 6, n == m == 1 ​

### Лабораторна №2 (Варіант 1 Рівень 3)
#### Код
1. [first version](https://github.com/OleksiuDatsko/algorithms/tree/lab2-v1-l3)
2. [5-10-23 version](https://github.com/OleksiuDatsko/algorithms/tree/lab2-v1-l3_5-10-2023)
3. [12-10-23 vesion](https://github.com/OleksiuDatsko/algorithms/tree/lab2-v1-l3_12-10-2023)
#### Завдання​

Зоомагазин займається продажем хом’ячкiв. Це мирнi домашнi iстоти, проте, як виявилося, вони мають цiкаву харчову поведiнку.
Для того, щоб прогодувати хом’ячка, який живе наодинцi, потрiбно H пакетiв корму на день.
Однак, якщо кiлька хом’ячкiв живуть разом, у них прокидається жадiбнiсть. У такому випадку кожен хом’ячок з’їдає додатково G пакетiв корму в день за кожного сусiда. Денна норма H та жадiбнiсть G є iндивiдуальними для кожного хом’ячка.
Всього в магазинi є C хом’ячкiв. Ви бажаєте придбати якомога бiльше, проте у вас є всього S пакетiв їжi на день. Визначте максимальну кiлькiсть хом’ячкiв, яку ви можете прогодувати.
​

Реалізуйте функцію, яка поверне число - максимальне число хом’ячкiв
Вхідні параметри функції:
- **S** — ваш денний запас їжi. 0 ≤ S ≤ 109
- **C** — загальна кiлькiсть хом’ячкiв, яка є в продажу, 1 ≤ C ≤ 105
- Матриця **hamsters**, яка містить **С** рядків, перший стовчик якої містить *денну норму корму*, другий - рiвень *жадiбностi* кожного хом’ячка.

Денні норми є цілими <u>додатніми числами</u> і гарантовано меншими за 109. Іноді у вас можуть бути не жадібні хом’ячки, але також можуть траплятись і надзвичайно жадібні, рівень жадібності може бути як нульовим, так і великим цілим числом

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити роботу вашої функції на прикладах, наведених нижче
​
#### Приклади

##### Приклад 1
​
S = 7

C = 3

hamsters = `[[1, 2], [2, 2], [3, 1]]`

​
Результат: 2

​
Пояснення: Можна взяти першого хом’ячка та будь-якого з iнших двох.
​
##### Приклад 2
​
S  = 19

C = 4

hamsters = `[[5, 0], [2, 2], [1, 4], [5, 1]]`

​
Результат: 3

Пояснення: Третiй хом’ячок надто жадiбний. Можна взяти всiх iнших трьох, тодi за день вони з’їдять (5 + 0 · 2) + (2 + 2 · 2) + (5 + 1 · 2) = 18 пакетiв
​
##### Приклад 3
S = 2

C = 2

hamsters = `[[1, 50000], [1, 60000]]`

​
Результат: 1

Пояснення: Обидва хом’ячки надто жадiбнi, щоб їсти разом.
​
### Лабораторна №1 (Варіант 1 рівень 3)
#### Код
 1. [code](https://github.com/OleksiuDatsko/algorithms/tree/lab3-v1-l3)
 2. [19-10-2023 version](https://github.com/OleksiuDatsko/algorithms/tree/lab3-v1-l3_19-10-2023)
#### Завдання


Для заданого бінарного дерева та конкретної вершини в цьому дереві реалізуйте функцію пошуку наступного елемента під час серединного проходу (in-order traversal). Наступник - це вузол, який має значення більше за заданий вузол і знаходиться найближче до нього при серединному обході.

Нехай у вас задане бінарне дерево такого вигляду:
```
    10
   /  \
  5    15
 / \     \
3   7    20
         /
        12

```
Для вершини зі значенням 7, наступник - це вузол зі значенням 10.

Функція отримує на вхід корінь бінарного дерева та вершину, для якої потрібно знайти наступника.

Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:
```python
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
```

Ваша функція має мати такий вигляд:

```python
def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
```

Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу `BinaryTree` наступним чином:

```python
root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
```

Написати тести з використанням бібліотеки `unittest`.  Ваш проект має бути розділено на окремі папки для коду додатку та тестів (`src` та `test` відповідно).

При написанні коду дотримуйтесь стандарту PEP 8, який визначає правила форматування Python-коду, такі як відступи, довжина рядків, іменування змінних тощо. Для полегшення читабельності коду слід відформатувати ваш код з допомогою  `Black` 


### Лабораторна №4 (Варіант 3 рівень 3)
#### Код
 1. [code](https://github.com/OleksiuDatsko/algorithms/tree/lab4-v3-l3)
 2. [02-11-2023](https://github.com/OleksiuDatsko/algorithms/tree/lab4-v3-l3_02-11-2023)
#### Завдання

Нехай дано двійкову матрицю, де 0 означає воду, а 1 — сушу, а з’єднані числа 1 утворюють острів, підрахуйте загальну кількість островів.
Наприклад, розглянемо таке зображення, де синім позначено воду (0), а сірим - сушу (1):

![image 1](https://github.com/OleksiuDatsko/algorithms/blob/additional-branch/Screenshot%20from%202023-10-30%2014-03-15.png?raw=true)


Загалом у наведеній вище матриці присутні п’ять островів. На зображенні нижче вони позначені цифрами 1–5.

![image 2](https://github.com/OleksiuDatsko/algorithms/blob/additional-branch/Screenshot%20from%202023-10-30%2014-15-18.png?raw=true)



### Лабораторна №5 (Варіант 1 рівень 3)
#### Код
 1. [main code](https://github.com/OleksiuDatsko/algorithms/tree/lab5-v1-l3)
 2. [draft code](https://github.com/OleksiuDatsko/algorithms/tree/lab5-v1-l3_16-11-2023)

#### Завдання [link](https://drive.google.com/file/d/1TcNhEhOd-Ri2bHEkGuk1x3kn3can_WPc/view)
Важливим фактором для багатокористувацької онлайн-гри є низька мережева затримка вiд користувача до сервера. При цьому, пристрої в Iнтернетi спiлкуються один з одним, використовуючи мережевi маршрути, якi проходять через низку промiжних вузлiв-маршрутизаторiв. Кожна ланка цього маршруту має власну ненульову затримку.

![img 1](https://github.com/OleksiuDatsko/algorithms/blob/additional-branch/Screenshot%20from%202023-11-13%2018-39-21.png?raw=true)

- Кожен вузол мережi може виконувати одну з трьох ролей: Client, Router або Server.
- Server може бути лише один на всю мережу.
- Усi комунiкацiї двостороннi: якщо вузол A може спiлкуватися з вузлом B, вузол B може спiлкуватися з вузлом A з такою ж затримкою.
- Якщо iснує кiлька шляхiв вiд клiєнта до сервера, клiєнт гарантовано пiде шляхом з найменшою сумарною затримкою (навiть якщо цей шлях пролягає через iншого клiєнта).
- Усi затримки — сталi додатнi числа. 

Для прикладу вище, затримки до клiєнтiв становлять:
- Client 1: 10 + 80 + 50 = 140 ms
- Client 2: 100 + 50 = 150 ms
- Client 3: 20 ms

Максимальною затримкою в такому випадку є 150 ms. Однак, якщо ми помiняємо ролями вузли *Router 2* i *Server*, затримки скоротяться до 90 ms, 100 ms i 70 ms вiдповiдно, тодi максимальна затримка буде становити 100 ms.

![img 2](https://github.com/OleksiuDatsko/algorithms/blob/additional-branch/Screenshot%20from%202023-11-13%2018-39-29.png?raw=true)

---

Ви розробляєте онлайн-гру для користувачiв зi всiєї країни, i бажаєте розмiстити центральний iгровий сервер таким чином, щоб максимальна затримка мiж сервером i кожним клiєнтом була мiнiмальною. В якостi сервера можна вибрати будь-який вузол мережi, який не є клiєнтом.
Маючи iнформацiю про топологiю мережi (якi вузли з’єднанi з якими, i яка затримка кожного з’єднання), знайдiть таке розташування сервера, яке мiнiмiзує найбiльше значення затримки до клiєнта. Виведiть це значення затримки.

**Вхiднi данi**

Вхiдний файл `gamsrv.in` складається з M + 2 рядкiв.
- Перший рядок мiстить N i M — кiлькiсть вузлiв та з’єднань вiдповiдно.
3 ≤ N ≤ 1000, 2 ≤ M ≤ 1000
- Другий рядок мiстить перелiк цiлих чисел, роздiлених пробiлом — номери
вузлiв, якi є клiєнтами. Усi вузли в мережi нумеруються вiд 1 до N.
- Наступнi M рядкiв мiстять трiйки натуральних чисел startnode, endnode, latency — номер початкового вузла, кiнцевого вузла та затримка для кожного з’єднання. 1 ≤ latency ≤ 109.

**Вихiднi данi**

Вихiдний файл `gamsrv.out` повинен мiстити одне число — мiнiмальне значення найбiльшої затримки до клiєнта (яке ми отримаємо при оптимальному розташуваннi сервера).

### Лабораторна №6 (Варіант 1 рівень 3)
#### Завдання
Cлід написати тести з використанням бібліотеки `unittest`.
Ваш проект має бути розділено на окремі папки для коду додатку та тестів (`src` та `test` відповідно).

При написанні коду дотримуйтесь стандарту PEP 8, який визначає правила форматування Python-коду, такі як відступи, довжина рядків, іменування змінних тощо. Для полегшення читабельності коду слід відформатувати ваш код з допомогою `Black`

Створити функцію на мові програмування Python, яка приймає дві стрічки: "haystack" (довільний текст) та "needle" (шукана стрічка). Програма повинна знайти індекси всіх входжень стрічки "needle" в стрічці "haystack" та повернути цей індекс, використовуючи  метод скінченних автоматів для пошуку підстрічки у стрічці

### Лабораторна №7 (Варіант 1 рівень 3)
#### Завдання

Iндiана Джонс i останнiй прямокутний обхiд

*Код задачi: IJONES*

В пошуках Святого Грааля Iндiана Джонс зiткнувся з небезпечним випробуванням Йому потрiбно пройти крiзь прямокутний коридор, який складається з крихких плит (пригадайте сцену з фiльму «Iндiана Джонс i останнiй хрестовий похiд»).

На кожнiй плитi написана одна лiтера:

```
a a a
c a b
d e f
```

Можна починати з будь-якої плити в найлiвiшому стовпцi. Виходом iз коридору є
верхня права та нижня права плити (для прикладу вище — a та f). Iндiана спритний, i може переходити не лише на сусiдню плиту, а й перестрибувати
через кiлька плит. Проте, щоб не провалитися крiзь пiдлогу, вiн повинен дотримуватися таких правил:

1. Пiсля кожного кроку Iндiана повинен опинятися правiше, нiж був перед цим.
```
a a a
c a b
d e f
```

2. Завжди можна переходити на одну плиту праворуч.
```
a a a
c a b
d e f
```

3. Крiм руху на одну плиту праворуч, можна перестрибувати, проте лише на ту саму лiтеру. Наприклад, з лiтери a можна перестрибнути на будь-яку iншу лiтеру a за умови, що ми цим ходом просунемося правiше.
```
a a a
c a b
d e f
```

Для заданого коридору, пiдрахуйте, скiльки всього iснує способiв пройти його успiшно.

**Вхiднi данi**

Вхiдний файл `ijones .in` складається з H + 1 рядкiв.
- Перший рядок мiстить два числа W i H, роздiленi пробiлом: W — ширина коридору, H — висота коридору, 1 <= W, H <= 2000.
- Кожен з наступних H рядкiв мiстить слово довжиною W символiв, яке складається з малих латинських лiтер вiд a до z.

**Вихiднi данi**

Вихiдний файл `ijones .out` повинен мiстити одне цiле число — кiлькiсть рiзних
шляхiв для виходу з коридору