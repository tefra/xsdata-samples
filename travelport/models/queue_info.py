from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.category_info import CategoryInfo

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass(kw_only=True)
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
        },
    )
    queue: str = field(
        metadata={
            "name": "Queue",
            "type": "Attribute",
            "required": True,
        }
    )
    pseudo_city_code: str = field(
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        }
    )
    total_pnrcount: int = field(
        metadata={
            "name": "TotalPNRCount",
            "type": "Attribute",
            "required": True,
        }
    )
    pnrcount: int = field(
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
        },
    )
