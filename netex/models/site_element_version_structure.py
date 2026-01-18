from collections.abc import Iterable
from dataclasses import dataclass, field

from .access_mode_enumeration import AccessModeEnumeration
from .accessibility_assessment import AccessibilityAssessment
from .addressable_place_version_structure import (
    AddressablePlaceVersionStructure,
)
from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .covered_enumeration import CoveredEnumeration
from .gated_enumeration import GatedEnumeration
from .lighting_enumeration import LightingEnumeration
from .multilingual_string import MultilingualString
from .presentation_structure import PresentationStructure
from .public_use_enumeration import PublicUseEnumeration
from .site_facility_sets_rel_structure import SiteFacilitySetsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteElementVersionStructure(AddressablePlaceVersionStructure):
    class Meta:
        name = "SiteElement_VersionStructure"

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
    name_suffix: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: AlternativeNamesRelStructure | None = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cross_road: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "CrossRoad",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    landmark: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Landmark",
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
