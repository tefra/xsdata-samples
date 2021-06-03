from dataclasses import dataclass, field
from typing import Optional
from autosar.models.data_filter import DataFilter
from autosar.models.i_signal_to_i_pdu_mapping_subtypes_enum import ISignalToIPduMappingSubtypesEnum
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TransmissionModeCondition:
    """Possibility to attach a condition to each signal within an I-PDU.

    If at least one condition evaluates to true, TRANSMISSION MODE True
    shall be used for this I-Pdu. In all other cases, the TRANSMISSION
    MODE FALSE shall be used.

    :ivar data_filter: Possibilities to define conditions
    :ivar i_signal_in_i_pdu_ref: Reference to a signal to which a
        condition is attached.
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
        name = "TRANSMISSION-MODE-CONDITION"

    data_filter: Optional[DataFilter] = field(
        default=None,
        metadata={
            "name": "DATA-FILTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    i_signal_in_i_pdu_ref: Optional["TransmissionModeCondition.ISignalInIPduRef"] = field(
        default=None,
        metadata={
            "name": "I-SIGNAL-IN-I-PDU-REF",
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
    class ISignalInIPduRef(Ref):
        dest: Optional[ISignalToIPduMappingSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
