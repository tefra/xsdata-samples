from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .multilanguage_long_name import MultilanguageLongName
from .numerical_or_text import NumericalOrText
from .numerical_value import NumericalValue
from .numerical_value_variation_point import NumericalValueVariationPoint
from .verbatim_string import VerbatimString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ValueGroup:
    """
    This element enables valules to be grouped.

    It can be used to perform row and column-orientated groupings, so that
    these can be rendered properly e.g. as a table.

    :ivar label: This label allows to give the valueGroup a partiluclar
        name. It can be usel if the Values are rendered as a table.
    :ivar vtf: Thias aggregation represents the ability to provide a
        value that is either numerical or text which existence is
        subject to variability. From the formal point of view, the
        aggregation needs to have the multiplicity 1 because SwValues is
        modelled with stereotype &lt;&lt;atpMixed&gt;&gt;. Nevertheless,
        the existence of vtf is optional and subject to constraints. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar vf: This allows to specify the value as VariationPoint. It is
        distinguished to non variant for sake of compatibility to ASAM
        CDF 2.0.
    :ivar vt: This represents the values of textual data elements
        (Strings). Note that vt uses the | to separate the values for
        the different bitfield masks in case that the semantics of the
        related DataPrototype is described by means of a
        BITFIELD_TEXTTABLE in the associated CompuMethod.
    :ivar v: This is a non variant Value. It is provided for sake of
        Compatibility to ASAM CDF.
    :ivar vg: This allows to have intersections in the values in order
        to support specific rendering (eg. using stylesheets). For tools
        it is important that the v values are always processed in the
        same (flattened) order and the tool is able to interpret it
        without respecting vg.
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
        name = "VALUE-GROUP"

    label: MultilanguageLongName | None = field(
        default=None,
        metadata={
            "name": "LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vtf: list[NumericalOrText] = field(
        default_factory=list,
        metadata={
            "name": "VTF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vf: list[NumericalValueVariationPoint] = field(
        default_factory=list,
        metadata={
            "name": "VF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vt: list[VerbatimString] = field(
        default_factory=list,
        metadata={
            "name": "VT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    v: list[NumericalValue] = field(
        default_factory=list,
        metadata={
            "name": "V",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vg: list[ValueGroup] = field(
        default_factory=list,
        metadata={
            "name": "VG",
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
