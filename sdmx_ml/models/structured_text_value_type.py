from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.structured_text import StructuredText
from sdmx_ml.models.value_type import ValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class StructuredTextValueType(ValueType):
    """
    StructuredTextValueType is a restriction of ValueType that allows
    mutliple StructuredText (XHTML mixed content) elements to expressed a
    text value in multiple languages.

    The content of this should be restricted in its use to only allow a
    langue code (xml:lang) to be used once within an element of this type.
    """

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    structured_text: tuple[StructuredText, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "StructuredText",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
