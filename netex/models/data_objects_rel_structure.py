from dataclasses import dataclass, field
from typing import List
from .common_frame import CommonFrame
from .driver_schedule_frame import DriverScheduleFrame
from .entities_in_version_rel_structure import (
    CompositeFrame,
    GeneralFrame,
)
from .fare_frame import FareFrame
from .infrastructure_frame import InfrastructureFrame
from .resource_frame import ResourceFrame
from .sales_transaction_frame import SalesTransactionFrame
from .service_calendar_frame import ServiceCalendarFrame
from .service_frame import ServiceFrame
from .site_frame import SiteFrame
from .timetable_frame import TimetableFrame
from .vehicle_schedule_frame import VehicleScheduleFrame

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectsRelStructure:
    class Meta:
        name = "dataObjects_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompositeFrame",
                    "type": CompositeFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransactionFrame",
                    "type": SalesTransactionFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareFrame",
                    "type": FareFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverScheduleFrame",
                    "type": DriverScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleScheduleFrame",
                    "type": VehicleScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFrame",
                    "type": ServiceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetableFrame",
                    "type": TimetableFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFrame",
                    "type": SiteFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InfrastructureFrame",
                    "type": InfrastructureFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralFrame",
                    "type": GeneralFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResourceFrame",
                    "type": ResourceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarFrame",
                    "type": ServiceCalendarFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommonFrame",
                    "type": CommonFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
