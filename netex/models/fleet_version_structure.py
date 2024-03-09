from dataclasses import dataclass, field
from typing import Optional, Union

from .authority_ref import AuthorityRef
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .operator_ref import OperatorRef
from .transport_type_refs_rel_structure import TransportTypeRefsRelStructure
from .type_of_fleet_ref import TypeOfFleetRef
from .vehicles_rel_structure import VehiclesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FleetVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "Fleet_VersionStructure"

    members: Optional[VehiclesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_organisation_ref: Optional[Union[AuthorityRef, OperatorRef]] = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "AuthorityRef",
                        "type": AuthorityRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "OperatorRef",
                        "type": OperatorRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
    type_of_fleet_ref: Optional[TypeOfFleetRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFleetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_types: Optional[TransportTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "transportTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
