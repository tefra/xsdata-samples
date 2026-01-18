from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.abbrev_title import (
    AbbrevTitle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import (
    ArchiveLocations,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.coden import Coden
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.full_title import (
    FullTitle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.issn import Issn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.journal_metadata_language import (
    JournalMetadataLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.journal_metadata_reference_distribution_opts import (
    JournalMetadataReferenceDistributionOpts,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class JournalMetadata:
    """
    Container for metadata that defines a journal.
    """

    class Meta:
        name = "journal_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    full_title: list[FullTitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
    abbrev_title: list[AbbrevTitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        },
    )
    issn: list[Issn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        },
    )
    coden: Coden | None = field(
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
    language: JournalMetadataLanguage | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reference_distribution_opts: JournalMetadataReferenceDistributionOpts = (
        field(
            default=JournalMetadataReferenceDistributionOpts.NONE,
            metadata={
                "type": "Attribute",
            },
        )
    )
