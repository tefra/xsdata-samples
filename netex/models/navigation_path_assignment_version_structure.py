from dataclasses import dataclass, field
from typing import Optional, Union
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

    default_connection_ref_or_site_connection_ref_or_connection_ref: Optional[
        Union[DefaultConnectionRef, SiteConnectionRef, ConnectionRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DefaultConnectionRef",
                    "type": DefaultConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteConnectionRef",
                    "type": SiteConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ConnectionRef",
                    "type": ConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice: Optional[
        Union[
            StopPlaceRef,
            ParkingRef,
            PointOfInterestRef,
            ServiceSiteRef,
            SiteRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSiteRef",
                    "type": ServiceSiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteRef",
                    "type": SiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    navigation_path_ref: Optional[NavigationPathRef] = field(
        default=None,
        metadata={
            "name": "NavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
