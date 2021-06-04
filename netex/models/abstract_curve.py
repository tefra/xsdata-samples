from dataclasses import dataclass
from netex.models.abstract_curve_type import AbstractCurveType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractCurve(AbstractCurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
