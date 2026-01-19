from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
class IndividualTravellerVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "IndividualTraveller_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_ref: None | CustomerRef = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    identity_verified: None | bool = field(
        default=None,
        metadata={
            "name": "IdentityVerified",
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
    gender: None | GenderEnumeration = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    talkative: None | bool = field(
        default=None,
        metadata={
            "name": "Talkative",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    smoker: None | bool = field(
        default=None,
        metadata={
            "name": "Smoker",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    languages: Sequence[str] = field(
        default_factory=list,
        metadata={
            "name": "Languages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    vehicle_pooling_driver_infos: (
        None | VehiclePoolingDriverInfosRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "vehiclePoolingDriverInfos",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    individual_passenger_infos: None | IndividualPassengerInfosRelStructure = (
        field(
            default=None,
            metadata={
                "name": "individualPassengerInfos",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
