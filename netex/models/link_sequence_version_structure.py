from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.authority_ref import AuthorityRef
from netex.models.common_section_point_members_rel_structure import CommonSectionPointMembersRelStructure
from netex.models.common_section_ref import CommonSectionRef
from netex.models.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from netex.models.destination_display_ref import DestinationDisplayRef
from netex.models.destination_display_view import DestinationDisplayView
from netex.models.direction_ref import DirectionRef
from netex.models.direction_type_enumeration import DirectionTypeEnumeration
from netex.models.direction_view import DirectionView
from netex.models.fare_point_in_pattern_ref_structure import FarePointInPatternRefStructure
from netex.models.fare_section_ref import FareSectionRef
from netex.models.flexible_line_ref import FlexibleLineRef
from netex.models.general_section_ref import GeneralSectionRef
from netex.models.info_links_rel_structure import InfoLinksRelStructure
from netex.models.journey_pattern_headways_rel_structure import JourneyPatternHeadwaysRelStructure
from netex.models.journey_pattern_layovers_rel_structure import JourneyPatternLayoversRelStructure
from netex.models.journey_pattern_ref import JourneyPatternRef
from netex.models.journey_pattern_run_times_rel_structure import JourneyPatternRunTimesRelStructure
from netex.models.journey_pattern_wait_times_rel_structure import JourneyPatternWaitTimesRelStructure
from netex.models.line_ref import LineRef
from netex.models.line_section_ref import LineSectionRef
from netex.models.link_in_link_sequence_versioned_child_structure import LinkInLinkSequenceVersionedChildStructure
from netex.models.link_sequence_refs_rel_structure import LinkSequenceRefsRelStructure
from netex.models.links_in_journey_pattern_rel_structure import LinksInJourneyPatternRelStructure
from netex.models.links_on_section_rel_structure import LinksOnSectionRelStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.models.operational_context_ref import OperationalContextRef
from netex.models.operator_ref import OperatorRef
from netex.models.parent_common_section_ref import ParentCommonSectionRef
from netex.models.point_on_line_sections_rel_structure import PointOnLineSectionsRelStructure
from netex.models.points_in_journey_pattern_rel_structure import PointsInJourneyPatternRelStructure
from netex.models.points_on_section_rel_structure import PointsOnSectionRelStructure
from netex.models.private_code import PrivateCode
from netex.models.projections_rel_structure import ProjectionsRelStructure
from netex.models.purpose_of_grouping_ref import PurposeOfGroupingRef
from netex.models.route_ref import RouteRef
from netex.models.route_view import RouteView
from netex.models.section_ref import SectionRef
from netex.models.section_type_enumeration import SectionTypeEnumeration
from netex.models.service_journey_pattern_ref import ServiceJourneyPatternRef
from netex.models.service_pattern_ref import ServicePatternRef
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.models.timing_pattern_ref import TimingPatternRef
from netex.models.transport_organisation_ref import TransportOrganisationRef
from netex.models.type_of_journey_pattern_ref import TypeOfJourneyPatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


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
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    projections: Optional[ProjectionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    info_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "infoLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sections_in_sequence: Optional["SectionsInSequenceRelStructure"] = field(
        default=None,
        metadata={
            "name": "sectionsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class JourneyPatternVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "JourneyPattern_VersionStructure"

    route_ref: Optional[RouteRef] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_view: Optional[RouteView] = field(
        default=None,
        metadata={
            "name": "RouteView",
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
    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_view: Optional[DestinationDisplayView] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_journey_pattern_ref: Optional[TypeOfJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "TypeOfJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_pattern_ref: Optional[TimingPatternRef] = field(
        default=None,
        metadata={
            "name": "TimingPatternRef",
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
    run_times: Optional[JourneyPatternRunTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wait_times: Optional[JourneyPatternWaitTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "waitTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    headways: Optional[JourneyPatternHeadwaysRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    layovers: Optional[JourneyPatternLayoversRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    points_in_sequence: Optional[PointsInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    links_in_sequence: Optional[LinksInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "linksInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
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
        }
    )
    used_in: Optional[LinkSequenceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "usedIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name_of_link_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfLinkClass",
            "type": "Attribute",
        }
    )


@dataclass
class Section1(LinkSequenceVersionStructure):
    class Meta:
        name = "Section_"
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class CommonSectionVersionStructure(SectionVersionStructure):
    class Meta:
        name = "CommonSection_VersionStructure"

    points_on_section: Optional[PointsOnSectionRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    members: Optional[CommonSectionPointMembersRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
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
        }
    )
    links_on_section: Optional[LinksOnSectionRelStructure] = field(
        default=None,
        metadata={
            "name": "linksOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class JourneyPattern2(JourneyPatternVersionStructure):
    class Meta:
        name = "JourneyPattern"
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class LineSectionVersionStructure(SectionVersionStructure):
    class Meta:
        name = "LineSection_VersionStructure"

    points_on_section: Optional[PointOnLineSectionsRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    members: Optional[CommonSectionPointMembersRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reverse_points_on_section: Optional[PointOnLineSectionsRelStructure] = field(
        default=None,
        metadata={
            "name": "reversePointsOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reverse_members: Optional[CommonSectionPointMembersRelStructure] = field(
        default=None,
        metadata={
            "name": "reverseMembers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    section_type: Optional[SectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "SectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_line_ref: List[FlexibleLineRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    line_ref: Optional[LineRef] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    authority_ref: List[AuthorityRef] = field(
        default_factory=list,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    operator_ref: List[OperatorRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    transport_organisation_ref: Optional[TransportOrganisationRef] = field(
        default=None,
        metadata={
            "name": "TransportOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class Section2(SectionVersionStructure):
    class Meta:
        name = "Section"
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class CommonSection(CommonSectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class FareSectionVersionStructure(GeneralSectionVersionStructure):
    class Meta:
        name = "FareSection_VersionStructure"

    service_journey_pattern_ref: List[ServiceJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    service_pattern_ref: List[ServicePatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServicePatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    dead_run_journey_pattern_ref: List[DeadRunJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    journey_pattern_ref: Optional[JourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern: Optional[JourneyPattern2] = field(
        default=None,
        metadata={
            "name": "JourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_point_in_pattern_ref: Optional[FarePointInPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "FromPointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_point_in_pattern_ref: Optional[FarePointInPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
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


@dataclass
class SectionInSequenceVersionedChildStructure(LinkInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "SectionInSequence_VersionedChildStructure"

    parent_common_section_ref: List[ParentCommonSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "ParentCommonSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    common_section_ref: List[CommonSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "CommonSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    line_section_ref: List[LineSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "LineSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    fare_section_ref: List[FareSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "FareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    general_section_ref: List[GeneralSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    section_ref: Optional[SectionRef] = field(
        default=None,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_section: List["FareSection"] = field(
        default_factory=list,
        metadata={
            "name": "FareSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    common_section: List[CommonSection] = field(
        default_factory=list,
        metadata={
            "name": "CommonSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    line_section: List[LineSection] = field(
        default_factory=list,
        metadata={
            "name": "LineSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    general_section: List[GeneralSection] = field(
        default_factory=list,
        metadata={
            "name": "GeneralSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    section: List[Section2] = field(
        default_factory=list,
        metadata={
            "name": "Section",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    netex_org_uk_netex_section: Optional[Section1] = field(
        default=None,
        metadata={
            "name": "Section_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
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
        }
    )
