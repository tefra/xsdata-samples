from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union
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

    from_value: Optional[PathLinkEndStructure] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to: Optional[PathLinkEndStructure] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
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
    accessibility_assessment_ref_or_accessibility_assessment: Optional[
        Union[AccessibilityAssessmentRef, AccessibilityAssessment]
    ] = field(
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
    access_modes: List[AccessModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    public_use: Optional[PublicUseEnumeration] = field(
        default=None,
        metadata={
            "name": "PublicUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    covered: Optional[CoveredEnumeration] = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gated: Optional[GatedEnumeration] = field(
        default=None,
        metadata={
            "name": "Gated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lighting: Optional[LightingEnumeration] = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    all_areas_wheelchair_accessible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllAreasWheelchairAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    person_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PersonCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: Optional[SiteFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    towards: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Towards",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    back: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Back",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_steps: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    allowed_use: Optional[PathDirectionEnumeration] = field(
        default=None,
        metadata={
            "name": "AllowedUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transition: Optional[TransitionEnumeration] = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gradient: Optional[int] = field(
        default=None,
        metadata={
            "name": "Gradient",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gradient_type: Optional[GradientEnumeration] = field(
        default=None,
        metadata={
            "name": "GradientType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tilt_angle: Optional[int] = field(
        default=None,
        metadata={
            "name": "TiltAngle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tilt_type: Optional[TiltTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TiltType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_feature_type: Optional[AccessFeatureEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passage_type: Optional[PassageTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PassageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flooring_type: Optional[FlooringTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FlooringType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    right_side_border: Optional[BorderTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RightSideBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    left_side_border: Optional[BorderTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LeftSideBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_warning_strip: Optional[TactileWarningStripEnumeration] = field(
        default=None,
        metadata={
            "name": "TactileWarningStrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_guiding_strip: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileGuidingStrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_flow_per_minute: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumFlowPerMinute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_duration: Optional[TransferDurationStructure] = field(
        default=None,
        metadata={
            "name": "TransferDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
