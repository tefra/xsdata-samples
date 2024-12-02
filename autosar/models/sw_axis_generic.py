from dataclasses import dataclass, field
from typing import Optional

from .integer_value_variation_point import IntegerValueVariationPoint
from .ref import Ref
from .sw_axis_type_subtypes_enum import SwAxisTypeSubtypesEnum
from .sw_generic_axis_param import SwGenericAxisParam

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwAxisGeneric:
    """This meta-class defines a generic axis.

    In a generic axis the axispoints points are calculated in the ECU.
    The ECU is equipped with a fixed calculation algorithm. Parameters
    for the algorithm can be stored in the data component of the ECU.
    Therefore these parameters are specified in the data declaration,
    not in the calibration data.

    :ivar sw_axis_type_ref: Associated axis calculation strategy.
    :ivar sw_number_of_axis_points: The number of base points to be
        calculated for this axis. This element exists to enable the
        number of axis points to be stored explicitly, although it could
        also be described as swGenericAxisParam. This attribute has been
        deprecated, note that the value of
        SwAxisIndividual.swMaxAxisPoints shall be taken instead. In case
        of a generated axis, the number of axis points to be  generated
        shall be taken from SwAxisIndividual.swMaxAxisPoints.
    :ivar sw_generic_axis_params: Specific parameter of a generic axis.
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
        name = "SW-AXIS-GENERIC"

    sw_axis_type_ref: Optional["SwAxisGeneric.SwAxisTypeRef"] = field(
        default=None,
        metadata={
            "name": "SW-AXIS-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_number_of_axis_points: Optional[IntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "SW-NUMBER-OF-AXIS-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_generic_axis_params: Optional["SwAxisGeneric.SwGenericAxisParams"] = (
        field(
            default=None,
            metadata={
                "name": "SW-GENERIC-AXIS-PARAMS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    class SwAxisTypeRef(Ref):
        dest: Optional[SwAxisTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SwGenericAxisParams:
        sw_generic_axis_param: list[SwGenericAxisParam] = field(
            default_factory=list,
            metadata={
                "name": "SW-GENERIC-AXIS-PARAM",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
