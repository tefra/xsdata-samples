from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.alert_cdirection import AlertCDirection
from datexii.models.eu.datexii.v2.alert_cmethod2_primary_point_location import (
    AlertCMethod2PrimaryPointLocation,
)
from datexii.models.eu.datexii.v2.alert_cpoint import AlertCPoint
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class AlertCMethod2Point(AlertCPoint):
    """
    A single point on the road network defined by reference to a point in a
    pre-defined ALERT-C location table and which has an associated
    direction of traffic flow.
    """

    alert_cdirection: AlertCDirection = field(
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod2_primary_point_location: AlertCMethod2PrimaryPointLocation = field(
        metadata={
            "name": "alertCMethod2PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod2_point_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "alertCMethod2PointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
