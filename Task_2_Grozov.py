cities = [
    'Москва',
    'Токио',
    'Париж',
    'Нью-Йорк',
    'Лондон',
    'Берлин',
    'Сингапур',
    'Копенгаген',
    'Амстердам',
    'Сидней'
]

# TODO с помощью цикла for и команды enumerate распечатайте рейтинг городов
for i in enumerate(cities,1):
    a, b = i
    print(f"{a:2}-е место: {b:2}")
