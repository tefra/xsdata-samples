from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class McdIdentifier:
    """This primitive denotes a name used for measurement and calibration
    systems and shall follow the restrictions for an ASAM ASAP2 ident.

    For detailed syntax see the xsd.pattern. The size limitations are
    not captured. McdIdentifiers are random names which may contain
    characters A through Z, a through z, underscore (_), numerals 0
    through 9, points ('.') and brackets ( '[',']' ). However, the
    following limitations apply: the first character shall be a letter
    or an underscore, brackets shall occur in pairs at the end of a
    partial string and shall contain a number or an alpha-numerical
    string (description of the index of an array element).

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
        name = "MCD-IDENTIFIER"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"[a-zA-Z_][a-zA-Z0-9_]*(\[([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\])*(\.[a-zA-Z_][a-zA-Z0-9_]*(\[([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\])*)*",
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
