from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.contributed_resource_group import (
    ContributedResourceGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.funding_group import FundingGroup
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class SupportGroup:
    """
    <div> <h3>Support Group</h3> </div>.
    """

    class Meta:
        name = "support-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    funding_group: list[FundingGroup] = field(
        default_factory=list,
        metadata={
            "name": "funding-group",
            "type": "Element",
        },
    )
    contributed_resource_group: list[ContributedResourceGroup] = field(
        default_factory=list,
        metadata={
            "name": "contributed-resource-group",
            "type": "Element",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: str | None = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: str | LangValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
