from .geometric_figure import GeometricFigure
from .figure_color import FigureColor

class Rectangle(GeometricFigure):
    def __init__(self, width: float, height: float, color: str):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self) -> float:
        return self.width * self.height

    def __repr__(self) -> str:
        return "Фигура: {0}, Ширина: {1}, Высота: {2}, Цвет: {3}, Площадь: {4}".format(
            self.name(),
            self.width,
            self.height,
            self.color.color,
            self.area()
        )

    @classmethod
    def name(cls) -> str:
        return "Прямоугольник"