from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypePreferencePurpose2(StrEnum):
    """
    Specify the preference purpose. (ie.

    Business, Leisure, etc).
    """

    BUSINESS = "Business"
    LEISURE = "Leisure"
    MEETING = "Meeting"
    GROUP = "Group"
    INCENTIVE = "Incentive"
    GOVERNMENT = "Government"
    DOMESTIC = "Domestic"
    INTERNATIONAL = "International"
    CONFERENCE = "Conference"
    LOYALTY = "Loyalty"
