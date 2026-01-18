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
from crossref.models.org.crossref.schema.pkg_5.pkg_3.approval_date import (
    ApprovalDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import (
    ArchiveLocations,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.citation_list import (
    CitationList,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import (
    Contributors,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.crossmark import Crossmark
from crossref.models.org.crossref.schema.pkg_5.pkg_3.designators import (
    Designators,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.edition_number import (
    EditionNumber,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher import Publisher
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_item import (
    PublisherItem,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.standard_metadata_language import (
    StandardMetadataLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.standard_metadata_publication_status import (
    StandardMetadataPublicationStatus,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.standard_metadata_reference_distribution_opts import (
    StandardMetadataReferenceDistributionOpts,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.standards_body import (
    StandardsBody,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class StandardMetadata:
    """
    Container for the metadata related to a Standard that is not part of a
    series.
    """

    class Meta:
        name = "standard_metadata"
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
    designators: Designators = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    edition_number: None | EditionNumber = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    approval_date: None | ApprovalDate = field(
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
    publisher: None | Publisher = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    standards_body: StandardsBody = field(
        metadata={
            "type": "Element",
            "required": True,
        }
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
    publication_status: None | StandardMetadataPublicationStatus = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    language: None | StandardMetadataLanguage = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reference_distribution_opts: StandardMetadataReferenceDistributionOpts = (
        field(
            default=StandardMetadataReferenceDistributionOpts.NONE,
            metadata={
                "type": "Attribute",
            },
        )
    )
