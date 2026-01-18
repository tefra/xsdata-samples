from dataclasses import dataclass, field
from typing import Optional

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import Abstract
from crossref.models.org.crossref.access_indicators.program import (
    Program as AccessIndicatorsProgram,
)
from crossref.models.org.crossref.fundref.program import (
    Program as FundrefProgram,
)
from crossref.models.org.crossref.relations.program import (
    Program as RelationsProgram,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.acceptance_date import (
    AcceptanceDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import (
    Contributors,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.crossmark import Crossmark
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi import Doi
from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution import (
    Institution,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.intent_statement import (
    IntentStatement,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.item_number import (
    ItemNumber,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.pending_publication_language import (
    PendingPublicationLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publication import (
    Publication,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class PendingPublication:
    """
    Container for 'pending publication' metadata.

    Pending publication DOIs are used to create a DOI for a content item
    that is not yet available online or in print.
    """

    class Meta:
        name = "pending_publication"
        namespace = "http://www.crossref.org/schema/5.3.1"

    contributors: Contributors | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publication: Publication | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    titles: Titles | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    acceptance_date: AcceptanceDate | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    institution: list[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        },
    )
    item_number: list[ItemNumber] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 3,
        },
    )
    intent_statement: IntentStatement | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ncbi.nlm.nih.gov/JATS1",
        },
    )
    crossmark: Crossmark | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    program: FundrefProgram | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/fundref.xsd",
        },
    )
    program_1: AccessIndicatorsProgram | None = field(
        default=None,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/AccessIndicators.xsd",
        },
    )
    program_2: RelationsProgram | None = field(
        default=None,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/relations.xsd",
        },
    )
    doi: Doi | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    language: PendingPublicationLanguage | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
