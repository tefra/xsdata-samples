from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.attribute_representation_type import (
    AttributeRepresentationType,
)
from sdmx_ml.models.component_type import ComponentType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataAttributeUsageBaseType(ComponentType):
    """MetadataAttributeUsageBaseType is the abstract base refinement of a metadata
    attribute usage.

    Since this is a usage of metadata attribute already defined in
    metadata structure, the typical id, concept identity, and
    representation are excluded in place of a local refernce to the
    metadata attribute being used.
    """

    concept_identity: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    local_representation: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    id: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
