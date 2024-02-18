from dataclasses import dataclass, field
from typing import Optional
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
    """Container for component metadata.

    Supplemental materials, figures, tables, and other items that can be
    considered a citeable part of a registered item may be registered as
    components.
    """

    class Meta:
        name = "component"
        namespace = "http://www.crossref.org/schema/5.3.1"

    titles: Optional[Titles] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    contributors: Optional[Contributors] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publication_date: Optional[PublicationDate] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    format: Optional[Format] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    program: Optional[Program] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/AccessIndicators.xsd",
        },
    )
    doi_data: Optional[DoiData] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    doi: Optional[Doi] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parent_relation: Optional[ComponentParentRelation] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    reg_agency: Optional[str] = field(
        default=None,
        metadata={
            "name": "reg-agency",
            "type": "Attribute",
        },
    )
    language: Optional[ComponentLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    component_size: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
