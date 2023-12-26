from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeContactType1(Enum):
    """A code for categorizing contactees based on a role they might play.

    Examples include Emergency Contact, Regular Contact, Backup Contact,
    etc.
    """

    ADMIN_ASSISTANT = "Admin Assistant"
    AFTER_HOUR = "After Hour"
    ASSISTANT = "Assistant"
    BACKUP = "Backup"
    CHILD = "Child"
    COLLEAGUE = "Colleague"
    EMERGENCY = "Emergency"
    MANAGER = "Manager"
    OTHER = "Other"
    PARENT = "Parent"
    REGULAR = "Regular"
    RELATIVE = "Relative"
    SERVICE_CENTER = "Service Center"
    SPOUSE = "Spouse"
    SUPERVISOR = "Supervisor"
    TICKET_AUTHORIZER = "Ticket Authorizer"
    TRAVEL_ARRANGER = "Travel Arranger"
    TRIP_AUTHORIZATION = "Trip Authorization"
