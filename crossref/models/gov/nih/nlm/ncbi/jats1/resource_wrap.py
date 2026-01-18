from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.resource_id import ResourceId
from crossref.models.gov.nih.nlm.ncbi.jats1.resource_name import ResourceName

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class ResourceWrap:
    """
    <div> <h3>Resource Wrap</h3> </div>.
    """

    class Meta:
        name = "resource-wrap"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    resource_name: ResourceName | None = field(
        default=None,
        metadata={
            "name": "resource-name",
            "type": "Element",
            "required": True,
        },
    )
    resource_id: list[ResourceId] = field(
        default_factory=list,
        metadata={
            "name": "resource-id",
            "type": "Element",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
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
