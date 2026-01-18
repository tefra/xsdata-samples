from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.maintainable_type import MaintainableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ItemSchemeMapBaseType(MaintainableType):
    """
    ItemSchemeMapBaseType is an abstract base type which forms the basis
    for the ItemSchemeMapType.
    """
