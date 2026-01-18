from __future__ import annotations

from dataclasses import dataclass

from .point_property_type import PointPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointProperty(PointPropertyType):
    class Meta:
        name = "pointProperty"
        namespace = "http://www.opengis.net/gml/3.2"
