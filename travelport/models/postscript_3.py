from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_remark_3 import TypeRemark3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class Postscript3(TypeRemark3):
    """
    Postscript Notes.
    """
    class Meta:
        name = "Postscript"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
