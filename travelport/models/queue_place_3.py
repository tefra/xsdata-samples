from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.queue_selector_3 import QueueSelector3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class QueuePlace3:
    """
    Allow queue placement of a PNR at the time of booking to be used for Providers
    1G,1V,1P and 1J.

    Parameters
    ----------
    pseudo_city_code
        Pseudo City Code
    queue_selector
        Identifies the Queue Information to be selected for placing the UR
    """

    class Meta:
        name = "QueuePlace"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Element",
            "min_length": 2,
            "max_length": 10,
        },
    )
    queue_selector: list[QueueSelector3] = field(
        default_factory=list,
        metadata={
            "name": "QueueSelector",
            "type": "Element",
            "max_occurs": 999,
        },
    )
