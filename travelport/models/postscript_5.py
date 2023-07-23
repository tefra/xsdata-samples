from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_remark_5 import TypeRemark5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class Postscript5(TypeRemark5):
    """
    Postscript Notes.
    """
    class Meta:
        name = "Postscript"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
