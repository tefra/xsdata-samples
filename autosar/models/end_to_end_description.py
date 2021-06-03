from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.nmtoken_string import NmtokenString
from autosar.models.positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EndToEndDescription:
    """This meta-class contains information about end-to-end protection.

    The set of applicable attributes depends on the actual value of the
    category attribute of EndToEndProtection.

    :ivar category: The category represents the identification of the
        concrete E2E profile. The applicable values are specified in a
        semantic constraint and determine the applicable attributes of
        EndToEndDescription.
    :ivar data_ids:
    :ivar data_id_mode: There are three inclusion modes how the implicit
        two-byte Data ID is included in the one-byte CRC:  * dataIDMode
        = 0: Two bytes are included in the CRC (double ID configuration)
        This is used in variant 1A. * dataIDMode = 1: One of the two
        bytes byte is included, alternating high and low byte, depending
        on parity of the counter (alternating ID configuration). For
        even counter low byte is included; For odd counters the high
        byte is included. This is used in variant 1B. * dataIDMode = 2:
        Only low byte is included, high byte is never used. This is
        applicable if the IDs in a particular system are 8 bits. *
        dataIdMode = 3: The low byte is included in the implicit CRC
        calculation, the low nibble of the high byte is transmitted
        along with the data (i.e. it is explicitly included), the high
        nibble of the high byte is not used. This is applicable for the
        IDs up to 12 bits.
    :ivar data_length: This attribute represents the length of the Array
        representation of the Signal Group/VariableDataPrototype
        including CRC and Counter in bits.
    :ivar max_delta_counter_init: Initial maximum allowed gap between
        two counter values of two consecutively received valid Data,
        i.e. how many subsequent lost data is accepted. For example, if
        the receiver gets Data with counter 1 and MaxDeltaCounterInit is
        1, then at the next reception the receiver can accept Counters
        with values 2 and 3, but not 4.  Note that if the receiver does
        not receive new Data at a consecutive read, then the receiver
        increments the tolerance by 1.
    :ivar crc_offset: Bit offset of CRC from the beginning of the Array
        representation of the Signal Group/VariableDataPrototype (MSB
        order, bit numbering: bit 0 is the least important). The offset
        shall be a multiplicity of 8 and it should be 0 whenever
        possible. For example, offset 8 means that the CRC will take the
        byte 1, i.e. bits 8..15. If crcOffset is not present the value
        is defined by the selected profile.
    :ivar counter_offset: Bit offset of Counter from the beginning of
        the Array representation of the Signal
        Group/VariableDataPrototype (MSB order, bit numbering: bit 0 is
        the least important). The offset shall be a multiplicity of 4
        and it should be 8 whenever possible. For example, offset 8
        means that the counter will take the low nibble of the byte 1,
        i.e. bits 8 .. 11. If counterOffset is not present the value is
        defined by the selected profile.
    :ivar max_no_new_or_repeated_data: The maximum amount of missing or
        repeated Data which the receiver does not expect to exceed under
        normal communication conditions.
    :ivar sync_counter_init: Number of Data required for validating the
        consistency of the counter that shall be received with a valid
        counter  (i.e. counter within the allowed lock-in range) after
        the detection of an unexpected behavior of a received counter.
    :ivar data_id_nibble_offset: Bit offset of the low nibble of the
        high byte of Data ID. The applicability of this attribute is
        controlled by [constr_1261].
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
        name = "END-TO-END-DESCRIPTION"

    category: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    data_ids: Optional["EndToEndDescription.DataIds"] = field(
        default=None,
        metadata={
            "name": "DATA-IDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    data_id_mode: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "DATA-ID-MODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    data_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "DATA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_delta_counter_init: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-DELTA-COUNTER-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    crc_offset: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "CRC-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    counter_offset: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "COUNTER-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_no_new_or_repeated_data: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-NO-NEW-OR-REPEATED-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sync_counter_init: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SYNC-COUNTER-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    data_id_nibble_offset: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "DATA-ID-NIBBLE-OFFSET",
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
    class DataIds:
        """
        :ivar data_id: This represents a unique numerical identifier.
            Note: ID is used for protection against masquerading. The
            details concerning the maximum number of values (this
            information is specific for each E2E profile) applicable for
            this attribute are controlled by a semantic constraint that
            depends on the category of the EndToEndProtection.
        """
        data_id: List[PositiveInteger] = field(
            default_factory=list,
            metadata={
                "name": "DATA-ID",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
