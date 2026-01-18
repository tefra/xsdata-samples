from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True, kw_only=True)
class Xhtmltype:
    """
    XHTMLType allows for mixed content of text and XHTML tags.

    When using this type, one will have to provide a reference to the XHTML
    schema, since the processing of the tags within this type is strict,
    meaning that they are validated against the XHTML schema provided.
    """

    class Meta:
        name = "XHTMLType"

    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
