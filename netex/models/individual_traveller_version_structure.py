from dataclasses import dataclass, field
from typing import List, Optional

from .customer_ref import CustomerRef
from .entity_in_version_structure import DataManagedObjectStructure
from .gender_enumeration import GenderEnumeration
from .individual_passenger_infos_rel_structure import (
    IndividualPassengerInfosRelStructure,
)
from .multilingual_string import MultilingualString
from .vehicle_pooling_driver_infos_rel_structure import (
    VehiclePoolingDriverInfosRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class IndividualTravellerVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "IndividualTraveller_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    identity_verified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IdentityVerified",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ranking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gender: Optional[GenderEnumeration] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    talkative: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Talkative",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    smoker: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Smoker",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    languages: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Languages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    vehicle_pooling_driver_infos: Optional[
        VehiclePoolingDriverInfosRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "vehiclePoolingDriverInfos",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    individual_passenger_infos: Optional[
        IndividualPassengerInfosRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "individualPassengerInfos",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
