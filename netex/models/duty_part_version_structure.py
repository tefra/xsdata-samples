from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration, XmlTime

from .accountable_element_structure import AccountableElementStructure
from .duty_ref import DutyRef
from .timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DutyPartVersionStructure(AccountableElementStructure):
    class Meta:
        name = "DutyPart_VersionStructure"

    driver_access_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "DriverAccessDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    driver_return_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "DriverReturnDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    duty_ref: DutyRef | None = field(
        default=None,
        metadata={
            "name": "DutyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_offset: int | None = field(
        default=None,
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_day_offset: int | None = field(
        default=None,
        metadata={
            "name": "EndDayOffset",
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
