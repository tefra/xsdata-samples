from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.access_indicators.program import (
    Program as AccessIndicatorsProgram,
)
from crossref.models.org.crossref.fundref.program import (
    Program as FundrefProgram,
)
from crossref.models.org.crossref.relations.program import (
    Program as RelationsProgram,
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
from crossref.models.org.crossref.schema.pkg_5.pkg_3.database_date import (
    DatabaseDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.dataset_dataset_type import (
    DatasetDatasetType,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.description import (
    Description,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.format import Format
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_item import (
    PublisherItem,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Dataset:
    """
    dataset is used to capture information about one or more database
    records or collections.
    """

    class Meta:
        name = "dataset"
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
    database_date: list[DatabaseDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        },
    )
    publisher_item: PublisherItem | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    description: Description | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    format: Format | None = field(
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
    dataset_type: DatasetDatasetType = field(
        default=DatasetDatasetType.RECORD,
        metadata={
            "type": "Attribute",
        },
    )
