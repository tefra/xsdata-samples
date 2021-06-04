from dataclasses import dataclass
from netex.models.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractReference(ReferenceType):
    class Meta:
        name = "abstractReference"
        namespace = "http://www.opengis.net/gml/3.2"
