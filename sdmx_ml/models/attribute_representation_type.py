from dataclasses import dataclass, field
from typing import Union

from sdmx_ml.models.representation_type import RepresentationType
from sdmx_ml.models.unbounded_code_type import UnboundedCodeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class AttributeRepresentationType(RepresentationType):
    """AttributeRepresentationType defines the representation for a data attribute.

    A data attribute can be text (including XHTML and multi-lingual
    values), a simple value, or an enumerated value.
    """

    max_occurs: Union[int, UnboundedCodeType] = field(
        default=1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
