from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.representation_type import RepresentationType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataAttributeRepresentationType(RepresentationType):
    """
    MetadataAttributeRepresentationType defines the possible local
    representations of a metadata attribute.
    """

    min_occurs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    max_occurs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
