from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .baggage_type_enumeration import BaggageTypeEnumeration
from .baggage_use_type_enumeration import BaggageUseTypeEnumeration
from .luggage_allowance_type_enumeration import LuggageAllowanceTypeEnumeration
from .luggage_charging_basis_enumeration import LuggageChargingBasisEnumeration
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageAllowanceVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "LuggageAllowance_VersionStructure"

    baggage_use_type: None | BaggageUseTypeEnumeration = field(
        default=None,
        metadata={
            "name": "BaggageUseType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    baggage_type: None | BaggageTypeEnumeration = field(
        default=None,
        metadata={
            "name": "BaggageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    luggage_allowance_type: None | LuggageAllowanceTypeEnumeration = field(
        default=None,
        metadata={
            "name": "LuggageAllowanceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_items: None | int = field(
        default=None,
        metadata={
            "name": "MaximumNumberItems",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_bag_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "MaximumBagHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_bag_width: None | Decimal = field(
        default=None,
        metadata={
            "name": "MaximumBagWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_bag_depth: None | Decimal = field(
        default=None,
        metadata={
            "name": "MaximumBagDepth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_bag_weight: None | Decimal = field(
        default=None,
        metadata={
            "name": "MaximumBagWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    total_weight: None | Decimal = field(
        default=None,
        metadata={
            "name": "TotalWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    luggage_charging_basis: None | LuggageChargingBasisEnumeration = field(
        default=None,
        metadata={
            "name": "LuggageChargingBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
