from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.alert_cdirection import AlertCDirection
from datexii.models.eu.datexii.v2.alert_cmethod2_primary_point_location import (
    AlertCMethod2PrimaryPointLocation,
)
from datexii.models.eu.datexii.v2.alert_cpoint import AlertCPoint
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AlertCMethod2Point(AlertCPoint):
    """
    A single point on the road network defined by reference to a point in a pre-
    defined ALERT-C location table and which has an associated direction of traffic
    flow.
    """

    alert_cdirection: Optional[AlertCDirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    alert_cmethod2_primary_point_location: Optional[
        AlertCMethod2PrimaryPointLocation
    ] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    alert_cmethod2_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
