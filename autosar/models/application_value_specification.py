from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .identifier import Identifier
from .sw_axis_cont import SwAxisCont
from .sw_value_cont import SwValueCont

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ApplicationValueSpecification:
    """This meta-class represents values for DataPrototypes typed by
    ApplicationDataTypes (this includes in particular compound primitives).

    For further details refer to ASAM CDF 2.0. This meta-class
    corresponds to some extent with SW-INSTANCE in ASAM CDF 2.0.

    :ivar short_label: This can be used to identify particular value
        specifications for human readers, for example elements of a
        record type.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar category: Specifies to which category of ApplicationDataType
        this ApplicationValueSpecification can be applied (e.g. as an
        initial value), thus imposing constraints on the structure and
        semantics of the contained values, see [constr_1006] and
        [constr_2051].
    :ivar sw_axis_conts: This represents the axis values of a Compound
        Primitive Data Type (curve or map). The first swAxisCont
        describes the x-axis, the second swAxisCont describes the
        y-axis, the third swAxisCont describes the z-axis. In addition
        to this, the axis can be denoted in swAxisIndex.
    :ivar sw_value_cont: This represents the values of a Compound
        Primitive Data Type.
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
        name = "APPLICATION-VALUE-SPECIFICATION"

    short_label: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_axis_conts: Optional["ApplicationValueSpecification.SwAxisConts"] = (
        field(
            default=None,
            metadata={
                "name": "SW-AXIS-CONTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    sw_value_cont: Optional[SwValueCont] = field(
        default=None,
        metadata={
            "name": "SW-VALUE-CONT",
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
    class SwAxisConts:
        sw_axis_cont: list[SwAxisCont] = field(
            default_factory=list,
            metadata={
                "name": "SW-AXIS-CONT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
