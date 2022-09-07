from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class OtherPages:
    """When an item has non-contiguous page information, capture the first page
    range in first_page and last_page.

    Any additional page information should be captured in other_pages.
    """
    class Meta:
        name = "other_pages"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 100,
        }
    )
