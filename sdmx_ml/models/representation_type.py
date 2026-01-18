from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.coded_text_format_type import CodedTextFormatType
from sdmx_ml.models.text_format_type import TextFormatType
from sdmx_ml.models.unbounded_code_type import UnboundedCodeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class RepresentationType:
    """
    RepresentationType is an abstract type that defines a representation.

    Because the type of item schemes that are allowed as the an enumeration
    vary based on the object in which this is defined, this type is
    abstract to force that the enumeration reference be restricted to the
    proper type of item scheme reference.

    :ivar text_format_or_enumeration_or_enumeration_format:
    :ivar min_occurs: The minOccurs attribute indicates the minimum
        number of value that must be reported for the component.
    :ivar max_occurs: The maxOccurs attribute indicates the maximum
        number of values that can be reported for the component.
    """

    text_format_or_enumeration_or_enumeration_format: tuple[
        TextFormatType | str | CodedTextFormatType, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TextFormat",
                    "type": TextFormatType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Enumeration",
                    "type": str,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                    "pattern": r".+\.codelist\.Codelist=.+|.+\.codelist\.ValueList=.+",
                },
                {
                    "name": "EnumerationFormat",
                    "type": CodedTextFormatType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
            "max_occurs": 2,
        },
    )
    min_occurs: int = field(
        default=1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: None | int | UnboundedCodeType = field(
        default=None,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
