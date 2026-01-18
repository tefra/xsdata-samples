from dataclasses import dataclass, field

from .priceable_object_version_structure import PriceableObjectVersionStructure
from .type_of_usage_parameter_ref import TypeOfUsageParameterRef
from .usage_parameter_prices_rel_structure import (
    UsageParameterPricesRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageParameterVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "UsageParameter_VersionStructure"

    type_of_usage_parameter_ref: TypeOfUsageParameterRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfUsageParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: UsageParameterPricesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
