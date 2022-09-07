from dataclasses import dataclass, field
from typing import Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.affiliations import Affiliations
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributor_atts_contributor_role import ContributorAttsContributorRole
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributor_atts_name_style import ContributorAttsNameStyle
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributor_atts_sequence import ContributorAttsSequence
from crossref.models.org.crossref.schema.pkg_5.pkg_3.language_atts_language import LanguageAttsLanguage

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
    sequence: Optional[ContributorAttsSequence] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    contributor_role: Optional[ContributorAttsContributorRole] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name_style: Optional[ContributorAttsNameStyle] = field(
        default=None,
        metadata={
            "name": "name-style",
            "type": "Attribute",
        }
    )
    language: Optional[LanguageAttsLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
