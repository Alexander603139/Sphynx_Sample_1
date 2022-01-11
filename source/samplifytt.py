def factorial(num):
    """Функция вычисления факториала простого числа.
    Args:
        num: [description]
    Returns:
        num: [description]
    """
    if num == 0: 
        return 1 # По договоренности факториал нуля равен единице
    else:
        return num * factorial(num - 1) # возвращаем результат произведения num
        #  и результата возвращенного функцией fact(num - 1)
