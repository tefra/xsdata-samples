from dataclasses import dataclass, field

from .numerical_value_variation_point import NumericalValueVariationPoint

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Sdf:
    """
    This class represents a numerical value in a special data group which
    may be subject to variability.

    :ivar value: This is the value of the special data.
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
    :ivar gid: This attributes specifies an identifier. Gid comes from
        the SGML/XML-Term "Generic Identifier" which is the element name
        in XML. The role of this attribute is the same as the name of an
        XML - element.
    """

    class Meta:
        name = "SDF"

    value: NumericalValueVariationPoint | None = field(
        default=None,
        metadata={
            "name": "VALUE",
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
    gid: str | None = field(
        default=None,
        metadata={
            "name": "GID",
            "type": "Attribute",
        },
    )
