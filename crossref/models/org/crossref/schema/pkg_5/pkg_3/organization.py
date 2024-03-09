from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.organization_contributor_role import (
    OrganizationContributorRole,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.organization_language import (
    OrganizationLanguage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.organization_name_style import (
    OrganizationNameStyle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.organization_sequence import (
    OrganizationSequence,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Organization:
    """The name of an organization (as opposed to a person) that contributed to an
    item.

    If an item was authored by individuals in addition to one or more
    organizations, person_name and organization may be freely intermixed
    within contributors.
    """

    class Meta:
        name = "organization"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 511,
            "white_space": "collapse",
        },
    )
    sequence: Optional[OrganizationSequence] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    contributor_role: Optional[OrganizationContributorRole] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name_style: Optional[OrganizationNameStyle] = field(
        default=None,
        metadata={
            "name": "name-style",
            "type": "Attribute",
        },
    )
    language: Optional[OrganizationLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
