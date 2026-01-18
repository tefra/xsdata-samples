from __future__ import annotations

from dataclasses import dataclass, field

from .ref import Ref
from .single_language_unit_names import SingleLanguageUnitNames
from .sw_values import SwValues
from .unit_subtypes_enum import UnitSubtypesEnum
from .value_list import ValueList

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwValueCont:
    """
    This metaclass represents the content of one particular SwInstance.

    :ivar unit_ref: This represents the physical unit of the provided
        values.
    :ivar unit_display_name: This specifies how the physical units of
        the current value set shall be displayed in documents or in user
        interfaces of tools.
    :ivar sw_arraysize: This attribute defines the size of each
        dimension for compound primitives CURVE, MAP, CUBOID, CUBE_4,
        CUBE_5, COM_AXIS, RES_AXIS, VAL_BLK. For each dimension one
        value has to be defined, e.g. one in case of COM_AXIS and two or
        more in case of MAP.
    :ivar sw_values_phys: swValuesPhys represents the values in the
        physical domain.
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
        name = "SW-VALUE-CONT"

    unit_ref: None | SwValueCont.UnitRef = field(
        default=None,
        metadata={
            "name": "UNIT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    unit_display_name: None | SingleLanguageUnitNames = field(
        default=None,
        metadata={
            "name": "UNIT-DISPLAY-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_arraysize: None | ValueList = field(
        default=None,
        metadata={
            "name": "SW-ARRAYSIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_values_phys: None | SwValues = field(
        default=None,
        metadata={
            "name": "SW-VALUES-PHYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
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

    @dataclass
    class UnitRef(Ref):
        dest: None | UnitSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
