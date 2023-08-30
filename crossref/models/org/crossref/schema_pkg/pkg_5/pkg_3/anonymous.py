from dataclasses import dataclass, field
from typing import Optional
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.affiliations import Affiliations
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.anonymous_contributor_role import AnonymousContributorRole
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.anonymous_language import AnonymousLanguage
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.anonymous_name_style import AnonymousNameStyle
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.anonymous_sequence import AnonymousSequence

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Anonymous:
    class Meta:
        name = "anonymous"
        namespace = "http://www.crossref.org/schema/5.3.1"

    affiliations: Optional[Affiliations] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sequence: Optional[AnonymousSequence] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    contributor_role: Optional[AnonymousContributorRole] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name_style: Optional[AnonymousNameStyle] = field(
        default=None,
        metadata={
            "name": "name-style",
            "type": "Attribute",
        }
    )
    language: Optional[AnonymousLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
