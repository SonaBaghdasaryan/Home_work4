# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.
def my_function(**kwargs) -> dict:
    def hash_():
        try:
            hash()
            return True
        except:
            return False
    return {item if hash_() else str(item): key for key, item in kwargs.items()}
print(my_function(num = 2964, word = "Hallo", arr = [1, 2, 3, 4]))