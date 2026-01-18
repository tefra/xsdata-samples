from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.value_type import ValueType

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific"
)


@dataclass(frozen=True)
class CompType(AnnotableType):
    """
    CompType is the abstract base for any component value (e.g. a data or
    metadata attribute, or a measure) that cannot be represented as an XML
    attribute.

    For example, a repeated value, a text value in multiple languages, or a
    value with structured text (XHTML) cannot be expressed as an XML
    attribute. This type is meant to be restricted based on the component
    to restrict the cardinality and type of its Value element to conform to
    the compoent definition. The type of the value element should be
    restricted to common:SimpleValueType, common:TextValueType, or
    common:StructuredValueType. In addition, the id attribute should be
    restricted to be a fixed value with the component identifier. This
    restricted type based on the component can then be used on Comp
    elements by using the xsi:type to state the component being expressed
    and refine the contents of the element to the values allowed by the
    component.
    """

    value: tuple[ValueType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_\-]*",
        },
    )
