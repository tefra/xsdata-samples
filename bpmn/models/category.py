from dataclasses import dataclass

from .t_category import TCategory

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Category(TCategory):
    class Meta:
        name = "category"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
