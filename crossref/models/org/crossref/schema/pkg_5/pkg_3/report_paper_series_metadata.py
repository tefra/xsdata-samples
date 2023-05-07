from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.annotation import Abstract
from crossref.models.org.crossref.relations.program import Program
from crossref.models.org.crossref.schema.pkg_5.pkg_3.approval_date import ApprovalDate
from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import ArchiveLocations
from crossref.models.org.crossref.schema.pkg_5.pkg_3.citation_list import CitationList
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import Contributors
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution import Institution
from crossref.models.org.crossref.schema.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publication_date import PublicationDate
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher import Publisher
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_item import PublisherItem
from crossref.models.org.crossref.schema.pkg_5.pkg_3.report_paper_series_metadata_language import ReportPaperSeriesMetadataLanguage
from crossref.models.org.crossref.schema.pkg_5.pkg_3.report_paper_series_metadata_reference_distribution_opts import ReportPaperSeriesMetadataReferenceDistributionOpts
from crossref.models.org.crossref.schema.pkg_5.pkg_3.series_metadata import SeriesMetadata
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ReportPaperSeriesMetadata:
    """
    Container for the metadata related to a Technical Report or Working Paper that
    is part of a series.
    """
    class Meta:
        name = "report-paper_series_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    series_metadata: Optional[SeriesMetadata] = field(
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
    approval_date: List[ApprovalDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
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
    publisher: Optional[Publisher] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    institution: List[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        }
    )
    publisher_item: Optional[PublisherItem] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    contract_number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 2,
            "max_length": 255,
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
    program: Optional[Program] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/relations.xsd",
        }
    )
    language: Optional[ReportPaperSeriesMetadataLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reference_distribution_opts: ReportPaperSeriesMetadataReferenceDistributionOpts = field(
        default=ReportPaperSeriesMetadataReferenceDistributionOpts.NONE,
        metadata={
            "type": "Attribute",
        }
    )
