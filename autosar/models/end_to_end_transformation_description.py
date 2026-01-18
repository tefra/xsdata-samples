from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .data_id_mode_enum import DataIdModeEnum
from .e_2_e_profile_compatibility_props_subtypes_enum import (
    E2EProfileCompatibilityPropsSubtypesEnum,
)
from .end_to_end_profile_behavior_enum import EndToEndProfileBehaviorEnum
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .nmtoken_string import NmtokenString
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class EndToEndTransformationDescription:
    """
    EndToEndTransformationDescription holds these attributes which are
    profile specific and have the same value for all E2E transformers.

    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particlar
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Describable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar admin_data: This represents the administrative data for the
        describable object.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar clear_from_valid_to_invalid: Clear monitoring window on
        transition from state Valid to state Invalid.
    :ivar counter_offset: Offset of the counter in the Data[] array in
        bits.
    :ivar crc_offset: Offset of the CRC in the Data[] array in bits.
    :ivar data_id_mode: This attribute describes the inclusion mode that
        is used to include the implicit two-byte Data ID in the one-byte
        CRC.
    :ivar data_id_nibble_offset: Offset of the Data ID nibble in the
        Data[] array in bits.
    :ivar e_2_e_profile_compatibility_props_ref: Reference to additional
        settings for the E2E state machine.
    :ivar max_delta_counter: Maximum allowed difference between two
        counter values of two consecutively received valid messages. For
        example, if the receiver gets data with counter 1 and
        MaxDeltaCounter is 3, then at the next reception the receiver
        can accept Counters with values 2, 3 or 4.
    :ivar max_error_state_init: Maximal number of checks in which
        ProfileStatus equal to E2E_P_ERROR was determined, within the
        last WindowSize checks, for the state E2E_SM_INIT.
    :ivar max_error_state_invalid: Maximal number of checks in which
        ProfileStatus equal to E2E_P_ERROR was determined, within the
        last WindowSize checks, for the state E2E_SM_INVALID.
    :ivar max_error_state_valid: Maximal number of checks in which
        ProfileStatus equal to E2E_P_ERROR was determined, within the
        last WindowSize checks, for the state E2E_SM_VALID.
    :ivar max_no_new_or_repeated_data: The maximum allowed amount of
        consecutive failed counter checks.
    :ivar min_ok_state_init: Minimal number of checks in which
        ProfileStatus equal to E2E_P_OK was determined, within the last
        WindowSize checks, for the state E2E_SM_INIT.
    :ivar min_ok_state_invalid: Minimal number of checks in which
        ProfileStatus equal to E2E_P_OK was determined, within the last
        WindowSize checks, for the state E2E_SM_INVALID.
    :ivar min_ok_state_valid: Minimal number of checks in which
        ProfileStatus equal to E2E_P_OK was determined, within the last
        WindowSize checks, for the state E2E_SM_VALID.
    :ivar offset: Offset of the E2E header in the Data[] array in bits.
    :ivar profile_behavior: Behavior of the check functionality
    :ivar profile_name: Definition of the E2E profile.
    :ivar sync_counter_init: Number of checks required for validating
        the consistency of the counter that shall be received with a
        valid counter (i.e. counter within the allowed lock-in range)
        after the detection of an unexpected behavior of a received
        counter.
    :ivar upper_header_bits_to_shift: This attribute describes the
        number of upper-header bits to be shifted. value = 0 or not
        present: shift of upper header is NOT performed. value &gt; 0:
        the E2E Transformer on the protect-side, takes the first
        upperHeaderBitsToShift bits from the upper buffer (e.g. SOME/IP
        header part generated by SOME/IP transformer) and shifts them
        towards the lower bytes and bits within the Data[] for the
        length of the E2E header (e.g. 12 bytes in case of E2E Profile
        4). This means the shift distance is fixed - it depends on the
        E2E header size - what is configured here is the number of bits
        that are to be shifted. This option is defined because the
        Some/IP header generated by SOME/IP transformer shall be, due to
        compatibility between non-protected and E2E-protected
        communication, at the same position, which is before E2E header.
    :ivar window_size: Size of the monitoring window for the E2E state
        machine.
    :ivar window_size_init: Size of the monitoring window of state Init
        for the E2E state machine.
    :ivar window_size_invalid: Size of the monitoring window of state
        Invalid for the E2E state machine.
    :ivar window_size_valid: Size of the monitoring window of state
        Valid for the E2E state machine.
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
        name = "END-TO-END-TRANSFORMATION-DESCRIPTION"

    desc: None | MultiLanguageOverviewParagraph = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: None | CategoryString = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: None | AdminData = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
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
    clear_from_valid_to_invalid: None | Boolean = field(
        default=None,
        metadata={
            "name": "CLEAR-FROM-VALID-TO-INVALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    counter_offset: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "COUNTER-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    crc_offset: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "CRC-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_id_mode: None | DataIdModeEnum = field(
        default=None,
        metadata={
            "name": "DATA-ID-MODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_id_nibble_offset: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "DATA-ID-NIBBLE-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    e_2_e_profile_compatibility_props_ref: (
        None
        | EndToEndTransformationDescription.E2EProfileCompatibilityPropsRef
    ) = field(
        default=None,
        metadata={
            "name": "E-2-E-PROFILE-COMPATIBILITY-PROPS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_delta_counter: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MAX-DELTA-COUNTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_error_state_init: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MAX-ERROR-STATE-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_error_state_invalid: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MAX-ERROR-STATE-INVALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_error_state_valid: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MAX-ERROR-STATE-VALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_no_new_or_repeated_data: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MAX-NO-NEW-OR-REPEATED-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min_ok_state_init: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MIN-OK-STATE-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min_ok_state_invalid: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MIN-OK-STATE-INVALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min_ok_state_valid: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MIN-OK-STATE-VALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    offset: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    profile_behavior: None | EndToEndProfileBehaviorEnum = field(
        default=None,
        metadata={
            "name": "PROFILE-BEHAVIOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    profile_name: None | NmtokenString = field(
        default=None,
        metadata={
            "name": "PROFILE-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sync_counter_init: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SYNC-COUNTER-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    upper_header_bits_to_shift: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "UPPER-HEADER-BITS-TO-SHIFT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    window_size: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "WINDOW-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    window_size_init: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "WINDOW-SIZE-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    window_size_invalid: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "WINDOW-SIZE-INVALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    window_size_valid: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "WINDOW-SIZE-VALID",
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

    @dataclass(kw_only=True)
    class E2EProfileCompatibilityPropsRef(Ref):
        dest: E2EProfileCompatibilityPropsSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
