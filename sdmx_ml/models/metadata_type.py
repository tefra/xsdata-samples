from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.attribute_type_1 import Attribute1

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/data/structurespecific"
)


@dataclass(frozen=True, kw_only=True)
class MetadataType(AnnotableType):
    """
    MetadataType describes the structure for reference metadata associated
    with datasets, groups, series or observations.

    :ivar attribute: Attribute elements hold the values being reported
        for reference metadata attributes, which were defined in the
        related metadata structure definition.
    """

    attribute: tuple[Attribute1, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/metadata/generic",
        },
    )
