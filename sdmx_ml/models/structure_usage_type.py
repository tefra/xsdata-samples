from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.maintainable_type import MaintainableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class StructureUsageType(MaintainableType):
    """
    StructureUsageType is an abstract base type for all structure usages.

    It contains a reference to a structure. Concrete instances of this type
    should restrict the type of structure referenced.

    :ivar structure: Structure references the structure (data structure
        or metadata structure definition) which the structure usage is
        based upon. Implementations will have to refine the type to use
        a concrete structure reference (i.e. either a data structure or
        metadata structure definition reference).
    """

    structure: str | None = field(
        default=None,
        metadata={
            "name": "Structure",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\.datastructure\.DataStructure=.+|.+\.metadatastructure\.MetadataStructure=.+",
        },
    )
