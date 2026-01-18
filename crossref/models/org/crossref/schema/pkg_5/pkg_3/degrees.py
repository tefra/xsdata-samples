from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.degrees_language import (
    DegreesLanguage,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Degrees:
    class Meta:
        name = "degrees"
        namespace = "http://www.crossref.org/schema/5.3.1"

    content_type: object | None = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    specific_use: object | None = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    language: DegreesLanguage | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
