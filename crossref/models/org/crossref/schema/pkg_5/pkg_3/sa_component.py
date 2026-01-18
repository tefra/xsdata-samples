from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.component_list import (
    ComponentList,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class SaComponent:
    """
    Container for component metadata if the component is being registered
    after the parent record/DOI is created.
    """

    class Meta:
        name = "sa_component"
        namespace = "http://www.crossref.org/schema/5.3.1"

    component_list: ComponentList | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    parent_doi: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 6,
            "max_length": 2048,
        },
    )
