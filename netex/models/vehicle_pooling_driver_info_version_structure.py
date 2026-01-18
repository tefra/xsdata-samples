from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from .driving_style_enumeration import DrivingStyleEnumeration
from .entity_in_version_structure import DataManagedObjectStructure
from .individual_traveller_ref import IndividualTravellerRef
from .multilingual_string import MultilingualString
from .vehicle_ref import VehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingDriverInfoVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VehiclePoolingDriverInfo_VersionStructure"

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
    driving_licence_verified: None | bool = field(
        default=None,
        metadata={
            "name": "DrivingLicenceVerified",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    insurance_verified: None | bool = field(
        default=None,
        metadata={
            "name": "InsuranceVerified",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    driving_style: None | DrivingStyleEnumeration = field(
        default=None,
        metadata={
            "name": "DrivingStyle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_proposed_trips: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfProposedTrips",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_travellers_carried: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfTravellersCarried",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_ref: None | VehicleRef = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
