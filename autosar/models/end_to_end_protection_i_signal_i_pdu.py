from dataclasses import dataclass, field
from typing import Optional
from .annotation import VariationPoint
from .i_signal_group_subtypes_enum import ISignalGroupSubtypesEnum
from .i_signal_i_pdu_subtypes_enum import ISignalIPduSubtypesEnum
from .integer import Integer
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EndToEndProtectionISignalIPdu:
    """It is possible to protect the inter-ECU data exchange of safety-related
    ISignalGroups at the level of COM IPdus using protection mechanisms provided by
    E2E Library.

    For each ISignalGroup to be protected, a separate
    EndToEndProtectionISignalIPdu element shall be created within the
    EndToEndProtectionSet. The EndToEndProtectionISignalIPdu element
    refers to the ISignalGroup that is to be protected and to the
    ISignalIPdu that transmits the protected ISignalGroup. The
    information how the referenced ISignalGroup shall be protected
    (through which E2E Profile and with which E2E settings) is defined
    in the EndToEndDescription element.

    :ivar data_offset: This attribute defines the beginning offset (in
        bits) of the Array representation of the Signal Group (including
        CRC, counter and application signal group) in the IPdu. This
        attribute is mandatory and the dataOffset shall always be
        defined.
    :ivar i_signal_group_ref: Reference to the ISignalGroup that is to
        be protected.
    :ivar i_signal_i_pdu_ref: Reference to the ISignalIPdu that
        transmits the protected ISignalGroup.
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
        name = "END-TO-END-PROTECTION-I-SIGNAL-I-PDU"

    data_offset: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "DATA-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    i_signal_group_ref: Optional[
        "EndToEndProtectionISignalIPdu.ISignalGroupRef"
    ] = field(
        default=None,
        metadata={
            "name": "I-SIGNAL-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    i_signal_i_pdu_ref: Optional[
        "EndToEndProtectionISignalIPdu.ISignalIPduRef"
    ] = field(
        default=None,
        metadata={
            "name": "I-SIGNAL-I-PDU-REF",
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
    class ISignalGroupRef(Ref):
        dest: Optional[ISignalGroupSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ISignalIPduRef(Ref):
        dest: Optional[ISignalIPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
