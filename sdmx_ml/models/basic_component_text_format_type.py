from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.basic_component_data_type import BasicComponentDataType
from sdmx_ml.models.text_format_type import TextFormatType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class BasicComponentTextFormatType(TextFormatType):
    """
    BasicComponentTextFormatType is a restricted version of the
    TextFormatType that restricts the text type to the representations
    allowed for all components except for target objects.
    """

    text_type: BasicComponentDataType = field(
        default=BasicComponentDataType.STRING,
        metadata={
            "name": "textType",
            "type": "Attribute",
        },
    )
