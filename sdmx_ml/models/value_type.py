from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.structured_text import StructuredText
from sdmx_ml.models.text import Text

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common"


@dataclass(frozen=True, kw_only=True)
class ValueType:
    """
    ValueType is an abstract class that is the basis for any component
    value that cannot be simply represented as a space-normalized value
    (e.g. in an XML attribute).

    Although its content is mixed, it should be restricted so that only
    character data or the Text or Structured text is used. See
    StringValueType, IntValueType, ObserverationalTimeValueType,
    TextValueType, and StructuredTextValueType for details.
    """

    content: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Text",
                    "type": Text,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common",
                },
                {
                    "name": "StructuredText",
                    "type": StructuredText,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common",
                },
            ),
        },
    )
