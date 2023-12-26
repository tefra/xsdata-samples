from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.queue_selector_1 import QueueSelector1

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class QueuePseudoCitySelector:
    """
    Need to specify the PseudoCityCode and Queue details.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_selector: None | QueueSelector1 = field(
        default=None,
        metadata={
            "name": "QueueSelector",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        },
    )
