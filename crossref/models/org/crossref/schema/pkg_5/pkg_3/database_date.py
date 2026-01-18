from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.creation_date import (
    CreationDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publication_date import (
    PublicationDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.update_date import (
    UpdateDate,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class DatabaseDate:
    """
    Container for key dates in the life of a database or dataset.
    """

    class Meta:
        name = "database_date"
        namespace = "http://www.crossref.org/schema/5.3.1"

    creation_date: CreationDate | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publication_date: PublicationDate | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    update_date: UpdateDate | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
