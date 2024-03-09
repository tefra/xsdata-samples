from dataclasses import dataclass

from .reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DescriptionReference(ReferenceType):
    class Meta:
        name = "descriptionReference"
        namespace = "http://www.opengis.net/gml/3.2"
