from __future__ import annotations

from dataclasses import dataclass, field

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
from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import (
    ArchiveLocations,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.book_metadata_language import (
    BookMetadataLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.book_metadata_reference_distribution_opts import (
    BookMetadataReferenceDistributionOpts,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.citation_list import (
    CitationList,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import (
    Contributors,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.crossmark import Crossmark
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.edition_number import (
    EditionNumber,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.noisbn import Noisbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publication_date import (
    PublicationDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher import Publisher
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_item import (
    PublisherItem,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class BookMetadata:
    """
    A container for all title-level metadata for a single book that is not
    part of a series or set.
    """

    class Meta:
        name = "book_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    contributors: None | Contributors = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    titles: Titles = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ncbi.nlm.nih.gov/JATS1",
        },
    )
    edition_number: None | EditionNumber = field(
        default=None,
        metadata={
            "type": "Element",
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
    isbn: list[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        },
    )
    noisbn: None | Noisbn = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publisher: list[Publisher] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
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
    program_2: None | RelationsProgram = field(
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
    doi_data: None | DoiData = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    citation_list: None | CitationList = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    language: None | BookMetadataLanguage = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reference_distribution_opts: BookMetadataReferenceDistributionOpts = field(
        default=BookMetadataReferenceDistributionOpts.NONE,
        metadata={
            "type": "Attribute",
        },
    )
