from dataclasses import dataclass

from .abstract_gmltype import AbstractGmltype

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGml(AbstractGmltype):
    class Meta:
        name = "AbstractGML"
        namespace = "http://www.opengis.net/gml/3.2"
