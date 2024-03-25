from dataclasses import dataclass, field
from typing import Optional, Union

from sdmx_ml.models.space_key_type import SpaceKeyType
from sdmx_ml.models.standard_from_vtl_mapping_method_type import (
    StandardFromVtlMappingMethodType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class FromVtlMappingType:
    """
    FromVtlMappingType defines the mapping method and filter used when mapping from
    VTL to SDMX.

    :ivar from_vtl_super_space: Identfies a super space of the mapped
        dataflow that the mapping applies to. This is a collection of
        references to the dimensions that make up the space.
    :ivar method: The mapping method used when mapping from VTL to SDMX.
        This is typically a StandardFromVtlMappingMethodType, but can be
        any other value to allow for non-standard methods. The implied
        default is Basic for single-measure VTL data structures and
        Unpivot for multi-meausre VTL data structures.
    """

    from_vtl_super_space: Optional[SpaceKeyType] = field(
        default=None,
        metadata={
            "name": "FromVtlSuperSpace",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    method: Optional[Union[StandardFromVtlMappingMethodType, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
