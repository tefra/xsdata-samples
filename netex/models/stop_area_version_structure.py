from __future__ import annotations

from dataclasses import dataclass, field

from .stop_area_ref_structure import StopAreaRefStructure
from .topographic_place_ref import TopographicPlaceRef
from .topographic_place_view import TopographicPlaceView
from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopAreaVersionStructure(ZoneVersionStructure):
    class Meta:
        name = "StopArea_VersionStructure"

    public_code: None | str = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_stop_area_ref: None | StopAreaRefStructure = field(
        default=None,
        metadata={
            "name": "ParentStopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    topographic_place_ref_or_topographic_place_view: (
        None | TopographicPlaceRef | TopographicPlaceView
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TopographicPlaceRef",
                    "type": TopographicPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlaceView",
                    "type": TopographicPlaceView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
