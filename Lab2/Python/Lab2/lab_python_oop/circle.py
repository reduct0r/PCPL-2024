from .geometric_figure import GeometricFigure
from .figure_color import FigureColor
import math

class Circle(GeometricFigure):
    def __init__(self, radius: float, color: str):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __repr__(self) -> str:
        return "Фигура: {0}, Радиус: {1}, Цвет: {2}, Площадь: {3:.2f}".format(
            self.name(),
            self.radius,
            self.color.color,
            self.area()
        )

    @classmethod
    def name(cls) -> str:
        return "Круг"