from __future__ import annotations

from dataclasses import dataclass

from .abstract_geometry_type import AbstractGeometryType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class AbstractGeometry(AbstractGeometryType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
