from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.component_list_type import ComponentListType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class ComponentList(ComponentListType):
    """
    ComponentList is an abstract element that serves as a substitution head
    for all component lists.

    Concrete instances of this must use a concrete instance of
    ComponentListType.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
