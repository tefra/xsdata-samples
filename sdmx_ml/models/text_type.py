from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common"


@dataclass(frozen=True, kw_only=True)
class TextType:
    """
    TextType provides for a set of language-specific alternates to be
    provided for any human-readable constructs in the instance.

    :ivar value:
    :ivar lang: The xml:lang attribute specifies a language code for the
        text. If not supplied, the default language is assumed to be
        English.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
