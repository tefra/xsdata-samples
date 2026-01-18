from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.alert_cdirection import AlertCDirection
from datexii.models.eu.datexii.v2.alert_clinear import AlertCLinear
from datexii.models.eu.datexii.v2.alert_cmethod4_primary_point_location import (
    AlertCMethod4PrimaryPointLocation,
)
from datexii.models.eu.datexii.v2.alert_cmethod4_secondary_point_location import (
    AlertCMethod4SecondaryPointLocation,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AlertCMethod4Linear(AlertCLinear):
    """
    A linear section along a road between two points, Primary and
    Secondary, which are pre-defined ALERT-C locations plus offset
    distance.

    Direction is FROM the Secondary point TO the Primary point, i.e. the
    Primary point is downstream of the Secondary point.
    """

    alert_cdirection: None | AlertCDirection = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    alert_cmethod4_primary_point_location: (
        None | AlertCMethod4PrimaryPointLocation
    ) = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    alert_cmethod4_secondary_point_location: (
        None | AlertCMethod4SecondaryPointLocation
    ) = field(
        default=None,
        metadata={
            "name": "alertCMethod4SecondaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    alert_cmethod4_linear_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "alertCMethod4LinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
