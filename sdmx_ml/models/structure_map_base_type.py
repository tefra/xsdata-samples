from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.maintainable_type import MaintainableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class StructureMapBaseType(MaintainableType):
    """
    StructureMapBaseType defines the base refinement of the
    StructureMapType.

    Its purpose is to retrict the urn attribute.
    """
