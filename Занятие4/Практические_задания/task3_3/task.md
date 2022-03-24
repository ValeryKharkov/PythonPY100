Для проверки вхождения ключа в словарь можно также использовать оператор `in`.  
```python
if key in dict_:
    ...
```

В данном случае с помощью функции `is_exist_fruit` мы проверяем наличие фрукта в корзине.
Но такую конструкцию условного оператор `if` можно переписать в тернарный оператор или inline if.
```python
if condition:  # обычный условный оператор
    return true_value
else:
    return false_value

return true_value if condition else false_value  # inline if
```