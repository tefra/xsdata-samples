from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.first_page import (
    FirstPage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.last_page import LastPage
from crossref.models.org.crossref.schema.pkg_5.pkg_3.other_pages import (
    OtherPages,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Pages:
    """
    The container for information about page ranges.
    """

    class Meta:
        name = "pages"
        namespace = "http://www.crossref.org/schema/5.3.1"

    first_page: FirstPage | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    last_page: LastPage | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    other_pages: OtherPages | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
