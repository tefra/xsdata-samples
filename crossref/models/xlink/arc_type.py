from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.xlink.actuate_type import ActuateType
from crossref.models.xlink.show_type import ShowType
from crossref.models.xlink.type_type import TypeType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass(kw_only=True)
class ArcType:
    """
    :ivar type_value:
    :ivar arcrole:
    :ivar title:
    :ivar show:
    :ivar actuate:
    :ivar from_value:
    :ivar to: from and to have default behavior when values are missing
    """

    class Meta:
        name = "arcType"

    type_value: TypeType = field(
        init=False,
        default=TypeType.ARC,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        },
    )
    arcrole: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    from_value: None | str = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    to: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
