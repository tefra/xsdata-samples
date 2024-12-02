from dataclasses import dataclass, field
from typing import ForwardRef, Union

from sdmx_ml.models.empty_type import EmptyType
from sdmx_ml.models.optional_local_dimension_reference_type import (
    OptionalLocalDimensionReferenceType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class AttributeRelationshipType:
    """
    AttributeRelationshipType defines the structure for stating the relationship
    between an attribute and other data structure definition components.
    """

    choice: tuple[
        Union[
            "AttributeRelationshipType.Dataflow",
            OptionalLocalDimensionReferenceType,
            str,
            "AttributeRelationshipType.Observation",
        ],
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Dataflow",
                    "type": ForwardRef("AttributeRelationshipType.Dataflow"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Dimension",
                    "type": OptionalLocalDimensionReferenceType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Group",
                    "type": str,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                    "pattern": r"[A-Za-z0-9_@$\-]+",
                },
                {
                    "name": "Observation",
                    "type": ForwardRef(
                        "AttributeRelationshipType.Observation"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )

    @dataclass(frozen=True)
    class Dataflow(EmptyType):
        pass

    @dataclass(frozen=True)
    class Observation(EmptyType):
        pass
