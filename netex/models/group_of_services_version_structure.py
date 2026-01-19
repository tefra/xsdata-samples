from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .day_type_ref_structure import DayTypeRefStructure
from .destination_display_refs_rel_structure import (
    DestinationDisplayRefsRelStructure,
)
from .direction_ref import DirectionRef
from .direction_type import DirectionType
from .direction_view import DirectionView
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .group_of_services_end_point_derived_view_structure import (
    GroupOfServicesEndPointDerivedViewStructure,
)
from .group_of_services_members_rel_structure import (
    GroupOfServicesMembersRelStructure,
)
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfServicesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfServices_VersionStructure"

    day_types: None | GroupOfServicesVersionStructure.DayTypes = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_type: None | DirectionType = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_ref_or_direction_view: None | DirectionRef | DirectionView = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "DirectionRef",
                        "type": DirectionRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "DirectionView",
                        "type": DirectionView,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
    origin: None | GroupOfServicesEndPointDerivedViewStructure = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination: None | GroupOfServicesEndPointDerivedViewStructure = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_displays: None | DestinationDisplayRefsRelStructure = field(
        default=None,
        metadata={
            "name": "destinationDisplays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: None | GroupOfServicesMembersRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: None | NoticeAssignmentsRelStructure = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class DayTypes:
        day_type_ref: Sequence[DayTypeRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "DayTypeRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
