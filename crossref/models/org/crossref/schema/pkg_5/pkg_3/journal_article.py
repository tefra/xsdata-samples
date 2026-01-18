from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import Abstract
from crossref.models.org.crossref.access_indicators.program import (
    Program as AccessIndicatorsProgram,
)
from crossref.models.org.crossref.clinicaltrials.program import (
    Program as ClinicaltrialsProgram,
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
from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import (
    ArchiveLocations,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.citation_list import (
    CitationList,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.component_list import (
    ComponentList,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import (
    Contributors,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.crossmark import Crossmark
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.journal_article_language import (
    JournalArticleLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.journal_article_publication_type import (
    JournalArticlePublicationType,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.journal_article_reference_distribution_opts import (
    JournalArticleReferenceDistributionOpts,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.pages import Pages
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publication_date import (
    PublicationDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_item import (
    PublisherItem,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.scn_policies import (
    ScnPolicies,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class JournalArticle:
    """
    Container for all information about a single journal article.
    """

    class Meta:
        name = "journal_article"
        namespace = "http://www.crossref.org/schema/5.3.1"

    titles: list[Titles] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 20,
        },
    )
    contributors: None | Contributors = field(
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
    publication_date: list[PublicationDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
    acceptance_date: None | AcceptanceDate = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pages: None | Pages = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publisher_item: None | PublisherItem = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    crossmark: None | Crossmark = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    program: None | FundrefProgram = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/fundref.xsd",
        },
    )
    program_1: None | AccessIndicatorsProgram = field(
        default=None,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/AccessIndicators.xsd",
        },
    )
    program_2: None | ClinicaltrialsProgram = field(
        default=None,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/clinicaltrials.xsd",
        },
    )
    program_3: None | RelationsProgram = field(
        default=None,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/relations.xsd",
        },
    )
    archive_locations: None | ArchiveLocations = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    scn_policies: None | ScnPolicies = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    doi_data: DoiData = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    citation_list: None | CitationList = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    component_list: None | ComponentList = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publication_type: JournalArticlePublicationType = field(
        default=JournalArticlePublicationType.FULL_TEXT,
        metadata={
            "type": "Attribute",
        },
    )
    language: None | JournalArticleLanguage = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reference_distribution_opts: JournalArticleReferenceDistributionOpts = (
        field(
            default=JournalArticleReferenceDistributionOpts.NONE,
            metadata={
                "type": "Attribute",
            },
        )
    )
