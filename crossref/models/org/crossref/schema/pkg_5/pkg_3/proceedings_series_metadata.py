from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import (
    ArchiveLocations,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.noisbn import Noisbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.proceedings_series_metadata_reference_distribution_opts import (
    ProceedingsSeriesMetadataReferenceDistributionOpts,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.proceedings_subject import (
    ProceedingsSubject,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.proceedings_title import (
    ProceedingsTitle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publication_date import (
    PublicationDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher import Publisher
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_item import (
    PublisherItem,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.series_metadata import (
    SeriesMetadata,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.volume import Volume

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ProceedingsSeriesMetadata:
    """
    Container for all information that applies to a specific conference
    proceeding that is part of a series.
    """

    class Meta:
        name = "proceedings_series_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    series_metadata: SeriesMetadata | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    proceedings_title: ProceedingsTitle | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
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
    proceedings_subject: list[ProceedingsSubject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        },
    )
    publisher: list[Publisher] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        },
    )
    publication_date: list[PublicationDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 20,
        },
    )
    isbn: list[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        },
    )
    noisbn: Noisbn | None = field(
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
    reference_distribution_opts: ProceedingsSeriesMetadataReferenceDistributionOpts = field(
        default=ProceedingsSeriesMetadataReferenceDistributionOpts.NONE,
        metadata={
            "type": "Attribute",
        },
    )
