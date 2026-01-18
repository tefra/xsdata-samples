from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.maintainable_type import MaintainableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class HierarchyAssociationType(MaintainableType):
    """
    HierarchyAssociationType defines the structure of a hiearchy
    association, which links a hierarchy with and identifiable object in
    the context of another object (e.g. a dimension within the context of a
    dataflow).

    :ivar linked_hierarchy: The associated hierarchy.
    :ivar linked_object: Associates the Identifiable Artefact that needs
        the Hierarchy.
    :ivar context_object: The context within which the association is
        performed.
    """

    linked_hierarchy: str | None = field(
        default=None,
        metadata={
            "name": "LinkedHierarchy",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\.codelist\.Hierarchy=.+",
        },
    )
    linked_object: str | None = field(
        default=None,
        metadata={
            "name": "LinkedObject",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\)(\.[A-Za-z0-9_@$\-]+(\.[A-Za-z0-9_@$\-]+)*)?",
        },
    )
    context_object: str | None = field(
        default=None,
        metadata={
            "name": "ContextObject",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\)(\.[A-Za-z0-9_@$\-]+(\.[A-Za-z0-9_@$\-]+)*)?",
        },
    )
