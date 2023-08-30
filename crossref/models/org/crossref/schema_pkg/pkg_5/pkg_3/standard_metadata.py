from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.annotation import Abstract
from crossref.models.org.crossref.access_indicators.program import Program as AccessIndicatorsProgram
from crossref.models.org.crossref.fundref.program import Program as FundrefProgram
from crossref.models.org.crossref.relations.program import Program as RelationsProgram
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.approval_date import ApprovalDate
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.archive_locations import ArchiveLocations
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.citation_list import CitationList
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.contributors import Contributors
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.crossmark import Crossmark
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.designators import Designators
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.publisher import Publisher
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.publisher_item import PublisherItem
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.standard_metadata_language import StandardMetadataLanguage
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.standard_metadata_publication_status import StandardMetadataPublicationStatus
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.standard_metadata_reference_distribution_opts import StandardMetadataReferenceDistributionOpts
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.standards_body import StandardsBody
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class StandardMetadata:
    """
    Container for the metadata related to a Standard that is not part of a series.
    """
    class Meta:
        name = "standard_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

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
            "required": True,
        }
    )
    abstract: List[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ncbi.nlm.nih.gov/JATS1",
        }
    )
    designators: Optional[Designators] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
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
    approval_date: Optional[ApprovalDate] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    isbn: List[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        }
    )
    publisher: Optional[Publisher] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    standards_body: Optional[StandardsBody] = field(
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
            "required": True,
        }
    )
    citation_list: Optional[CitationList] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    publication_status: Optional[StandardMetadataPublicationStatus] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[StandardMetadataLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reference_distribution_opts: StandardMetadataReferenceDistributionOpts = field(
        default=StandardMetadataReferenceDistributionOpts.NONE,
        metadata={
            "type": "Attribute",
        }
    )
