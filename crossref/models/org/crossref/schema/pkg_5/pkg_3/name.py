from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.given_name import (
    GivenName,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.name_language import (
    NameLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.name_name_style import (
    NameNameStyle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.prefix import Prefix
from crossref.models.org.crossref.schema.pkg_5.pkg_3.suffix import Suffix
from crossref.models.org.crossref.schema.pkg_5.pkg_3.surname import Surname

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Name:
    class Meta:
        name = "name"
        namespace = "http://www.crossref.org/schema/5.3.1"

    surname: Surname | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    given_name: list[GivenName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    prefix: Prefix | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    suffix: Suffix | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    content_type: object | None = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    name_style: NameNameStyle = field(
        default=NameNameStyle.WESTERN,
        metadata={
            "name": "name-style",
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
    language: NameLanguage | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
