from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Pages:
    """
    The container for information about page ranges.
    """
    class Meta:
        name = "pages"
        namespace = "http://www.crossref.org/schema/5.3.1"

    first_page: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 32,
        }
    )
    last_page: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 32,
        }
    )
    other_pages: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 100,
        }
    )
