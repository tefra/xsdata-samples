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

    from_value: PathLinkEndStructure | None = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to: PathLinkEndStructure | None = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_assessment_ref_or_accessibility_assessment: (
        AccessibilityAssessmentRef | AccessibilityAssessment | None
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
    towards: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Towards",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    back: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Back",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_steps: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "MinimumHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_width: Decimal | None = field(
        default=None,
        metadata={
            "name": "MinimumWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    allowed_use: PathDirectionEnumeration | None = field(
        default=None,
        metadata={
            "name": "AllowedUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transition: TransitionEnumeration | None = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gradient: int | None = field(
        default=None,
        metadata={
            "name": "Gradient",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gradient_type: GradientEnumeration | None = field(
        default=None,
        metadata={
            "name": "GradientType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tilt_angle: int | None = field(
        default=None,
        metadata={
            "name": "TiltAngle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tilt_type: TiltTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "TiltType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_feature_type: AccessFeatureEnumeration | None = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passage_type: PassageTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "PassageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flooring_type: FlooringTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "FlooringType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    right_side_border: BorderTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "RightSideBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    left_side_border: BorderTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "LeftSideBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_warning_strip: TactileWarningStripEnumeration | None = field(
        default=None,
        metadata={
            "name": "TactileWarningStrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_guiding_strip: bool | None = field(
        default=None,
        metadata={
            "name": "TactileGuidingStrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_flow_per_minute: int | None = field(
        default=None,
        metadata={
            "name": "MaximumFlowPerMinute",
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
