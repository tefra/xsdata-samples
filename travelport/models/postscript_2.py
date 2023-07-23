from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_remark_2 import TypeRemark2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class Postscript2(TypeRemark2):
    """
    Postscript Notes.
    """
    class Meta:
        name = "Postscript"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
