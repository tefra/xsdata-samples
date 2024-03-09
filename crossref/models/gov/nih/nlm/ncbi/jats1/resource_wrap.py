from dataclasses import dataclass, field
from typing import List, Optional

from crossref.models.gov.nih.nlm.ncbi.jats1.resource_id import ResourceId
from crossref.models.gov.nih.nlm.ncbi.jats1.resource_name import ResourceName

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class ResourceWrap:
    """
    <div> <h3>Resource Wrap</h3> </div>
    """

    class Meta:
        name = "resource-wrap"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    resource_name: Optional[ResourceName] = field(
        default=None,
        metadata={
            "name": "resource-name",
            "type": "Element",
            "required": True,
        },
    )
    resource_id: List[ResourceId] = field(
        default_factory=list,
        metadata={
            "name": "resource-id",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
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
