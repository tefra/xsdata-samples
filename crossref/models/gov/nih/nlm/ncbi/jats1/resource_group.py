from dataclasses import dataclass, field
from typing import List, Optional, Union
from crossref.models.gov.nih.nlm.ncbi.jats1.resource_name import ResourceName
from crossref.models.gov.nih.nlm.ncbi.jats1.resource_wrap import ResourceWrap
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class ResourceGroup:
    """
    <div> <h3>Resource Group</h3> </div>
    """

    class Meta:
        name = "resource-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    resource_name: List[ResourceName] = field(
        default_factory=list,
        metadata={
            "name": "resource-name",
            "type": "Element",
        },
    )
    resource_wrap: List[ResourceWrap] = field(
        default_factory=list,
        metadata={
            "name": "resource-wrap",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
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
