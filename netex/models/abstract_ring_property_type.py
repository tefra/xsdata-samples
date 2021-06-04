from dataclasses import dataclass, field
from typing import Optional
from netex.models.abstract_ring import AbstractRing
from netex.models.linear_ring import LinearRing

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractRingPropertyType:
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    abstract_ring: Optional[AbstractRing] = field(
        default=None,
        metadata={
            "name": "AbstractRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
