from dataclasses import dataclass, field

from sdmx_ml.models.space_key_type import SpaceKeyType
from sdmx_ml.models.standard_to_vtl_mapping_method_type import (
    StandardToVtlMappingMethodType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ToVtlMappingType:
    """
    ToVtlMappingType defines the mapping method and filter used when
    mapping from SDMX to VTL.

    :ivar to_vtl_sub_space: Identfies a sub space of the mapped dataflow
        that the mapping applies to. This is a collection of references
        to the dimensions that make up the space.
    :ivar method: The mapping method used when mapping from SDMX to VTL.
        This is typically a StandardToVtlMappingMethodType, but can be
        any other value to allow for non-standard methods. The implied
        default is Basic.
    """

    to_vtl_sub_space: SpaceKeyType | None = field(
        default=None,
        metadata={
            "name": "ToVtlSubSpace",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    method: StandardToVtlMappingMethodType | str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
