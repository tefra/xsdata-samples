from dataclasses import dataclass, field
from typing import Optional
from .common_version_frame_structure import CommonVersionFrameStructure
from .driver_trips_in_frame_rel_structure import DriverTripsInFrameRelStructure
from .duties_in_frame_rel_structure import DutiesInFrameRelStructure
from .duty_parts_in_frame_rel_structure import DutyPartsInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DriverScheduleVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "DriverSchedule_VersionFrameStructure"

    duties: Optional[DutiesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duty_parts: Optional[DutyPartsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "dutyParts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_trips: Optional[DriverTripsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "driverTrips",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
