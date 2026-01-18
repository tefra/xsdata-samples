from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.alert_cdirection import AlertCDirection
from datexii.models.eu.datexii.v2.alert_clinear import AlertCLinear
from datexii.models.eu.datexii.v2.alert_cmethod2_primary_point_location import (
    AlertCMethod2PrimaryPointLocation,
)
from datexii.models.eu.datexii.v2.alert_cmethod2_secondary_point_location import (
    AlertCMethod2SecondaryPointLocation,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class AlertCMethod2Linear(AlertCLinear):
    """
    A linear section along a road between two points, Primary and
    Secondary, which are pre-defined in an ALERT-C location table.

    Direction is FROM the Secondary point TO the Primary point, i.e. the
    Primary point is downstream of the Secondary point.
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
    alert_cmethod2_secondary_point_location: AlertCMethod2SecondaryPointLocation = field(
        metadata={
            "name": "alertCMethod2SecondaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    alert_cmethod2_linear_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "alertCMethod2LinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
