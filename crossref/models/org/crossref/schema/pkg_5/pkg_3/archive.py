from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_name import (
    ArchiveName,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Archive:
    """
    Used to indicate the designated archiving organization(s) for an item.
    """

    class Meta:
        name = "archive"
        namespace = "http://www.crossref.org/schema/5.3.1"

    name: None | ArchiveName = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
