from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.situation_record import SituationRecord

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class TrafficElement(SituationRecord):
    """
    An event which is not planned by the traffic operator, which is
    affecting, or has the potential to affect traffic flow.
    """

    traffic_element_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "trafficElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
