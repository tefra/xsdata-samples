from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .autosar_variable_ref import AutosarVariableRef
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class NvBlockDataMapping:
    """
    Defines the mapping between the VariableDataPrototypes in the
    NvBlockComponents ports and the VariableDataPrototypes of the RAM
    Block.

    The data types of the referenced VariableDataPrototypes in the ports
    and the referenced sub-element (inside a CompositeDataType) of the
    VariableDataPrototype representing the RAM Block shall be compatible.

    :ivar bitfield_text_table_mask_nv_block_descriptor: This attribute
        identifies the applicable bit mask on the side of the Nv Block.
    :ivar bitfield_text_table_mask_port_prototype: This attribute
        identifies the applicable bit mask on the side of the
        PortPrototype.
    :ivar nv_ram_block_element: Reference to a VariableDataPrototype of
        a RAM Block.
    :ivar read_nv_data: Reference to a VariableDataPrototype of a pPort
        of the NvBlockComponent providing read access to the RAM
        Block.If there is no PortPrototype providing read access (write-
        only) the reference can be omitted.
    :ivar written_nv_data: Reference to a VariableDataPrototype of a
        rPort of the NvBlockComponent providing write access to the RAM
        Block. If there is no port providing write access (read-only)
        the reference can be omitted.
    :ivar written_read_nv_data: Reference to a VariableDataPrototype of
        a PRPortPrototype of the NvBlockSwComponentType providing write
        and read access to the RAM Block.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "NV-BLOCK-DATA-MAPPING"

    bitfield_text_table_mask_nv_block_descriptor: None | PositiveInteger = (
        field(
            default=None,
            metadata={
                "name": "BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    bitfield_text_table_mask_port_prototype: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "BITFIELD-TEXT-TABLE-MASK-PORT-PROTOTYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nv_ram_block_element: None | AutosarVariableRef = field(
        default=None,
        metadata={
            "name": "NV-RAM-BLOCK-ELEMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    read_nv_data: None | AutosarVariableRef = field(
        default=None,
        metadata={
            "name": "READ-NV-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    written_nv_data: None | AutosarVariableRef = field(
        default=None,
        metadata={
            "name": "WRITTEN-NV-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    written_read_nv_data: None | AutosarVariableRef = field(
        default=None,
        metadata={
            "name": "WRITTEN-READ-NV-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
