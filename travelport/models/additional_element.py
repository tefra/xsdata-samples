from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class AdditionalElement:
    """
    To add or update reference data master records.

    Parameters
    ----------
    name
        Please provide other column names. This should match with exact
        database column name
    value
        Please provide corresponding value of the Name field
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )
