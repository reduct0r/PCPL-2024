from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        pass

    @classmethod
    @abstractmethod
    def name(cls):
        pass