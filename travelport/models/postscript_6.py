from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_remark_6 import TypeRemark6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class Postscript6(TypeRemark6):
    """
    Postscript Notes.
    """

    class Meta:
        name = "Postscript"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
