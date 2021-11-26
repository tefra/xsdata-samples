from dataclasses import dataclass, field
from typing import Optional
from .access_zone_ref import AccessZoneRef
from .administrative_zone_ref import AdministrativeZoneRef
from .derived_view_structure import DerivedViewStructure
from .fare_zone_ref import FareZoneRef
from .multilingual_string import MultilingualString
from .stop_area_ref import StopAreaRef
from .tariff_zone_ref_1 import TariffZoneRef1
from .transport_administrative_zone_ref import TransportAdministrativeZoneRef
from .type_of_zone_ref import TypeOfZoneRef
from .zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ZoneDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "Zone_DerivedViewStructure"

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
    zone_ref: Optional[ZoneRef] = field(
        default=None,
        metadata={
            "name": "ZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_zone_ref: Optional[TypeOfZoneRef] = field(
        default=None,
        metadata={
            "name": "TypeOfZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
