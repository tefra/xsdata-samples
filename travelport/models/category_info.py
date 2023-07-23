from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.date_range_info import DateRangeInfo

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class CategoryInfo:
    """
    The information related to a particular category.

    Parameters
    ----------
    date_range_info
    title
        Title of a particular category.
    category
        Queue Category Number. 2 Character Alpha or Numeric Number. Either
        Alpha or Numeric Number is allowed.
    count
        The PNR count of a particular category.
    total_count
        The PNR count of a all categories.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    date_range_info: list[DateRangeInfo] = field(
        default_factory=list,
        metadata={
            "name": "DateRangeInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    title: None | str = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
        }
    )
    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    count: None | int = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Attribute",
            "required": True,
        }
    )
    total_count: None | int = field(
        default=None,
        metadata={
            "name": "TotalCount",
            "type": "Attribute",
            "required": True,
        }
    )
