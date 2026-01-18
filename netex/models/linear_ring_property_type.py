from __future__ import annotations

from dataclasses import dataclass, field

from .linear_ring import LinearRing

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class LinearRingPropertyType:
    linear_ring: LinearRing = field(
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
