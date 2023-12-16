from dataclasses import dataclass, field
from typing import Optional, Union
from .access_zone_ref import AccessZoneRef
from .administrative_zone_ref import AdministrativeZoneRef
from .fare_zone_ref import FareZoneRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .stop_area_ref import StopAreaRef
from .tariff_zone_ref import TariffZoneRef
from .transport_administrative_zone_ref import TransportAdministrativeZoneRef
from .zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ZoneRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "zoneRefs_RelStructure"

    choice: Optional[Union[StopAreaRef, AccessZoneRef, TransportAdministrativeZoneRef, AdministrativeZoneRef, FareZoneRef, TariffZoneRef, ZoneRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StopAreaRef",
                    "type": StopAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessZoneRef",
                    "type": AccessZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZoneRef",
                    "type": TransportAdministrativeZoneRef,
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
                    "type": TariffZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneRef",
                    "type": ZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
