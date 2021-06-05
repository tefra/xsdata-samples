from dataclasses import dataclass, field
from typing import Optional
from netex.models.access_zone_ref import AccessZoneRef
from netex.models.administrative_zone_ref import AdministrativeZoneRef
from netex.models.fare_zone_ref import FareZoneRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.stop_area_ref import StopAreaRef
from netex.models.tariff_zone_ref_1 import TariffZoneRef1
from netex.models.tariff_zone_ref_2 import TariffZoneRef2
from netex.models.transport_administrative_zone_ref import TransportAdministrativeZoneRef
from netex.models.zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ZoneRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "zoneRefs_RelStructure"

    stop_area_ref: Optional[StopAreaRef] = field(
        default=None,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    access_zone_ref: Optional[AccessZoneRef] = field(
        default=None,
        metadata={
            "name": "AccessZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    transport_administrative_zone_ref: Optional[TransportAdministrativeZoneRef] = field(
        default=None,
        metadata={
            "name": "TransportAdministrativeZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    administrative_zone_ref: Optional[AdministrativeZoneRef] = field(
        default=None,
        metadata={
            "name": "AdministrativeZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    fare_zone_ref: Optional[FareZoneRef] = field(
        default=None,
        metadata={
            "name": "FareZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    tariff_zone_ref: Optional[TariffZoneRef1] = field(
        default=None,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    netex_org_uk_netex_tariff_zone_ref: Optional[TariffZoneRef2] = field(
        default=None,
        metadata={
            "name": "TariffZoneRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    zone_ref: Optional[ZoneRef] = field(
        default=None,
        metadata={
            "name": "ZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
