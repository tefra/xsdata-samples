from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.format_mime_type import (
    FormatMimeType,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Format:
    """
    A narrative description of a component's file format and/or file
    extension.
    """

    class Meta:
        name = "format"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 130,
        },
    )
    mime_type: None | FormatMimeType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
