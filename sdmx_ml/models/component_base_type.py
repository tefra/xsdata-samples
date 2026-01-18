from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.identifiable_type import IdentifiableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class ComponentBaseType(IdentifiableType):
    """
    ComponentBaseType is an abstract type that only serves the purpose of
    forming the base for the actual ComponentType.

    It only restricts the format of the id attribute to the NCNameIDType.
    """
