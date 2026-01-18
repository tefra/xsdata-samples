from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from decimal import Decimal

from .access_feature_enumeration import AccessFeatureEnumeration
from .access_mode_enumeration import AccessModeEnumeration
from .accessibility_assessment import AccessibilityAssessment
from .accessibility_assessment_ref import AccessibilityAssessmentRef
from .border_type_enumeration import BorderTypeEnumeration
from .covered_enumeration import CoveredEnumeration
from .flooring_type_enumeration import FlooringTypeEnumeration
from .gated_enumeration import GatedEnumeration
from .gradient_enumeration import GradientEnumeration
from .lighting_enumeration import LightingEnumeration
from .link_version_structure import LinkVersionStructure
from .multilingual_string import MultilingualString
from .passage_type_enumeration import PassageTypeEnumeration
from .path_direction_enumeration import PathDirectionEnumeration
from .path_link_end_structure import PathLinkEndStructure
from .presentation_structure import PresentationStructure
from .public_use_enumeration import PublicUseEnumeration
from .site_facility_sets_rel_structure import SiteFacilitySetsRelStructure
from .tactile_warning_strip_enumeration import TactileWarningStripEnumeration
from .tilt_type_enumeration import TiltTypeEnumeration
from .transfer_duration_structure import TransferDurationStructure
from .transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinkVersionStructure(LinkVersionStructure):
    class Meta:
        name = "PathLink_VersionStructure"

    from_value: None | PathLinkEndStructure = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to: None | PathLinkEndStructure = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_assessment_ref_or_accessibility_assessment: (
        None | AccessibilityAssessmentRef | AccessibilityAssessment
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccessibilityAssessmentRef",
                    "type": AccessibilityAssessmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessibilityAssessment",
                    "type": AccessibilityAssessment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
    public_use: None | PublicUseEnumeration = field(
        default=None,
        metadata={
            "name": "PublicUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    covered: None | CoveredEnumeration = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gated: None | GatedEnumeration = field(
        default=None,
        metadata={
            "name": "Gated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lighting: None | LightingEnumeration = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    all_areas_wheelchair_accessible: None | bool = field(
        default=None,
        metadata={
            "name": "AllAreasWheelchairAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    person_capacity: None | int = field(
        default=None,
        metadata={
            "name": "PersonCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    presentation: None | PresentationStructure = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: None | SiteFacilitySetsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    towards: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Towards",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    back: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Back",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_steps: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "MinimumHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_width: None | Decimal = field(
        default=None,
        metadata={
            "name": "MinimumWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    allowed_use: None | PathDirectionEnumeration = field(
        default=None,
        metadata={
            "name": "AllowedUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transition: None | TransitionEnumeration = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gradient: None | int = field(
        default=None,
        metadata={
            "name": "Gradient",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gradient_type: None | GradientEnumeration = field(
        default=None,
        metadata={
            "name": "GradientType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tilt_angle: None | int = field(
        default=None,
        metadata={
            "name": "TiltAngle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tilt_type: None | TiltTypeEnumeration = field(
        default=None,
        metadata={
            "name": "TiltType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_feature_type: None | AccessFeatureEnumeration = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passage_type: None | PassageTypeEnumeration = field(
        default=None,
        metadata={
            "name": "PassageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flooring_type: None | FlooringTypeEnumeration = field(
        default=None,
        metadata={
            "name": "FlooringType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    right_side_border: None | BorderTypeEnumeration = field(
        default=None,
        metadata={
            "name": "RightSideBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    left_side_border: None | BorderTypeEnumeration = field(
        default=None,
        metadata={
            "name": "LeftSideBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_warning_strip: None | TactileWarningStripEnumeration = field(
        default=None,
        metadata={
            "name": "TactileWarningStrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_guiding_strip: None | bool = field(
        default=None,
        metadata={
            "name": "TactileGuidingStrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_flow_per_minute: None | int = field(
        default=None,
        metadata={
            "name": "MaximumFlowPerMinute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_duration: None | TransferDurationStructure = field(
        default=None,
        metadata={
            "name": "TransferDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
