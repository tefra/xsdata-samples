from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .all_modes_enumeration import AllModesEnumeration
from .driver_trip_ref import DriverTripRef
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DriverTripTimeVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "DriverTripTime_VersionStructure"

    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    driver_trip_ref: DriverTripRef | None = field(
        default=None,
        metadata={
            "name": "DriverTripRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: AllModesEnumeration | None = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
