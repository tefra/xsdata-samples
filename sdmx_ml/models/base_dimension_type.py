from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.base_dimension_base_type import BaseDimensionBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class BaseDimensionType(BaseDimensionBaseType):
    """
    BaseDimensionType is an abstract base type which defines the basic
    structure of all dimensions.

    :ivar concept_role: ConceptRole references concepts which define
        roles which this dimension serves.
    :ivar position: The order of the dimensions in the key descriptor
        (DimensionList element) defines the order of the dimensions in
        the data structure. This position attribute explicitly specifies
        the position of the dimension in the data structure. It is
        optional and if specified must be consistent with the position
        of the dimension in the key descriptor.
    """

    concept_role: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ConceptRole",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\.conceptscheme\.Concept=.+",
        },
    )
    position: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
