from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeProfileLinkRelationship2(Enum):
    """
    Specify the one way relationship between two profiles.
    """

    COLLEAGUE = "Colleague"
    EMPLOYEE = "Employee"
    ADMIN_ASSISTANT = "Admin Assistant"
    SUPERVISOR = "Supervisor"
    MANAGER = "Manager"
    PROJECT_MANAGER = "Project Manager"
    LEAD = "Lead"
    SPOUSE = "Spouse"
    SIGNIFICANT_OTHER = "Significant Other"
    PARENT = "Parent"
    CHILD = "Child"
    SIBLING = "Sibling"
    RELATIVE = "Relative"
    FRIEND = "Friend"
    INFANT = "Infant"
    TRAVEL_ARRANGER = "Travel Arranger"
    AUTHORIZER = "Authorizer"
    OTHER = "Other"
