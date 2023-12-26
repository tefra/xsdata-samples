from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Type, Union
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .authority_ref import AuthorityRef
from .common_section_point_members_rel_structure import (
    CommonSectionPointMembersRelStructure,
)
from .common_section_ref import CommonSectionRef
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .destination_display_ref import DestinationDisplayRef
from .destination_display_view import DestinationDisplayView
from .direction_ref import DirectionRef
from .direction_type_enumeration import DirectionTypeEnumeration
from .direction_view import DirectionView
from .fare_point_in_pattern_ref_structure import FarePointInPatternRefStructure
from .fare_section_ref import FareSectionRef
from .flexible_line_ref import FlexibleLineRef
from .general_section_ref import GeneralSectionRef
from .info_links_rel_structure import InfoLinksRelStructure
from .journey_pattern_headways_rel_structure import (
    JourneyPatternHeadwaysRelStructure,
)
from .journey_pattern_layovers_rel_structure import (
    JourneyPatternLayoversRelStructure,
)
from .journey_pattern_ref import JourneyPatternRef
from .journey_pattern_run_times_rel_structure import (
    JourneyPatternRunTimesRelStructure,
)
from .journey_pattern_wait_times_rel_structure import (
    JourneyPatternWaitTimesRelStructure,
)
from .line_ref import LineRef
from .line_section_ref import LineSectionRef
from .link_in_link_sequence_versioned_child_structure import (
    LinkInLinkSequenceVersionedChildStructure,
)
from .link_sequence_refs_rel_structure import LinkSequenceRefsRelStructure
from .links_in_journey_pattern_rel_structure import (
    LinksInJourneyPatternRelStructure,
)
from .links_on_section_rel_structure import LinksOnSectionRelStructure
from .multilingual_string import MultilingualString
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .operational_context_ref import OperationalContextRef
from .operator_ref import OperatorRef
from .parent_common_section_ref import ParentCommonSectionRef
from .point_on_line_sections_rel_structure import (
    PointOnLineSectionsRelStructure,
)
from .points_in_journey_pattern_rel_structure import (
    PointsInJourneyPatternRelStructure,
)
from .points_on_section_rel_structure import PointsOnSectionRelStructure
from .private_code import PrivateCode
from .projections_rel_structure import ProjectionsRelStructure
from .purpose_of_grouping_ref import PurposeOfGroupingRef
from .route_ref import RouteRef
from .route_view import RouteView
from .section_ref import SectionRef
from .section_type_enumeration import SectionTypeEnumeration
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .timing_pattern_ref import TimingPatternRef
from .type_of_journey_pattern_ref import TypeOfJourneyPatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SectionInSequenceVersionedChildStructure(
    LinkInLinkSequenceVersionedChildStructure
):
    class Meta:
        name = "SectionInSequence_VersionedChildStructure"

    choice_1: Optional[
        Union[
            ParentCommonSectionRef,
            CommonSectionRef,
            LineSectionRef,
            FareSectionRef,
            GeneralSectionRef,
            SectionRef,
            "FareSection",
            "CommonSection",
            "LineSection",
            "GeneralSection",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParentCommonSectionRef",
                    "type": ParentCommonSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommonSectionRef",
                    "type": CommonSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineSectionRef",
                    "type": LineSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareSectionRef",
                    "type": FareSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSectionRef",
                    "type": GeneralSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SectionRef",
                    "type": SectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareSection",
                    "type": Type["FareSection"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommonSection",
                    "type": Type["CommonSection"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineSection",
                    "type": Type["LineSection"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSection",
                    "type": Type["GeneralSection"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class SectionInSequence(SectionInSequenceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class SectionsInSequenceRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "sectionsInSequence_RelStructure"

    section_in_sequence: List[SectionInSequence] = field(
        default_factory=list,
        metadata={
            "name": "SectionInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )


@dataclass
class LinkSequenceVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "LinkSequence_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    projections: Optional[ProjectionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    info_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "infoLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sections_in_sequence: Optional[SectionsInSequenceRelStructure] = field(
        default=None,
        metadata={
            "name": "sectionsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class JourneyPatternVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "JourneyPattern_VersionStructure"

    route_ref_or_route_view: Optional[Union[RouteRef, RouteView]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RouteRef",
                    "type": RouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteView",
                    "type": RouteView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_ref_or_direction_view: Optional[
        Union[DirectionRef, DirectionView]
    ] = field(
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
    destination_display_ref_or_destination_display_view: Optional[
        Union[DestinationDisplayRef, DestinationDisplayView]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DestinationDisplayRef",
                    "type": DestinationDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayView",
                    "type": DestinationDisplayView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_journey_pattern_ref: Optional[TypeOfJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "TypeOfJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_pattern_ref: Optional[TimingPatternRef] = field(
        default=None,
        metadata={
            "name": "TimingPatternRef",
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
    run_times: Optional[JourneyPatternRunTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wait_times: Optional[JourneyPatternWaitTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "waitTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    headways: Optional[JourneyPatternHeadwaysRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    layovers: Optional[JourneyPatternLayoversRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    points_in_sequence: Optional[PointsInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    links_in_sequence: Optional[LinksInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "linksInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class SectionVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "Section_VersionStructure"

    purpose_of_grouping_ref: Optional[PurposeOfGroupingRef] = field(
        default=None,
        metadata={
            "name": "PurposeOfGroupingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    used_in: Optional[LinkSequenceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "usedIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name_of_link_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfLinkClass",
            "type": "Attribute",
        },
    )


@dataclass
class CommonSectionVersionStructure(SectionVersionStructure):
    class Meta:
        name = "CommonSection_VersionStructure"

    points_on_section_or_members: Optional[
        Union[
            PointsOnSectionRelStructure, CommonSectionPointMembersRelStructure
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "pointsOnSection",
                    "type": PointsOnSectionRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "members",
                    "type": CommonSectionPointMembersRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class GeneralSectionVersionStructure(SectionVersionStructure):
    class Meta:
        name = "GeneralSection_VersionStructure"

    points_on_section: Optional[PointsOnSectionRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    links_on_section: Optional[LinksOnSectionRelStructure] = field(
        default=None,
        metadata={
            "name": "linksOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class JourneyPattern(JourneyPatternVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class LineSectionVersionStructure(SectionVersionStructure):
    class Meta:
        name = "LineSection_VersionStructure"

    points_on_section_or_members: Optional[
        Union[
            PointOnLineSectionsRelStructure,
            CommonSectionPointMembersRelStructure,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "pointsOnSection",
                    "type": PointOnLineSectionsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "members",
                    "type": CommonSectionPointMembersRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    reverse_points_on_section_or_reverse_members: Optional[
        Union[
            PointOnLineSectionsRelStructure,
            CommonSectionPointMembersRelStructure,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "reversePointsOnSection",
                    "type": PointOnLineSectionsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "reverseMembers",
                    "type": CommonSectionPointMembersRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    section_type: Optional[SectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "SectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_line_ref_or_line_ref: Optional[
        Union[FlexibleLineRef, LineRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    authority_ref_or_operator_ref: Optional[
        Union[AuthorityRef, OperatorRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class CommonSection(CommonSectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class FareSectionVersionStructure(GeneralSectionVersionStructure):
    class Meta:
        name = "FareSection_VersionStructure"

    choice: Optional[
        Union[
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
            JourneyPattern,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPattern",
                    "type": JourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    from_point_in_pattern_ref: Optional[
        FarePointInPatternRefStructure
    ] = field(
        default=None,
        metadata={
            "name": "FromPointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_point_in_pattern_ref: Optional[FarePointInPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class GeneralSection(GeneralSectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class LineSection(LineSectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class FareSection(FareSectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
