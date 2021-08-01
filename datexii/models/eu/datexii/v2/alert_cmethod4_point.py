from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.alert_cdirection import AlertCDirection
from datexii.models.eu.datexii.v2.alert_cmethod4_primary_point_location import AlertCMethod4PrimaryPointLocation
from datexii.models.eu.datexii.v2.alert_cpoint import AlertCPoint
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AlertCMethod4Point(AlertCPoint):
    """
    A single point on the road network defined by reference to a point in a
    pre-defined ALERT-C location table plus an offset distance and which has an
    associated direction of traffic flow.
    """
    alert_cdirection: Optional[AlertCDirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod4_primary_point_location: Optional[AlertCMethod4PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod4_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
