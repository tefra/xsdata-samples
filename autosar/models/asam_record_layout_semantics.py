from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class AsamRecordLayoutSemantics:
    """
    This meta-class is used to denote the semantics in particular in terms
    of the corresponding A2L-Keyword.

    This is to support the mapping of the more general record layouts in
    AUTOSAR/MSR to the specific A2L keywords. It is possible to express the
    specific semantics of A2l RecordLayout keywords in SwRecordlayoutGroup
    but not always vice versa. Therefore the mapping is provided in this
    optional attribute. It is specified as NMTOKEN to reduce the direct
    dependency of ASAM an AUTOSAR standards.

    :ivar value:
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
        name = "ASAM-RECORD-LAYOUT-SEMANTICS"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
