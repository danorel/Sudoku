# Sudoku
**Як реалізований сам алгоритм?**

Отже, розглянемо таку ситуацію:
```
* * * * * * * 9 7
* * 7 * * 1 * * *
6 * * 7 5 * * 3 *
* * 5 * * 7 * 1 *
* 3 * * * * 2 * *
9 1 * 5 * 8 * * 6
2 * * * * * 7 * *
* 7 * * * * * 4 9
3 * * 1 7 * * * *
```

1. Перебираємо усі цифри у нашому алфавіті [1, 9]. Беремо по порядку кожен елемент та перевіряємо наступні умови:  
  (1) Перевіряємо повністю рядок, чи елемент вже міститься у ньому.   
    -> Якщо так.   
      -> Якщо елементів з алфавіту для перебору не залишилось - сповістити користувача, що не має розв'язку для судоку.   
      -> Якщо залишились - беремо наступний елемент.   
    -> Якщо ні.  
      -> Переходимо до наступної умови.  
  (2) Перевіряємо повністю колону, чи елемент вже міститься у ній.     
    -> Якщо так.  
      -> Якщо елементів з алфавіту для перебору не залишилось - сповістити користувача, що не має розв'язку для судоку.   
      -> Якщо залишились - беремо наступний елемент.   
    -> Якщо ні - переходимо до наступної умови.   
  (3) Перевіряємо, чи міститься елемент у матриці 3х3.   
    -> Якщо так.   
      -> Якщо елементів з алфавіту для перебору не залишилось - сповістити користувача, що не має розв'язку для судоку.     
      -> Якщо залишились - беремо наступний елемент.    
    -> Якщо ні - заповнюємо матрицю у вибраних координатах значенням елемента.    
2. Рекурсивно продовжувати для кожного рядка алгоритм (1.)    

Отже на виході ми отримаємо розв'язане судоку, **якщо для нього існує розв'язок**:

```
1 2 3 4 8 6 5 9 7 
4 5 7 3 9 1 6 2 8 
6 9 8 7 5 2 4 3 1 
8 6 5 2 3 7 9 1 4 
7 3 4 6 1 9 2 8 5 
9 1 2 5 4 8 3 7 6 
2 8 1 9 6 4 7 5 3 
5 7 6 8 2 3 1 4 9 
3 4 9 1 7 5 8 6 2 
```
