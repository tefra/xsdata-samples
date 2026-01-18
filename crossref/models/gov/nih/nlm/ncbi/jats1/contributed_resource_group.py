from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.award_group import AwardGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.resource_group import ResourceGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.support_description import (
    SupportDescription,
)
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class ContributedResourceGroup:
    """
    <div> <h3>Contributed Resource Group</h3> </div>.
    """

    class Meta:
        name = "contributed-resource-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    award_group: list[AwardGroup] = field(
        default_factory=list,
        metadata={
            "name": "award-group",
            "type": "Element",
        },
    )
    support_description: list[SupportDescription] = field(
        default_factory=list,
        metadata={
            "name": "support-description",
            "type": "Element",
        },
    )
    resource_group: list[ResourceGroup] = field(
        default_factory=list,
        metadata={
            "name": "resource-group",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    resource_type: None | str = field(
        default=None,
        metadata={
            "name": "resource-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
