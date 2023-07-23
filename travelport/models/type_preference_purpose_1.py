from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypePreferencePurpose1(Enum):
    """Specify the preference purpose.

    (ie. Business, Leisure, etc)
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
