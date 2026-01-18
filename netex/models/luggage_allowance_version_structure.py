from dataclasses import dataclass, field
from decimal import Decimal

from .baggage_type_enumeration import BaggageTypeEnumeration
from .baggage_use_type_enumeration import BaggageUseTypeEnumeration
from .luggage_allowance_type_enumeration import LuggageAllowanceTypeEnumeration
from .luggage_charging_basis_enumeration import LuggageChargingBasisEnumeration
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LuggageAllowanceVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "LuggageAllowance_VersionStructure"

    baggage_use_type: BaggageUseTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "BaggageUseType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    baggage_type: BaggageTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "BaggageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    luggage_allowance_type: LuggageAllowanceTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "LuggageAllowanceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_items: int | None = field(
        default=None,
        metadata={
            "name": "MaximumNumberItems",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_bag_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumBagHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_bag_width: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumBagWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_bag_depth: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumBagDepth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_bag_weight: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumBagWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    total_weight: Decimal | None = field(
        default=None,
        metadata={
            "name": "TotalWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    luggage_charging_basis: LuggageChargingBasisEnumeration | None = field(
        default=None,
        metadata={
            "name": "LuggageChargingBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
