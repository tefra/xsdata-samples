from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.affiliations import (
    Affiliations,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.anonymous_contributor_role import (
    AnonymousContributorRole,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.anonymous_language import (
    AnonymousLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.anonymous_name_style import (
    AnonymousNameStyle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.anonymous_sequence import (
    AnonymousSequence,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Anonymous:
    class Meta:
        name = "anonymous"
        namespace = "http://www.crossref.org/schema/5.3.1"

    affiliations: None | Affiliations = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sequence: None | AnonymousSequence = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    contributor_role: None | AnonymousContributorRole = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name_style: None | AnonymousNameStyle = field(
        default=None,
        metadata={
            "name": "name-style",
            "type": "Attribute",
        },
    )
    language: None | AnonymousLanguage = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
