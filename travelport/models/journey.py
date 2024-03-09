from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from travelport.models.air_segment_ref import AirSegmentRef

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Journey:
    """
    Information about all connecting segment list and total traveling time.

    Parameters
    ----------
    air_segment_ref
    travel_time
        Total traveling time that is difference between the departure time
        of the first segment and the arrival time of the last segments for
        that particular entire set of connection.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_ref: list[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    travel_time: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
        },
    )
