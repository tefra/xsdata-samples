from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.reference_data_search_item_type import (
    ReferenceDataSearchItemType,
)

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class ReferenceDataSearchItem:
    """
    Container for a Reference Data search item that includes its type and
    how to search / identify the item either via code or value.

    Parameters
    ----------
    code
        Code uniquely identifying the reference data item (e.g. ORD for
        Airport item).
    name
        Value of the reference data item that may not uniquely identify a
        single Reference Data item (e.g. Chicago for Airport would return
        ORD and MDW).
    type_value
        Reference data type
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "min_length": 1,
            "white_space": "collapse",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "min_length": 1,
            "white_space": "collapse",
        },
    )
    type_value: None | ReferenceDataSearchItemType = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
