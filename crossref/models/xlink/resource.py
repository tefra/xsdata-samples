from dataclasses import dataclass

from crossref.models.xlink.resource_type import ResourceType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class Resource(ResourceType):
    class Meta:
        name = "resource"
        namespace = "http://www.w3.org/1999/xlink"
