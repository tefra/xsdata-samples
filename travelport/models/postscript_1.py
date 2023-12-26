from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_remark_1 import TypeRemark1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class Postscript1(TypeRemark1):
    """
    Postscript Notes.
    """

    class Meta:
        name = "Postscript"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
