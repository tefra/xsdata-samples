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
from crossref.models.org.crossref.schema.pkg_5.pkg_3.crossmark import Crossmark
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
from crossref.models.org.crossref.schema.pkg_5.pkg_3.report_paper_metadata_language import (
    ReportPaperMetadataLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.report_paper_metadata_reference_distribution_opts import (
    ReportPaperMetadataReferenceDistributionOpts,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.scn_policies import (
    ScnPolicies,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ReportPaperMetadata:
    """
    Container for the metadata related to a Technical Report or Working
    Paper.
    """

    class Meta:
        name = "report-paper_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

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
            "required": True,
        },
    )
    edition_number: EditionNumber | None = field(
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
    archive_locations: ArchiveLocations | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    scn_policies: ScnPolicies | None = field(
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
    language: ReportPaperMetadataLanguage | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reference_distribution_opts: ReportPaperMetadataReferenceDistributionOpts = field(
        default=ReportPaperMetadataReferenceDistributionOpts.NONE,
        metadata={
            "type": "Attribute",
        },
    )
