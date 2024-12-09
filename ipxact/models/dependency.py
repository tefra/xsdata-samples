from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.ipxact_uri import IpxactUri

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Dependency(IpxactUri):
    """Specifies a location on which  files or fileSets may be dependent.

    Typically, this would be a directory that would contain included
    files.
    """

    class Meta:
        name = "dependency"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
