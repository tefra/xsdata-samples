from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.alert_clocation import AlertCLocation
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.offset_distance import OffsetDistance

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AlertCMethod4PrimaryPointLocation:
    """The point (called Primary point) which is either a single point or at the
    downstream end of a linear road section.

    The point is specified by a reference to a point in a pre-defined
    ALERT-C location table plus a non-negative offset distance.
    """

    alert_clocation: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    offset_distance: Optional[OffsetDistance] = field(
        default=None,
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    alert_cmethod4_primary_point_location_extension: Optional[
        ExtensionType
    ] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
