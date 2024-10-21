from collections.abc import Iterable
from dataclasses import dataclass, field

from .fare_class_enumeration import FareClassEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareClasses:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[FareClassEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
