from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MeetingPointEnumeration(StrEnum):
    MEETING_POINT = "meetingPoint"
    GROUP_MEETING = "groupMeeting"
    SCHOOL_MEETING_POINT = "schoolMeetingPoint"
    OTHER = "other"
