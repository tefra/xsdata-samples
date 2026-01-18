from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from .entity_in_version_structure import DataManagedObjectStructure
from .individual_traveller_ref import IndividualTravellerRef
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class IndividualPassengerInfoVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "IndividualPassengerInfo_VersionStructure"

    individual_traveller_ref: None | IndividualTravellerRef = field(
        default=None,
        metadata={
            "name": "IndividualTravellerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ranking: None | int = field(
        default=None,
        metadata={
            "name": "Ranking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    last_trip_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LastTripDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    comments_about: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "CommentsAbout",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travelling_with_pet: None | bool = field(
        default=None,
        metadata={
            "name": "TravellingWithPet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
