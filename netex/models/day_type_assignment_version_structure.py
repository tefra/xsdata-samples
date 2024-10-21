from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate

from .assignment_version_structure_1 import AssignmentVersionStructure1
from .day_type_ref import DayTypeRef
from .fare_day_type_ref import FareDayTypeRef
from .operating_day_ref import OperatingDayRef
from .operating_period_ref import OperatingPeriodRef
from .service_calendar_ref import ServiceCalendarRef
from .timeband_ref import TimebandRef
from .uic_operating_period_ref import UicOperatingPeriodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DayTypeAssignmentVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "DayTypeAssignment_VersionStructure"

    service_calendar_ref: Optional[ServiceCalendarRef] = field(
        default=None,
        metadata={
            "name": "ServiceCalendarRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            UicOperatingPeriodRef, OperatingPeriodRef, OperatingDayRef, XmlDate
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UicOperatingPeriodRef",
                    "type": UicOperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingPeriodRef",
                    "type": OperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDayRef",
                    "type": OperatingDayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Date",
                    "type": XmlDate,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    day_type_ref: Optional[Union[FareDayTypeRef, DayTypeRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    timeband_ref: Iterable[TimebandRef] = field(
        default_factory=list,
        metadata={
            "name": "TimebandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 5,
        },
    )
    is_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
