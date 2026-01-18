from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .accessibility_tool_enumeration import AccessibilityToolEnumeration
from .assistance_availability_enumeration import (
    AssistanceAvailabilityEnumeration,
)
from .assistance_facility_list import AssistanceFacilityList
from .emergency_service_enumeration import EmergencyServiceEnumeration
from .local_service_version_structure import LocalServiceVersionStructure
from .safety_facility_enumeration import SafetyFacilityEnumeration
from .staffing_enumeration import StaffingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "AssistanceService_VersionStructure"

    assistance_facility_list: None | AssistanceFacilityList = field(
        default=None,
        metadata={
            "name": "AssistanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    assistance_availability: None | AssistanceAvailabilityEnumeration = field(
        default=None,
        metadata={
            "name": "AssistanceAvailability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    staffing: None | StaffingEnumeration = field(
        default=None,
        metadata={
            "name": "Staffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_tool_list: Iterable[AccessibilityToolEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityToolList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    languages: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "Languages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    accessibility_trained_staff: None | bool = field(
        default=None,
        metadata={
            "name": "AccessibilityTrainedStaff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    emergency_service_list: Iterable[EmergencyServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "EmergencyServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    safety_facility_list: Iterable[SafetyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SafetyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
