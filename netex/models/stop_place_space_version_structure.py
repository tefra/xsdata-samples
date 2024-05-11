from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .multilingual_string import MultilingualString
from .site_entrances_rel_structure import SiteEntrancesRelStructure
from .stop_place_component_version_structure import (
    StopPlaceComponentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceSpaceVersionStructure(StopPlaceComponentVersionStructure):
    class Meta:
        name = "StopPlaceSpace_VersionStructure"

    boarding_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BoardingUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alighting_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AlightingUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrances: Optional[SiteEntrancesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
