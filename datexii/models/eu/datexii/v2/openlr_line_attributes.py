from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_form_of_way_enum import (
    OpenlrFormOfWayEnum,
)
from datexii.models.eu.datexii.v2.openlr_functional_road_class_enum import (
    OpenlrFunctionalRoadClassEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrLineAttributes:
    """
    Line attributes are part of a location reference point and consists of
    functional road class (FRC),form of way (FOW) and bearing (BEAR) data.

    :ivar openlr_functional_road_class: The functional road class (FRC)
        can hold eight different values as described in the logical
        format.
    :ivar openlr_form_of_way: The form of way (FOW) can hold eight
        different values as described in the logical format.
    :ivar openlr_bearing: defines the bearing field as an integer value
        between 0 and 360 whereby “0” is included and “360” is excluded
        from that range.
    :ivar openlr_line_attributes_extension:
    """

    openlr_functional_road_class: OpenlrFunctionalRoadClassEnum | None = field(
        default=None,
        metadata={
            "name": "openlrFunctionalRoadClass",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_form_of_way: OpenlrFormOfWayEnum | None = field(
        default=None,
        metadata={
            "name": "openlrFormOfWay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_bearing: int | None = field(
        default=None,
        metadata={
            "name": "openlrBearing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_line_attributes_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "openlrLineAttributesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
