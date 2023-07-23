from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_remark_4 import TypeRemark4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class Postscript4(TypeRemark4):
    """
    Postscript Notes.
    """
    class Meta:
        name = "Postscript"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
