from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class TypeUnstructuredAddress:
    """
    A simple unstructured address (e.g. 123 South State Avenue, Chicago, IL 60612)
    """

    class Meta:
        name = "typeUnstructuredAddress"

    address: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "min_occurs": 1,
            "max_occurs": 6,
            "min_length": 0,
            "max_length": 50,
        },
    )
