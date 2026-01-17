from dataclasses import dataclass, field
from typing import Optional

from .identifier import Identifier
from .parameter_data_prototype_subtypes_enum import (
    ParameterDataPrototypeSubtypesEnum,
)
from .ref import Ref
from .variable_data_prototype_subtypes_enum import (
    VariableDataPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class McParameterElementGroup:
    """
    Denotes a group of calibration parameters which are handled by the RTE
    as one data structure.

    :ivar short_label: Assigns a name to this element.
    :ivar ram_location_ref: Refers to the RAM location of this parameter
        group. To be used for the init-RAM method.
    :ivar rom_location_ref: Refers to the ROM location of this parameter
        group. To be used for the init-RAM method.
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
        name = "MC-PARAMETER-ELEMENT-GROUP"

    short_label: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ram_location_ref: Optional["McParameterElementGroup.RamLocationRef"] = (
        field(
            default=None,
            metadata={
                "name": "RAM-LOCATION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    rom_location_ref: Optional["McParameterElementGroup.RomLocationRef"] = (
        field(
            default=None,
            metadata={
                "name": "ROM-LOCATION-REF",
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
    class RamLocationRef(Ref):
        dest: Optional[VariableDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class RomLocationRef(Ref):
        dest: Optional[ParameterDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
