from dataclasses import dataclass
from .meeting_restriction_ref_structure import MeetingRestrictionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MeetingRestrictionRef(MeetingRestrictionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
