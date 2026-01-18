from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class ContinuityOverrideRemark:
    """
    A textual remark container to hold any printable text. (max 512 chars).

    Parameters
    ----------
    value
    category
        This is remark category is always MCT. 'Minimum Connect Time'
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    category: str = field(
        default="MCT",
        metadata={
            "name": "Category",
            "type": "Attribute",
            "max_length": 10,
        },
    )
