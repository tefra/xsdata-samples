from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from .entity_in_version_structure import DataManagedObjectStructure
from .individual_traveller_ref import IndividualTravellerRef
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class IndividualPassengerInfoVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "IndividualPassengerInfo_VersionStructure"

    individual_traveller_ref: IndividualTravellerRef | None = field(
        default=None,
        metadata={
            "name": "IndividualTravellerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ranking: int | None = field(
        default=None,
        metadata={
            "name": "Ranking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    last_trip_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "LastTripDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    comments_about: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "CommentsAbout",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travelling_with_pet: bool | None = field(
        default=None,
        metadata={
            "name": "TravellingWithPet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
