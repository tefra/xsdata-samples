from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.obs_dimensions_code_type import ObsDimensionsCodeType
from sdmx_ml.models.payload_structure_type import PayloadStructureType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class MetadataStructureTypeAbstract(PayloadStructureType):
    """
    MetadataStructureType is an abstract base type the forms the basis of
    the structural information for any metadata message.

    A reference to the metadata structure definition or a metadataflow must
    be provided. This can be used to determine the structure of the
    message.
    """

    class Meta:
        name = "MetadataStructureType"

    dimension_at_observation: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    explicit_measures: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
