from dataclasses import dataclass, field
from typing import Optional

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
from crossref.models.org.crossref.schema.pkg_5.pkg_3.component_number import (
    ComponentNumber,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.content_item_component_type import (
    ContentItemComponentType,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.content_item_language import (
    ContentItemLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.content_item_publication_type import (
    ContentItemPublicationType,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.content_item_reference_distribution_opts import (
    ContentItemReferenceDistributionOpts,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import (
    Contributors,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.crossmark import Crossmark
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
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


@dataclass
class ContentItem:
    """
    A segment of a book, report, or standard for which a DOI is being
    registered.

    Most commonly used for book chapters.
    """

    class Meta:
        name = "content_item"
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
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ncbi.nlm.nih.gov/JATS1",
        },
    )
    component_number: ComponentNumber | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publication_date: list[PublicationDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        },
    )
    acceptance_date: AcceptanceDate | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pages: Pages | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publisher_item: PublisherItem | None = field(
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
    program_2: ClinicaltrialsProgram | None = field(
        default=None,
        metadata={
            "name": "program",
            "type": "Element",
            "namespace": "http://www.crossref.org/clinicaltrials.xsd",
        },
    )
    program_3: RelationsProgram | None = field(
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
            "required": True,
        },
    )
    citation_list: CitationList | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    component_list: ComponentList | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    component_type: ContentItemComponentType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    level_sequence_number: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 9,
            "total_digits": 1,
        },
    )
    publication_type: ContentItemPublicationType = field(
        default=ContentItemPublicationType.FULL_TEXT,
        metadata={
            "type": "Attribute",
        },
    )
    language: ContentItemLanguage | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reference_distribution_opts: ContentItemReferenceDistributionOpts = field(
        default=ContentItemReferenceDistributionOpts.NONE,
        metadata={
            "type": "Attribute",
        },
    )
