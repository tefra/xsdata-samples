from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.component import Component

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ComponentList:
    """
    Container for a group of components.
    """

    class Meta:
        name = "component_list"
        namespace = "http://www.crossref.org/schema/5.3.1"

    component: list[Component] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
