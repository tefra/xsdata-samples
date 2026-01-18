from collections.abc import Iterable
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .local_service_version_structure import LocalServiceVersionStructure
from .luggage_service_facility_enumeration import (
    LuggageServiceFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LuggageServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "LuggageService_VersionStructure"

    luggage_service_facility_list: Iterable[
        LuggageServiceFacilityEnumeration
    ] = field(
        default_factory=list,
        metadata={
            "name": "LuggageServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    luggage_trolleys: bool | None = field(
        default=None,
        metadata={
            "name": "LuggageTrolleys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_luggage_trolleys: bool | None = field(
        default=None,
        metadata={
            "name": "WheelchairLuggageTrolleys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    free_to_use: bool | None = field(
        default=None,
        metadata={
            "name": "FreeToUse",
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
    maximum_bag_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumBagHeight",
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
    luggage_maximal_weigth: Decimal | None = field(
        default=None,
        metadata={
            "name": "LuggageMaximalWeigth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
