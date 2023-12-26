from dataclasses import dataclass, field
from typing import Optional
from .nmtoken_string import NmtokenString
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EnumerationMappingEntry:
    """This class specifies the entry elements of the enumeration mapping table.

    Note that this class might be used in the extended meta-model only.

    :ivar numerical_value: This attribute specifies the numerical value
        (e.g. 0, 1) of the enumeration entry. The numericalValue marks
        an index on M2 level. It is not used in C-Code or at runtime.
        The numericalValue is only given to be able to calculate a value
        that represents the enumerator literal in a numerical
        expression.
    :ivar enumerator_value: This attribute specifies the symbolic value
        (e.g. in, out) of the enumeration entry.
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
        name = "ENUMERATION-MAPPING-ENTRY"

    numerical_value: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "NUMERICAL-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    enumerator_value: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "ENUMERATOR-VALUE",
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
