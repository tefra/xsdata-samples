from dataclasses import dataclass, field

from ipxact.models.file_set import FileSet

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class FileSets:
    """
    List of file sets associated with component.
    """

    class Meta:
        name = "fileSets"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    file_set: list[FileSet] = field(
        default_factory=list,
        metadata={
            "name": "fileSet",
            "type": "Element",
            "min_occurs": 1,
        },
    )
