from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side: float, color: str):
        super().__init__(width=side, height=side, color=color)
        self.side = side

    def __repr__(self) -> str:
        return "Фигура: {0}, Сторона: {1}, Цвет: {2}, Площадь: {3}".format(
            self.name(),
            self.side,
            self.color.color,
            self.area()
        )

    @classmethod
    def name(cls) -> str:
        return "Квадрат"