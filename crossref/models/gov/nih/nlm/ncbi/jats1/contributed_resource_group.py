from dataclasses import dataclass, field
from typing import List, Optional, Union

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
    <div> <h3>Contributed Resource Group</h3> </div>
    """

    class Meta:
        name = "contributed-resource-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    award_group: List[AwardGroup] = field(
        default_factory=list,
        metadata={
            "name": "award-group",
            "type": "Element",
        },
    )
    support_description: List[SupportDescription] = field(
        default_factory=list,
        metadata={
            "name": "support-description",
            "type": "Element",
        },
    )
    resource_group: List[ResourceGroup] = field(
        default_factory=list,
        metadata={
            "name": "resource-group",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    resource_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "resource-type",
            "type": "Attribute",
        },
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
