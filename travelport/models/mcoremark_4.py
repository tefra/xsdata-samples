from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class Mcoremark4:
    """Information related to fare construction, free form text etc.

    of the MCO

    Parameters
    ----------
    value
    additional_rmk
        Indicates if the remark is additional remark or not.
    """

    class Meta:
        name = "MCORemark"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    additional_rmk: None | bool = field(
        default=None,
        metadata={
            "name": "AdditionalRmk",
            "type": "Attribute",
        },
    )
