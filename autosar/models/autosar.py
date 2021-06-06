from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    DocumentationBlock,
)
from .ar_package import ArPackage
from .file_info_comment import FileInfoComment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Autosar:
    """
    Root element of an AUTOSAR description, also the root element in
    corresponding XML documents.

    :ivar file_info_comment: This represents a possibility to provide a
        structured comment in an AUTOSAR file.
    :ivar admin_data: This represents the administrative data of an
        Autosar file.
    :ivar introduction: This represents an introduction on the Autosar
        file. It is intended for example to rpresent disclaimers and
        legal notes.
    :ivar ar_packages: This is the top level package in an AUTOSAR
        model. The upper multiplicity of this role has been increased to
        * due to resolving an atpVariation stereotype. The previous
        value was -1.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """
    class Meta:
        name = "AUTOSAR"
        namespace = "http://autosar.org/schema/r4.0"

    file_info_comment: Optional[FileInfoComment] = field(
        default=None,
        metadata={
            "name": "FILE-INFO-COMMENT",
            "type": "Element",
        }
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
        }
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
        }
    )
    ar_packages: Optional["Autosar.ArPackages"] = field(
        default=None,
        metadata={
            "name": "AR-PACKAGES",
            "type": "Element",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class ArPackages:
        ar_package: List[ArPackage] = field(
            default_factory=list,
            metadata={
                "name": "AR-PACKAGE",
                "type": "Element",
            }
        )
