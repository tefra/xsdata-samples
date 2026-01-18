from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ComponentNumber:
    """
    The chapter, section, part, etc. number for a content item in a book.

    Unlike volume and edition_number, component_number should include any
    additional text that helps identify the type of component.
    """

    class Meta:
        name = "component_number"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 50,
        },
    )
