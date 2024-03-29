from dataclasses import dataclass, field

from .direction_type_enumeration import DirectionTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DirectionType:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: DirectionTypeEnumeration = field(
        default=DirectionTypeEnumeration.OUTBOUND,
        metadata={
            "required": True,
        },
    )
