from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import (
    ArchiveLocations,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_item import (
    PublisherItem,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.volume import Volume

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class JournalVolume:
    """Container for the journal volume and DOI assigned to an entire journal
    volume.

    You may register a DOI for an entire volume by including doi_data in
    journal_volume.
    """

    class Meta:
        name = "journal_volume"
        namespace = "http://www.crossref.org/schema/5.3.1"

    volume: Optional[Volume] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
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
