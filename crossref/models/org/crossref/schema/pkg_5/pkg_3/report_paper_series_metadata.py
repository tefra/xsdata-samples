from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import Abstract
from crossref.models.org.crossref.relations.program import Program
from crossref.models.org.crossref.schema.pkg_5.pkg_3.approval_date import (
    ApprovalDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import (
    ArchiveLocations,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.citation_list import (
    CitationList,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contract_number import (
    ContractNumber,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import (
    Contributors,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.edition_number import (
    EditionNumber,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution import (
    Institution,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publication_date import (
    PublicationDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher import Publisher
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_item import (
    PublisherItem,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.report_paper_series_metadata_language import (
    ReportPaperSeriesMetadataLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.report_paper_series_metadata_reference_distribution_opts import (
    ReportPaperSeriesMetadataReferenceDistributionOpts,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.series_metadata import (
    SeriesMetadata,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles
from crossref.models.org.crossref.schema.pkg_5.pkg_3.volume import Volume

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ReportPaperSeriesMetadata:
    """
    Container for the metadata related to a Technical Report or Working
    Paper that is part of a series.
    """

    class Meta:
        name = "report-paper_series_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    series_metadata: SeriesMetadata | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    contributors: Contributors | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    titles: Titles | None = field(
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
    volume: list[Volume] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    edition_number: EditionNumber | None = field(
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
    approval_date: list[ApprovalDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        },
    )
    isbn: list[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        },
    )
    publisher: Publisher | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    institution: list[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        },
    )
    publisher_item: PublisherItem | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    contract_number: ContractNumber | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    archive_locations: ArchiveLocations | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    doi_data: DoiData | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    citation_list: CitationList | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    program: Program | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/relations.xsd",
        },
    )
    language: ReportPaperSeriesMetadataLanguage | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reference_distribution_opts: ReportPaperSeriesMetadataReferenceDistributionOpts = field(
        default=ReportPaperSeriesMetadataReferenceDistributionOpts.NONE,
        metadata={
            "type": "Attribute",
        },
    )
