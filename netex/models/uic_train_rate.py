from dataclasses import dataclass, field

from .uic_rate_type_enumeration import UicRateTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UicTrainRate:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: UicRateTypeEnumeration | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
