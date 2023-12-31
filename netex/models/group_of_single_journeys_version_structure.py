from dataclasses import dataclass, field
from typing import Optional
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .single_journey_refs_rel_structure import SingleJourneyRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfSingleJourneysVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfSingleJourneys_VersionStructure"

    members: Optional[SingleJourneyRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
