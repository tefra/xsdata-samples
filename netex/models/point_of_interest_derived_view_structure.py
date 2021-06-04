from dataclasses import dataclass, field
from typing import Optional
from netex.models.derived_view_structure import DerivedViewStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.point_of_interest_ref import PointOfInterestRef
from netex.models.type_of_place_refs_rel_structure import TypeOfPlaceRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "PointOfInterest_DerivedViewStructure"

    point_of_interest_ref: Optional[PointOfInterestRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestRef",
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
