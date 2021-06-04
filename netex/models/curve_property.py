from dataclasses import dataclass
from netex.models.curve_property_type import CurvePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveProperty(CurvePropertyType):
    class Meta:
        name = "curveProperty"
        namespace = "http://www.opengis.net/gml/3.2"
