from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import Abstract
from crossref.models.org.crossref.access_indicators.program import Program as AccessIndicatorsProgram
from crossref.models.org.crossref.fundref.program import Program as FundrefProgram
from crossref.models.org.crossref.relations.program import Program as RelationsProgram
from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import ArchiveLocations
from crossref.models.org.crossref.schema.pkg_5.pkg_3.citation_list import CitationList
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import Contributors
from crossref.models.org.crossref.schema.pkg_5.pkg_3.crossmark import Crossmark
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.language_atts_language import LanguageAttsLanguage
from crossref.models.org.crossref.schema.pkg_5.pkg_3.noisbn import Noisbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publication_date import PublicationDate
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher import Publisher
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_item import PublisherItem
from crossref.models.org.crossref.schema.pkg_5.pkg_3.reference_distribution_opts_att_reference_distribution_opts import ReferenceDistributionOptsAttReferenceDistributionOpts
from crossref.models.org.crossref.schema.pkg_5.pkg_3.set_metadata import SetMetadata
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class BookSetMetadata:
    """
    A container for all information that applies to an individual volume of a
    book set.
    """
    class Meta:
        name = "book_set_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    set_metadata: Optional[SetMetadata] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    contributors: Optional[Contributors] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    titles: Optional[Titles] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    abstract: List[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ncbi.nlm.nih.gov/JATS1",
        }
    )
    volume: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 32,
        }
    )
    edition_number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 15,
        }
    )
    publication_date: List[PublicationDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
        }
    )
    isbn: List[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        }
    )
    noisbn: Optional[Noisbn] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    publisher: Optional[Publisher] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    publisher_item: Optional[PublisherItem] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    crossmark: Optional[Crossmark] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    program: Optional[FundrefProgram] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/fundref.xsd",
        }
    )
    program_1: Optional[AccessIndicatorsProgram] = field(
        default=None,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/AccessIndicators.xsd",
        }
    )
    program_2: Optional[RelationsProgram] = field(
        default=None,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/relations.xsd",
        }
    )
    archive_locations: Optional[ArchiveLocations] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    doi_data: Optional[DoiData] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    citation_list: Optional[CitationList] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    language: Optional[LanguageAttsLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reference_distribution_opts: ReferenceDistributionOptsAttReferenceDistributionOpts = field(
        default=ReferenceDistributionOptsAttReferenceDistributionOpts.NONE,
        metadata={
            "type": "Attribute",
        }
    )
