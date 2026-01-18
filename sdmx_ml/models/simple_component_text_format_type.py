from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.basic_component_text_format_type import (
    BasicComponentTextFormatType,
)
from sdmx_ml.models.simple_data_type import SimpleDataType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class SimpleComponentTextFormatType(BasicComponentTextFormatType):
    """
    SimpleComponentTextFormatType is a restricted version of the
    BasicComponentTextFormatType that does not allow for multi-lingual
    values.
    """

    text_type: SimpleDataType = field(
        default=SimpleDataType.STRING,
        metadata={
            "name": "textType",
            "type": "Attribute",
        },
    )
    is_multi_lingual: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
