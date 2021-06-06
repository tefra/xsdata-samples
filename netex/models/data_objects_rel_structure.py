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

    composite_frame: List[CompositeFrame] = field(
        default_factory=list,
        metadata={
            "name": "CompositeFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_transaction_frame: List[SalesTransactionFrame] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransactionFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_frame: List[FareFrame] = field(
        default_factory=list,
        metadata={
            "name": "FareFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_schedule_frame: List[DriverScheduleFrame] = field(
        default_factory=list,
        metadata={
            "name": "DriverScheduleFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_schedule_frame: List[VehicleScheduleFrame] = field(
        default_factory=list,
        metadata={
            "name": "VehicleScheduleFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_frame: List[ServiceFrame] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timetable_frame: List[TimetableFrame] = field(
        default_factory=list,
        metadata={
            "name": "TimetableFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_frame: List[SiteFrame] = field(
        default_factory=list,
        metadata={
            "name": "SiteFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_frame: List[InfrastructureFrame] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_frame: List[GeneralFrame] = field(
        default_factory=list,
        metadata={
            "name": "GeneralFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    resource_frame: List[ResourceFrame] = field(
        default_factory=list,
        metadata={
            "name": "ResourceFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_calendar_frame: List[ServiceCalendarFrame] = field(
        default_factory=list,
        metadata={
            "name": "ServiceCalendarFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    common_frame: List[CommonFrame] = field(
        default_factory=list,
        metadata={
            "name": "CommonFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
