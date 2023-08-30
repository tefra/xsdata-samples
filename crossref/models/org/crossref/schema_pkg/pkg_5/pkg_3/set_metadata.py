from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.archive_locations import ArchiveLocations
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.contributors import Contributors
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.noisbn import Noisbn
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.publisher_item import PublisherItem
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class SetMetadata:
    """
    When a book consists of multiple volumes that are not part of a serial
    publication (series), set_metadata is used to describe information about the
    entire set.
    """
    class Meta:
        name = "set_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    titles: Optional[Titles] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    isbn: List[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        }
    )
    noisbn: Optional[Noisbn] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    contributors: Optional[Contributors] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    part_number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 15,
        }
    )
    publisher_item: Optional[PublisherItem] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    archive_locations: Optional[ArchiveLocations] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    doi_data: Optional[DoiData] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
