from dataclasses import dataclass, field
from typing import Optional
from .access_zone_ref import AccessZoneRef
from .administrative_zone_ref import AdministrativeZoneRef
from .fare_zone_ref import FareZoneRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .stop_area_ref import StopAreaRef
from .tariff_zone_ref_1 import TariffZoneRef1
from .tariff_zone_ref_2 import TariffZoneRef2
from .transport_administrative_zone_ref import TransportAdministrativeZoneRef
from .zone_ref import ZoneRef

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
        }
    )
    access_zone_ref: Optional[AccessZoneRef] = field(
        default=None,
        metadata={
            "name": "AccessZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_administrative_zone_ref: Optional[TransportAdministrativeZoneRef] = field(
        default=None,
        metadata={
            "name": "TransportAdministrativeZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    administrative_zone_ref: Optional[AdministrativeZoneRef] = field(
        default=None,
        metadata={
            "name": "AdministrativeZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_zone_ref: Optional[FareZoneRef] = field(
        default=None,
        metadata={
            "name": "FareZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zone_ref: Optional[TariffZoneRef1] = field(
        default=None,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_tariff_zone_ref: Optional[TariffZoneRef2] = field(
        default=None,
        metadata={
            "name": "TariffZoneRef_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zone_ref: Optional[ZoneRef] = field(
        default=None,
        metadata={
            "name": "ZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
