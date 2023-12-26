from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.annotation import Abstract
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
    """Container for 'pending publication' metadata.

    Pending publication DOIs are used to create a DOI for a content item
    that is not yet available online or in print.
    """

    class Meta:
        name = "pending_publication"
        namespace = "http://www.crossref.org/schema/5.3.1"

    contributors: Optional[Contributors] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publication: Optional[Publication] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    titles: Optional[Titles] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    acceptance_date: Optional[AcceptanceDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    institution: List[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        },
    )
    item_number: List[ItemNumber] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 3,
        },
    )
    intent_statement: Optional[IntentStatement] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    abstract: List[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ncbi.nlm.nih.gov/JATS1",
        },
    )
    crossmark: Optional[Crossmark] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    program: Optional[FundrefProgram] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/fundref.xsd",
        },
    )
    program_1: Optional[AccessIndicatorsProgram] = field(
        default=None,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/AccessIndicators.xsd",
        },
    )
    program_2: Optional[RelationsProgram] = field(
        default=None,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/relations.xsd",
        },
    )
    doi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 6,
            "max_length": 2048,
            "pattern": r"10\.[0-9]{4,9}/.{1,200}",
        },
    )
    language: Optional[PendingPublicationLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
