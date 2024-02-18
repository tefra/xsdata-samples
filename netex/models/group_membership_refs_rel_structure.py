from dataclasses import dataclass, field
from typing import List, Union
from .access_zone_ref import AccessZoneRef
from .administrative_zone_ref import AdministrativeZoneRef
from .fare_zone_ref import FareZoneRef
from .mobility_service_constraint_zone_ref import (
    MobilityServiceConstraintZoneRef,
)
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .stop_area_ref import StopAreaRef
from .tariff_zone_ref_1 import TariffZoneRef1
from .transport_administrative_zone_ref import TransportAdministrativeZoneRef
from .zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupMembershipRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "groupMembershipRefs_RelStructure"

    zone_ref_or_tariff_zone_ref: List[
        Union[
            MobilityServiceConstraintZoneRef,
            StopAreaRef,
            TransportAdministrativeZoneRef,
            AccessZoneRef,
            AdministrativeZoneRef,
            FareZoneRef,
            TariffZoneRef1,
            ZoneRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobilityServiceConstraintZoneRef",
                    "type": MobilityServiceConstraintZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopAreaRef",
                    "type": StopAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZoneRef",
                    "type": TransportAdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessZoneRef",
                    "type": AccessZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZoneRef",
                    "type": AdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareZoneRef",
                    "type": FareZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZoneRef",
                    "type": TariffZoneRef1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneRef",
                    "type": ZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
