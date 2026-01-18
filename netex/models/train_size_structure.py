from __future__ import annotations

from dataclasses import dataclass, field

from .train_size_enumeration import TrainSizeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainSizeStructure:
    number_of_cars: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfCars",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_size_type: None | TrainSizeEnumeration = field(
        default=None,
        metadata={
            "name": "TrainSizeType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
