from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class LinkType:
    """
    :ivar rel: The type of object that is being linked to.
    :ivar url: The url of the object being linked.
    :ivar urn: A SDMX registry urn of the object being linked (if
        applicable).
    :ivar type_value: The type of link (e.g. PDF, text, HTML, reference
        metadata).
    """

    rel: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    url: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    urn: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
