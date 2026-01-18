from __future__ import annotations

from dataclasses import dataclass

from .curve_property_type import CurvePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveProperty(CurvePropertyType):
    class Meta:
        name = "curveProperty"
        namespace = "http://www.opengis.net/gml/3.2"
