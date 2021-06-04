from dataclasses import dataclass, field
from typing import Optional
from netex.models.derived_view_structure import DerivedViewStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.stop_place_ref import StopPlaceRef
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.type_of_place_refs_rel_structure import TypeOfPlaceRefsRelStructure
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "StopPlace_DerivedViewStructure"

    stop_place_ref: Optional[StopPlaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_types: Optional[TypeOfPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_type: Optional[StopTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPlaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_mode: Optional[VehicleModeEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
