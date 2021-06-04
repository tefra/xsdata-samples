from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.access_feature_enumeration import AccessFeatureEnumeration
from netex.models.access_mode_enumeration import AccessModeEnumeration
from netex.models.access_summaries_rel_structure import AccessSummariesRelStructure
from netex.models.accessibility_assessment import AccessibilityAssessment
from netex.models.covered_enumeration import CoveredEnumeration
from netex.models.gated_enumeration import GatedEnumeration
from netex.models.lighting_enumeration import LightingEnumeration
from netex.models.link_sequence_version_structure import LinkSequenceVersionStructure
from netex.models.navigation_type_enumeration import NavigationTypeEnumeration
from netex.models.path_link_end_structure import PathLinkEndStructure
from netex.models.path_links_in_sequence_rel_structure import PathLinksInSequenceRelStructure
from netex.models.places_in_sequence_rel_structure import PlacesInSequenceRelStructure
from netex.models.public_use_enumeration import PublicUseEnumeration
from netex.models.site_facility_sets_rel_structure import SiteFacilitySetsRelStructure
from netex.models.transfer_duration_structure import TransferDurationStructure
from netex.models.transfer_refs_rel_structure import TransferRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NavigationPathVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "NavigationPath_VersionStructure"

    from_value: Optional[PathLinkEndStructure] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to: Optional[PathLinkEndStructure] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_modes: List[AccessModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    summaries: Optional[AccessSummariesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transfer_duration: Optional[TransferDurationStructure] = field(
        default=None,
        metadata={
            "name": "TransferDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_use: Optional[PublicUseEnumeration] = field(
        default=None,
        metadata={
            "name": "PublicUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    covered: Optional[CoveredEnumeration] = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gated: Optional[GatedEnumeration] = field(
        default=None,
        metadata={
            "name": "Gated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lighting: Optional[LightingEnumeration] = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_areas_wheelchair_accessible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllAreasWheelchairAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    person_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PersonCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    facilities: Optional[SiteFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_feature_list: List[AccessFeatureEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessFeatureList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    navigation_type: Optional[NavigationTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "NavigationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    places_in_sequence: Optional[PlacesInSequenceRelStructure] = field(
        default=None,
        metadata={
            "name": "placesInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_links_in_sequence: Optional[PathLinksInSequenceRelStructure] = field(
        default=None,
        metadata={
            "name": "pathLinksInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transfers: Optional[TransferRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
