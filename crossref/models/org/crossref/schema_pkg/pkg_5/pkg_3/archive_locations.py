from dataclasses import dataclass, field
from typing import List
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.archive import Archive

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ArchiveLocations:
    """
    Container element for archive information.
    """
    class Meta:
        name = "archive_locations"
        namespace = "http://www.crossref.org/schema/5.3.1"

    archive: List[Archive] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
