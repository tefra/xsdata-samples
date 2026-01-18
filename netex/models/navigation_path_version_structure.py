from collections.abc import Iterable
from dataclasses import dataclass, field

from .access_feature_enumeration import AccessFeatureEnumeration
from .access_mode_enumeration import AccessModeEnumeration
from .access_summaries_rel_structure import AccessSummariesRelStructure
from .accessibility_assessment import AccessibilityAssessment
from .covered_enumeration import CoveredEnumeration
from .gated_enumeration import GatedEnumeration
from .lighting_enumeration import LightingEnumeration
from .navigation_type_enumeration import NavigationTypeEnumeration
from .path_link_end_structure import PathLinkEndStructure
from .path_links_in_sequence_rel_structure import (
    PathLinksInSequenceRelStructure,
)
from .places_in_sequence_rel_structure import PlacesInSequenceRelStructure
from .presentation_structure import PresentationStructure
from .public_use_enumeration import PublicUseEnumeration
from .sections_in_sequence_rel_structure import LinkSequenceVersionStructure
from .site_facility_sets_rel_structure import SiteFacilitySetsRelStructure
from .transfer_duration_structure import TransferDurationStructure
from .transfer_refs_rel_structure import TransferRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NavigationPathVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "NavigationPath_VersionStructure"

    from_value: PathLinkEndStructure | None = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to: PathLinkEndStructure | None = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_assessment: AccessibilityAssessment | None = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_modes: Iterable[AccessModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    summaries: AccessSummariesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_duration: TransferDurationStructure | None = field(
        default=None,
        metadata={
            "name": "TransferDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_use: PublicUseEnumeration | None = field(
        default=None,
        metadata={
            "name": "PublicUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    covered: CoveredEnumeration | None = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gated: GatedEnumeration | None = field(
        default=None,
        metadata={
            "name": "Gated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lighting: LightingEnumeration | None = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    all_areas_wheelchair_accessible: bool | None = field(
        default=None,
        metadata={
            "name": "AllAreasWheelchairAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    person_capacity: int | None = field(
        default=None,
        metadata={
            "name": "PersonCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    presentation: PresentationStructure | None = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: SiteFacilitySetsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_feature_list: Iterable[AccessFeatureEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessFeatureList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    navigation_type: NavigationTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "NavigationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    places_in_sequence: PlacesInSequenceRelStructure | None = field(
        default=None,
        metadata={
            "name": "placesInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_links_in_sequence: PathLinksInSequenceRelStructure | None = field(
        default=None,
        metadata={
            "name": "pathLinksInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfers: TransferRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
