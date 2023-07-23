from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.category_info import CategoryInfo

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class QueueInfo:
    """
    Parameters
    ----------
    category_info
    queue
    pseudo_city_code
    total_pnrcount
    pnrcount
    title
        Title of a queue.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    category_info: list[CategoryInfo] = field(
        default_factory=list,
        metadata={
            "name": "CategoryInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    queue: None | str = field(
        default=None,
        metadata={
            "name": "Queue",
            "type": "Attribute",
            "required": True,
        }
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        }
    )
    total_pnrcount: None | int = field(
        default=None,
        metadata={
            "name": "TotalPNRCount",
            "type": "Attribute",
            "required": True,
        }
    )
    pnrcount: None | int = field(
        default=None,
        metadata={
            "name": "PNRCount",
            "type": "Attribute",
            "required": True,
        }
    )
    title: None | str = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
        }
    )
