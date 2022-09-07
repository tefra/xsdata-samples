from dataclasses import dataclass, field
from typing import Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.affiliations import Affiliations
from crossref.models.org.crossref.schema.pkg_5.pkg_3.alt_name import AltName
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributor_atts_contributor_role import ContributorAttsContributorRole
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributor_atts_name_style import ContributorAttsNameStyle
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributor_atts_sequence import ContributorAttsSequence
from crossref.models.org.crossref.schema.pkg_5.pkg_3.language_atts_language import LanguageAttsLanguage
from crossref.models.org.crossref.schema.pkg_5.pkg_3.orcid import Orcid

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class PersonName:
    """
    The name of a person (as opposed to an organization) that contributed to an
    item.
    """
    class Meta:
        name = "person_name"
        namespace = "http://www.crossref.org/schema/5.3.1"

    given_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
            "pattern": r"[^\d\?]*[^\?\s]+[^\d]*",
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
            "pattern": r"[^\d\?]*[^\?\s]+[^\d]*",
        }
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 10,
        }
    )
    affiliations: Optional[Affiliations] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orcid: Optional[Orcid] = field(
        default=None,
        metadata={
            "name": "ORCID",
            "type": "Element",
        }
    )
    alt_name: Optional[AltName] = field(
        default=None,
        metadata={
            "name": "alt-name",
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
