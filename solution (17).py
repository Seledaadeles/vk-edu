def repeat_deco(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Пример использования декоратора
@repeat_deco(n=3)
def some_function(arg):
    # Вычисления или операции
    pass

# Ваш код для тестирования
code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)