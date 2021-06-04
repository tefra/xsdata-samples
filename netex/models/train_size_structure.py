from dataclasses import dataclass, field
from typing import Optional
from netex.models.train_size_enumeration import TrainSizeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainSizeStructure:
    number_of_cars: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfCars",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_size_type: Optional[TrainSizeEnumeration] = field(
        default=None,
        metadata={
            "name": "TrainSizeType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
