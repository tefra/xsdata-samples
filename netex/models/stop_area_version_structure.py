from dataclasses import dataclass, field
from typing import Optional
from netex.models.stop_area_ref_structure import StopAreaRefStructure
from netex.models.topographic_place_ref import TopographicPlaceRef
from netex.models.topographic_place_view import TopographicPlaceView
from netex.models.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopAreaVersionStructure(ZoneVersionStructure):
    class Meta:
        name = "StopArea_VersionStructure"

    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parent_stop_area_ref: Optional[StopAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentStopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place_ref: Optional[TopographicPlaceRef] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place_view: Optional[TopographicPlaceView] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
