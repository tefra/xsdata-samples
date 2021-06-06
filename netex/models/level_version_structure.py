from dataclasses import dataclass, field
from typing import List, Optional
from .accessibility_assessment_versioned_child_structure import AccessibilityAssessmentVersionedChildStructure
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .parking_ref import ParkingRef
from .point_of_interest_ref import PointOfInterestRef
from .service_site_ref import ServiceSiteRef
from .site_ref import SiteRef
from .stop_place_ref import StopPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LevelVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Level_VersionStructure"

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
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PublicUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accessibility_assessment: Optional[AccessibilityAssessmentVersionedChildStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
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
    stop_place_ref: List[StopPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    parking_ref: List[ParkingRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    point_of_interest_ref: List[PointOfInterestRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    service_site_ref: List[ServiceSiteRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceSiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    site_ref: Optional[SiteRef] = field(
        default=None,
        metadata={
            "name": "SiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
