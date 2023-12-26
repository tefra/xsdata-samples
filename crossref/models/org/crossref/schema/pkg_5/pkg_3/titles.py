from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.original_language_title import (
    OriginalLanguageTitle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.subtitle import Subtitle
from crossref.models.org.crossref.schema.pkg_5.pkg_3.title import Title

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Titles:
    """
    A container for the title and original language title elements.
    """

    class Meta:
        name = "titles"
        namespace = "http://www.crossref.org/schema/5.3.1"

    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    subtitle: List[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        },
    )
    original_language_title: Optional[OriginalLanguageTitle] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
