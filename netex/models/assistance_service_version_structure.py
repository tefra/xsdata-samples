from dataclasses import dataclass, field
from typing import List, Optional
from .accessibility_tool_enumeration import AccessibilityToolEnumeration
from .assistance_availability_enumeration import AssistanceAvailabilityEnumeration
from .assistance_facility_enumeration import AssistanceFacilityEnumeration
from .emergency_service_enumeration import EmergencyServiceEnumeration
from .local_service_version_structure import LocalServiceVersionStructure
from .safety_facility_enumeration import SafetyFacilityEnumeration
from .staffing_enumeration import StaffingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AssistanceServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "AssistanceService_VersionStructure"

    assistance_facility_list: List[AssistanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    assistance_availability: Optional[AssistanceAvailabilityEnumeration] = field(
        default=None,
        metadata={
            "name": "AssistanceAvailability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    staffing: Optional[StaffingEnumeration] = field(
        default=None,
        metadata={
            "name": "Staffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accessibility_tool_list: List[AccessibilityToolEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityToolList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    languages: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Languages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    accessibility_trained_staff: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccessibilityTrainedStaff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    emergency_service_list: List[EmergencyServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "EmergencyServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    safety_facility_list: List[SafetyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SafetyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
