from dataclasses import dataclass, field
from typing import Optional
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

    default_connection_ref: Optional[DefaultConnectionRef] = field(
        default=None,
        metadata={
            "name": "DefaultConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_connection_ref: Optional[SiteConnectionRef] = field(
        default=None,
        metadata={
            "name": "SiteConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    stop_place_ref: Optional[StopPlaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_ref: Optional[ParkingRef] = field(
        default=None,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_ref: Optional[PointOfInterestRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_site_ref: Optional[ServiceSiteRef] = field(
        default=None,
        metadata={
            "name": "ServiceSiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
