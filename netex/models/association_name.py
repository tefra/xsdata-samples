from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class AssociationName:
    class Meta:
        name = "associationName"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
