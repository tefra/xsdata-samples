from __future__ import annotations

from dataclasses import dataclass

from .abstract_ring_type import AbstractRingType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractRing(AbstractRingType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
