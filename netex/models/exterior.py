from __future__ import annotations

from dataclasses import dataclass

from .abstract_ring_property_type import AbstractRingPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class Exterior(AbstractRingPropertyType):
    class Meta:
        name = "exterior"
        namespace = "http://www.opengis.net/gml/3.2"
