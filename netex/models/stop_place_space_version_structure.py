from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .multilingual_string import MultilingualString
from .site_entrances_rel_structure import SiteEntrancesRelStructure
from .stop_place_component_version_structure import (
    StopPlaceComponentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceSpaceVersionStructure(StopPlaceComponentVersionStructure):
    class Meta:
        name = "StopPlaceSpace_VersionStructure"

    boarding_use: None | bool = field(
        default=None,
        metadata={
            "name": "BoardingUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alighting_use: None | bool = field(
        default=None,
        metadata={
            "name": "AlightingUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrances: None | SiteEntrancesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    length: None | Decimal = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: None | Decimal = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
