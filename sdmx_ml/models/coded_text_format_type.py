from dataclasses import dataclass, field
from typing import Any, Optional

from sdmx_ml.models.code_data_type import CodeDataType
from sdmx_ml.models.simple_component_text_format_type import (
    SimpleComponentTextFormatType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CodedTextFormatType(SimpleComponentTextFormatType):
    """
    CodedTextFormatType is a restricted version of the
    SimpleComponentTextFormatType that only allows factets and text types
    applicable to codes.

    Although the time facets permit any value, an actual code identifier
    does not support the necessary characters for time. Therefore these
    facets should not contain time in their values.

    :ivar sentinel_value: SentinelValue defines a value that has a
        special meaning within the text format representation of a
        component.
    :ivar text_type:
    :ivar decimals:
    """

    sentinel_value: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    text_type: Optional[CodeDataType] = field(
        default=None,
        metadata={
            "name": "textType",
            "type": "Attribute",
        },
    )
    decimals: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
