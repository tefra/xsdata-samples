from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.day_type_ref_structure import DayTypeRefStructure
from netex.models.destination_display_refs_rel_structure import DestinationDisplayRefsRelStructure
from netex.models.direction_ref import DirectionRef
from netex.models.direction_type_enumeration import DirectionTypeEnumeration
from netex.models.direction_view import DirectionView
from netex.models.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.models.group_of_services_end_point_derived_view_structure import GroupOfServicesEndPointDerivedViewStructure
from netex.models.group_of_services_members_rel_structure import GroupOfServicesMembersRelStructure
from netex.models.notice_assignments_rel_structure import NoticeAssignmentsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfServicesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfServices_VersionStructure"

    day_types: Optional["GroupOfServicesVersionStructure.DayTypes"] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_view: Optional[DirectionView] = field(
        default=None,
        metadata={
            "name": "DirectionView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    origin: Optional[GroupOfServicesEndPointDerivedViewStructure] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination: Optional[GroupOfServicesEndPointDerivedViewStructure] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_displays: Optional[DestinationDisplayRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "destinationDisplays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    members: Optional[GroupOfServicesMembersRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class DayTypes:
        day_type_ref: List[DayTypeRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "DayTypeRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )
