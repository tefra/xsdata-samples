from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.maintainable_type import MaintainableType

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/metadata/generic"
)


@dataclass(frozen=True, kw_only=True)
class MetadataSetBaseType(MaintainableType):
    """
    MetadataSetBaseType defines the base refinement of the MetadataSetType.

    Its purpose is to restrict the urn attribute.
    """
