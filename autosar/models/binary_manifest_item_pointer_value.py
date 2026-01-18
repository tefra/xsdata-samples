from dataclasses import dataclass, field

from .address import Address
from .symbol_string import SymbolString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BinaryManifestItemPointerValue:
    """
    This meta-class has the ability to provide a value for a pointer in the
    context of a binary manifest item.

    :ivar address: This attribute represents the address value of the
        enclosing pointer value.
    :ivar symbol: This attribute represents the symbol associated with
        the binary manifest handle.
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
        name = "BINARY-MANIFEST-ITEM-POINTER-VALUE"

    address: Address | None = field(
        default=None,
        metadata={
            "name": "ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    symbol: SymbolString | None = field(
        default=None,
        metadata={
            "name": "SYMBOL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
