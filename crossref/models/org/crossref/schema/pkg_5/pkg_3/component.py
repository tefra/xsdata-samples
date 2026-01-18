from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.access_indicators.program import Program
from crossref.models.org.crossref.schema.pkg_5.pkg_3.component_language import (
    ComponentLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.component_parent_relation import (
    ComponentParentRelation,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import (
    Contributors,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.description import (
    Description,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi import Doi
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.format import Format
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publication_date import (
    PublicationDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Component:
    """
    Container for component metadata.

    Supplemental materials, figures, tables, and other items that can be
    considered a citeable part of a registered item may be registered as
    components.
    """

    class Meta:
        name = "component"
        namespace = "http://www.crossref.org/schema/5.3.1"

    titles: Titles | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    contributors: Contributors | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publication_date: PublicationDate | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    description: Description | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    format: Format | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    program: Program | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/AccessIndicators.xsd",
        },
    )
    doi_data: DoiData | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    doi: Doi | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parent_relation: ComponentParentRelation | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    reg_agency: str | None = field(
        default=None,
        metadata={
            "name": "reg-agency",
            "type": "Attribute",
        },
    )
    language: ComponentLanguage | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    component_size: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
