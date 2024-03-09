from dataclasses import dataclass, field
from typing import List, Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.degrees_language import (
    DegreesLanguage,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Degrees:
    class Meta:
        name = "degrees"
        namespace = "http://www.crossref.org/schema/5.3.1"

    content_type: Optional[object] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    specific_use: Optional[object] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    language: Optional[DegreesLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
