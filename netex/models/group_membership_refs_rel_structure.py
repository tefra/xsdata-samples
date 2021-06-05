from dataclasses import dataclass, field
from typing import List
from netex.models.access_zone_ref import AccessZoneRef
from netex.models.administrative_zone_ref import AdministrativeZoneRef
from netex.models.fare_zone_ref import FareZoneRef
from netex.models.group_of_points_ref_2 import GroupOfPointsRef2
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.stop_area_ref import StopAreaRef
from netex.models.tariff_zone_ref_1 import TariffZoneRef1
from netex.models.tariff_zone_ref_2 import TariffZoneRef2
from netex.models.transport_administrative_zone_ref import TransportAdministrativeZoneRef
from netex.models.zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupMembershipRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "groupMembershipRefs_RelStructure"

    stop_area_ref: List[StopAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    access_zone_ref: List[AccessZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    transport_administrative_zone_ref: List[TransportAdministrativeZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TransportAdministrativeZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    administrative_zone_ref: List[AdministrativeZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_zone_ref: List[FareZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "FareZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    tariff_zone_ref: List[TariffZoneRef1] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_tariff_zone_ref: List[TariffZoneRef2] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    zone_ref: List[ZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "ZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_of_points_ref: List[GroupOfPointsRef2] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPointsRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
