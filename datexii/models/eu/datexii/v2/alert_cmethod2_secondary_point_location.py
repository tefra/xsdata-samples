from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.alert_clocation import AlertCLocation
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AlertCMethod2SecondaryPointLocation:
    """
    The point (called Secondary point) which is at the upstream end of a
    linear road section.

    The point is specified by a reference to a point in a pre-defined
    ALERT-C location table.
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
    alert_cmethod2_secondary_point_location_extension: Optional[
        ExtensionType
    ] = field(
        default=None,
        metadata={
            "name": "alertCMethod2SecondaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
