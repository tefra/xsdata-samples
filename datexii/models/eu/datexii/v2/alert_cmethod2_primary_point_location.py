from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.alert_clocation import AlertCLocation
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AlertCMethod2PrimaryPointLocation:
    """
    The point (called Primary point) which is either a single point or at
    the downstream end of a linear road section.

    The point is specified by a reference to a point in a pre-defined
    ALERT-C location table.
    """

    alert_clocation: None | AlertCLocation = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    alert_cmethod2_primary_point_location_extension: None | ExtensionType = (
        field(
            default=None,
            metadata={
                "name": "alertCMethod2PrimaryPointLocationExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
