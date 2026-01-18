from __future__ import annotations

from dataclasses import dataclass, field

from .axis_index_type import AxisIndexType
from .calprm_axis_category_enum import CalprmAxisCategoryEnum
from .display_format_string import DisplayFormatString
from .ref import Ref
from .sw_axis_grouped import SwAxisGrouped
from .sw_axis_individual import SwAxisIndividual
from .sw_base_type_subtypes_enum import SwBaseTypeSubtypesEnum
from .sw_calibration_access_enum import SwCalibrationAccessEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwCalprmAxis:
    """
    This element specifies an individual input parameter axis (abscissa).

    :ivar sw_axis_index: This attribute specifies which axis is
        specified by the containing SwCalprmAxis. For example in a curve
        this is usually "1". In a map this is "1" or "2".
    :ivar category: This property specifies the category of a particular
        axis.
    :ivar sw_axis_grouped:
    :ivar sw_axis_individual:
    :ivar sw_calibration_access: Describes the applicability of
        parameters and variables.
    :ivar display_format: This property specifies how the axis values
        shall be displayed e.g. in documents or in measurement and
        calibration tools.
    :ivar base_type_ref: The SwBaseType to be used for the axis. Note
        that this is not applicable for ApplicationDataTypes. The value
        shall be ignored.
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
        name = "SW-CALPRM-AXIS"

    sw_axis_index: AxisIndexType | None = field(
        default=None,
        metadata={
            "name": "SW-AXIS-INDEX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: CalprmAxisCategoryEnum | None = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_axis_grouped: SwAxisGrouped | None = field(
        default=None,
        metadata={
            "name": "SW-AXIS-GROUPED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_axis_individual: SwAxisIndividual | None = field(
        default=None,
        metadata={
            "name": "SW-AXIS-INDIVIDUAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_calibration_access: SwCalibrationAccessEnum | None = field(
        default=None,
        metadata={
            "name": "SW-CALIBRATION-ACCESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    display_format: DisplayFormatString | None = field(
        default=None,
        metadata={
            "name": "DISPLAY-FORMAT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    base_type_ref: SwCalprmAxis.BaseTypeRef | None = field(
        default=None,
        metadata={
            "name": "BASE-TYPE-REF",
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

    @dataclass
    class BaseTypeRef(Ref):
        dest: SwBaseTypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
