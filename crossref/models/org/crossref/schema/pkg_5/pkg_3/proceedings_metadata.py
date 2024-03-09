from dataclasses import dataclass, field
from typing import List, Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import (
    ArchiveLocations,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.noisbn import Noisbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.proceedings_metadata_language import (
    ProceedingsMetadataLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.proceedings_metadata_reference_distribution_opts import (
    ProceedingsMetadataReferenceDistributionOpts,
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

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ProceedingsMetadata:
    """
    Container for all information that applies to a non-series conference
    proceeding.
    """

    class Meta:
        name = "proceedings_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    proceedings_title: Optional[ProceedingsTitle] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    proceedings_subject: Optional[ProceedingsSubject] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publisher: List[Publisher] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
    publication_date: List[PublicationDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
    isbn: List[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        },
    )
    noisbn: Optional[Noisbn] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publisher_item: Optional[PublisherItem] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    archive_locations: Optional[ArchiveLocations] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    doi_data: Optional[DoiData] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    language: Optional[ProceedingsMetadataLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reference_distribution_opts: ProceedingsMetadataReferenceDistributionOpts = field(
        default=ProceedingsMetadataReferenceDistributionOpts.NONE,
        metadata={
            "type": "Attribute",
        },
    )
