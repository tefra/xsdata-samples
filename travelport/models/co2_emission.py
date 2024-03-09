from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Co2Emission:
    """
    Carbon emission values.

    Parameters
    ----------
    air_segment_ref
        The segment reference
    value
        The CO2 emission value for the air segment
    """

    class Meta:
        name = "CO2Emission"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Attribute",
        },
    )
    value: None | float = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        },
    )
