from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .driver_trip_times_rel_structure import DriverTripTimesRelStructure
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DriverTripVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "DriverTrip_VersionStructure"

    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_point_ref: TimingPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_point_ref: TimingPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accounting_time: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "AccountingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accounting_factor: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "AccountingFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    trip_times: DriverTripTimesRelStructure | None = field(
        default=None,
        metadata={
            "name": "tripTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
