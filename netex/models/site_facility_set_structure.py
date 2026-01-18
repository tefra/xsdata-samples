from dataclasses import dataclass, field

from .access_facility_list import AccessFacilityList
from .emergency_service_list import EmergencyServiceList
from .facility_set_version_structure import FacilitySetVersionStructure
from .hire_facility_list import HireFacilityList
from .luggage_locker_facility_list import LuggageLockerFacilityList
from .luggage_service_facility_list import LuggageServiceFacilityList
from .money_facility_list import MoneyFacilityList
from .parking_facility_list import ParkingFacilityList
from .staffing import Staffing

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteFacilitySetStructure(FacilitySetVersionStructure):
    access_facility_list: AccessFacilityList | None = field(
        default=None,
        metadata={
            "name": "AccessFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    emergency_service_list: EmergencyServiceList | None = field(
        default=None,
        metadata={
            "name": "EmergencyServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    hire_facility_list: HireFacilityList | None = field(
        default=None,
        metadata={
            "name": "HireFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    luggage_locker_facility_list: LuggageLockerFacilityList | None = field(
        default=None,
        metadata={
            "name": "LuggageLockerFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    luggage_service_facility_list: LuggageServiceFacilityList | None = field(
        default=None,
        metadata={
            "name": "LuggageServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    money_facility_list: MoneyFacilityList | None = field(
        default=None,
        metadata={
            "name": "MoneyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_facility_list: ParkingFacilityList | None = field(
        default=None,
        metadata={
            "name": "ParkingFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    staffing: Staffing | None = field(
        default=None,
        metadata={
            "name": "Staffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
