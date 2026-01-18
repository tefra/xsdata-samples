from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.lane_enum import LaneEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class LocationCharacteristicsOverride:
    """
    Location characteristics which override values set in the referenced
    measurement point.

    :ivar measurement_lanes_override: Overrides for this single measured
        value instance the lane(s) defined for the set of measurements.
    :ivar reversed_flow: Indicates that the direction of flow for the
        measured lane(s) is the reverse of the normal direction of
        traffic flow.  Default is "no", which indicates traffic flow is
        in the normal sense as defined by the referenced measurement
        point.
    :ivar location_characteristics_override_extension:
    """

    measurement_lanes_override: LaneEnum | None = field(
        default=None,
        metadata={
            "name": "measurementLanesOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    reversed_flow: bool | None = field(
        default=None,
        metadata={
            "name": "reversedFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    location_characteristics_override_extension: ExtensionType | None = (
        field(
            default=None,
            metadata={
                "name": "locationCharacteristicsOverrideExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
