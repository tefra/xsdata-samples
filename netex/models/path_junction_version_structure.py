from dataclasses import dataclass, field
from typing import Optional
from netex.models.covered_enumeration import CoveredEnumeration
from netex.models.gated_enumeration import GatedEnumeration
from netex.models.lighting_enumeration import LightingEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.point_version_structure import PointVersionStructure
from netex.models.public_use_enumeration import PublicUseEnumeration
from netex.models.site_component_ref_structure import SiteComponentRefStructure
from netex.models.site_facility_sets_rel_structure import SiteFacilitySetsRelStructure
from netex.models.zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathJunctionVersionStructure(PointVersionStructure):
    class Meta:
        name = "PathJunction_VersionStructure"

    parent_zone_ref: Optional[ZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentZoneRef",
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
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_component_ref: Optional[SiteComponentRefStructure] = field(
        default=None,
        metadata={
            "name": "SiteComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
