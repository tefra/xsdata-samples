from dataclasses import dataclass, field
from typing import List
from netex.models.fare_class_enumeration import FareClassEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareClasses:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[FareClassEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
