from dataclasses import dataclass, field
from typing import Optional
from autosar.models.axis_index_type import AxisIndexType
from autosar.models.calprm_axis_category_enum import CalprmAxisCategoryEnum
from autosar.models.ref import Ref
from autosar.models.single_language_unit_names import SingleLanguageUnitNames
from autosar.models.sw_values import SwValues
from autosar.models.unit_subtypes_enum import UnitSubtypesEnum
from autosar.models.value_list import ValueList

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwAxisCont:
    """This represents the values for the axis of a compound primitive (curve,
    map).

    For standard and fix axes,  SwAxisCont contains the values of the
    axis directly. The axis values of SwAxisCont with the category
    COM_AXIS, RES_AXIS are for display only. For editing and processing,
    only the values in the related GroupAxis are binding.

    :ivar category: This category specifies the particular axis types: *
        STD_AXIS * COM_AXIS * RES_AXIS  (swArraysize necessary)
    :ivar unit_ref: This represents the physical unit of the provided
        values.
    :ivar unit_display_name: This represents the display name which is
        used for the physical unit of the axis.
    :ivar sw_axis_index: This property allows to explicitly assign the
        axis contents to a particular axis. It is specified by numbers
        where 1 corresponds to the x-axis. It is also possible to derive
        the axis association from the sequence of the parent.
    :ivar sw_arraysize: For multidimensional compound primitivies
        (curve, map ...) it is necessary to know the dimensions.They are
        specified using swArraySize. * RES_AXIS
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
        name = "SW-AXIS-CONT"

    category: Optional[CalprmAxisCategoryEnum] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    unit_ref: Optional["SwAxisCont.UnitRef"] = field(
        default=None,
        metadata={
            "name": "UNIT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    unit_display_name: Optional[SingleLanguageUnitNames] = field(
        default=None,
        metadata={
            "name": "UNIT-DISPLAY-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_axis_index: Optional[AxisIndexType] = field(
        default=None,
        metadata={
            "name": "SW-AXIS-INDEX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_arraysize: Optional[ValueList] = field(
        default=None,
        metadata={
            "name": "SW-ARRAYSIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_values_phys: Optional[SwValues] = field(
        default=None,
        metadata={
            "name": "SW-VALUES-PHYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
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

    @dataclass
    class UnitRef(Ref):
        dest: Optional[UnitSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
