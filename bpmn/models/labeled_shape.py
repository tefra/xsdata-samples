from dataclasses import dataclass

from .shape import Shape

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass
class LabeledShape(Shape):
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"
