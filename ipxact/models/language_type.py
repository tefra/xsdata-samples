from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class LanguageType:
    """
    :ivar value:
    :ivar strict: A value of 'true' indicates that this value must match
        the language being generated for the design.
    """

    class Meta:
        name = "languageType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    strict: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
