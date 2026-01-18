from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.identifier_id_type import (
    IdentifierIdType,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Identifier:
    """
    A public standard identifier that can be used to uniquely identify the
    item being registered.
    """

    class Meta:
        name = "identifier"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
    id_type: IdentifierIdType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
