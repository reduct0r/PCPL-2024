from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import requests

def main():
    N = 22

    # Создание объектов
    rectangle = Rectangle(width=N, height=N, color="синий")
    circle = Circle(radius=N, color="зеленый")
    square = Square(side=N, color="красный")

    # Вывод информации о фигурах
    print(rectangle)
    print(circle)
    print(square)

    # Вызов метода внешнего пакета
    response = requests.get("https://api.github.com")
    print(f"Статус запроса к GitHub API: {response.status_code}")

if __name__ == "__main__":
    main()