from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.resource_name import ResourceName
from crossref.models.gov.nih.nlm.ncbi.jats1.resource_wrap import ResourceWrap
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class ResourceGroup:
    """
    <div> <h3>Resource Group</h3> </div>.
    """

    class Meta:
        name = "resource-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    resource_name: list[ResourceName] = field(
        default_factory=list,
        metadata={
            "name": "resource-name",
            "type": "Element",
        },
    )
    resource_wrap: list[ResourceWrap] = field(
        default_factory=list,
        metadata={
            "name": "resource-wrap",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
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
