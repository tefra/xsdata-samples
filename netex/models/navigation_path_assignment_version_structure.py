from dataclasses import dataclass, field
from typing import List, Optional
from .connection_ref import ConnectionRef
from .default_connection_ref import DefaultConnectionRef
from .navigation_path_ref import NavigationPathRef
from .parking_ref import ParkingRef
from .point_of_interest_ref import PointOfInterestRef
from .service_site_ref import ServiceSiteRef
from .site_connection_ref import SiteConnectionRef
from .site_ref import SiteRef
from .stop_assignment_version_structure import StopAssignmentVersionStructure
from .stop_place_ref import StopPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NavigationPathAssignmentVersionStructure(StopAssignmentVersionStructure):
    class Meta:
        name = "NavigationPathAssignment_VersionStructure"

    default_connection_ref: List[DefaultConnectionRef] = field(
        default_factory=list,
        metadata={
            "name": "DefaultConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    site_connection_ref: List[SiteConnectionRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    connection_ref: Optional[ConnectionRef] = field(
        default=None,
        metadata={
            "name": "ConnectionRef",
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
    navigation_path_ref: Optional[NavigationPathRef] = field(
        default=None,
        metadata={
            "name": "NavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )