from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .driving_style_enumeration import DrivingStyleEnumeration
from .entity_in_version_structure import DataManagedObjectStructure
from .individual_traveller_ref import IndividualTravellerRef
from .multilingual_string import MultilingualString
from .vehicle_ref import VehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolingDriverInfoVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VehiclePoolingDriverInfo_VersionStructure"

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
    driving_licence_verified: bool | None = field(
        default=None,
        metadata={
            "name": "DrivingLicenceVerified",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    insurance_verified: bool | None = field(
        default=None,
        metadata={
            "name": "InsuranceVerified",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    driving_style: DrivingStyleEnumeration | None = field(
        default=None,
        metadata={
            "name": "DrivingStyle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_proposed_trips: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfProposedTrips",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_travellers_carried: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfTravellersCarried",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_ref: VehicleRef | None = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
