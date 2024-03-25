from dataclasses import dataclass, field
from typing import Optional, Tuple, Union

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.structured_text import StructuredText
from sdmx_ml.models.text import Text

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/metadata/generic"
)


@dataclass(frozen=True)
class AttributeType1(AnnotableType):
    """AttributeType defines the structure for a reported metadata attribute.

    A value for the attribute can be supplied as either a single value
    (enumerated or non-enumerated single value), or multi-lingual text
    values (either structured or unstructured). Optional child
    attributes ar also available if the metadata attribute definition
    defines nested metadata attributes.

    :ivar value_or_text_or_structured_text:
    :ivar attribute: Att contains the reported metadata attribute values
        for the child metadata attributes.
    :ivar id: The id attribute identifies the metadata attribute that
        the value is being reported for.
    """

    class Meta:
        name = "AttributeType"

    value_or_text_or_structured_text: Tuple[
        Union[object, Text, StructuredText], ...
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Value",
                    "type": object,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/metadata/generic",
                },
                {
                    "name": "Text",
                    "type": Text,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
                },
                {
                    "name": "StructuredText",
                    "type": StructuredText,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
                },
            ),
        },
    )
    attribute: Tuple["Attribute1", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/metadata/generic",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )


@dataclass(frozen=True)
class Attribute1(AttributeType1):
    """Att elements hold the reported values for a given metadata attribute.

    These values conform to the definition of the meatadata attribute in
    the metadata structure definition.
    """

    class Meta:
        name = "Attribute"
        namespace = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/metadata/generic"
