from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.text import Text
from sdmx_ml.models.value_type import ValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class TextValueType(ValueType):
    """
    TextValueType is a restriction of ValueType that allows mutliple Text
    elements to expressed a text value in multiple languages.

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
    text: tuple[Text, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
