from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.simple_file_type import SimpleFileType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class FileType:
    """
    Enumerated file types known by IP-XACT.
    """

    class Meta:
        name = "fileType"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: SimpleFileType = field(
        metadata={
            "required": True,
        }
    )
    user: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    libext: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
