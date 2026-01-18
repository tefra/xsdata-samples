from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.relations.program import Program
from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import (
    ArchiveLocations,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import (
    Contributors,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.database_date import (
    DatabaseDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.database_metadata_language import (
    DatabaseMetadataLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.database_metadata_reference_distribution_opts import (
    DatabaseMetadataReferenceDistributionOpts,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.description import (
    Description,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution import (
    Institution,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher import Publisher
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_item import (
    PublisherItem,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class DatabaseMetadata:
    """
    database_metadata contains metadata about the database.
    """

    class Meta:
        name = "database_metadata"
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
    description: None | Description = field(
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
    publisher: None | Publisher = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    institution: list[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        },
    )
    publisher_item: None | PublisherItem = field(
        default=None,
        metadata={
            "type": "Element",
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
    program: None | Program = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/relations.xsd",
        },
    )
    language: None | DatabaseMetadataLanguage = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reference_distribution_opts: DatabaseMetadataReferenceDistributionOpts = (
        field(
            default=DatabaseMetadataReferenceDistributionOpts.NONE,
            metadata={
                "type": "Attribute",
            },
        )
    )
