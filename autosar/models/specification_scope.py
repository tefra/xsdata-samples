from dataclasses import dataclass, field
from typing import List, Optional

from .specification_document_scope import SpecificationDocumentScope

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SpecificationScope:
    """
    Specification of the relevant subset of Autosar specifications.

    :ivar specification_document_scopes: The Autosar or custom
        specifications that contain that are considered in this Data
        Exchange Point.
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
        name = "SPECIFICATION-SCOPE"

    specification_document_scopes: Optional[
        "SpecificationScope.SpecificationDocumentScopes"
    ] = field(
        default=None,
        metadata={
            "name": "SPECIFICATION-DOCUMENT-SCOPES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class SpecificationDocumentScopes:
        specification_document_scope: List[SpecificationDocumentScope] = field(
            default_factory=list,
            metadata={
                "name": "SPECIFICATION-DOCUMENT-SCOPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
