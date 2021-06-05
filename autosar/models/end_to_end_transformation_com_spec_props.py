from dataclasses import dataclass, field
from typing import Optional
from autosar.models.annotation import (
    AdminData,
    DocumentationBlock,
)
from autosar.models.boolean import Boolean
from autosar.models.category_string import CategoryString
from autosar.models.e_2_e_profile_compatibility_props_subtypes_enum import E2EProfileCompatibilityPropsSubtypesEnum
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.positive_integer import PositiveInteger
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EndToEndTransformationComSpecProps:
    """
    The class EndToEndTransformationIComSpecProps specifies port specific
    configuration properties for EndToEnd transformer attributes.

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
    :ivar clear_from_valid_to_invalid: Clear monitoring window on
        transition from state Valid to state Invalid.
    :ivar disable_end_to_end_check: Disables/Enables the E2E check. The
        E2Eheader is removed from the payload independent from the
        setting of this attribute.
    :ivar disable_end_to_end_state_machine: Disables the E2EStateMachine
        (only E2E check functionality is performed)
    :ivar e_2_e_profile_compatibility_props_ref: Reference to additional
        settings for the E2E state machine.
    :ivar max_delta_counter: Maximum allowed difference between two
        counter values of two consecutively received valid messages. For
        example, if the receiver gets data with counter 1 and
        MaxDeltaCounter is 3, then at the next reception the receiver
        can accept Counters with values 2, 3 or 4.
    :ivar max_error_state_init: Maximal number of checks in which
        ProfileStatus equal to E2E_P_ERROR was determined, within the
        last WindowSize checks, for the state E2E_SM_INIT. The minimum
        value is 0.
    :ivar max_error_state_invalid: Maximal number of checks in which
        ProfileStatus equal to E2E_P_ERROR was determined, within the
        last WindowSize checks, for the state E2E_SM_INVALID. The
        minimum value is 0.
    :ivar max_error_state_valid: Maximal number of checks in which
        ProfileStatus equal to E2E_P_ERROR was determined, within the
        last WindowSize checks, for the state E2E_SM_VALID. The minimum
        value is 0.
    :ivar max_no_new_or_repeated_data: EndToEndTransformationDescription
        holds these attributes which are profile specific and have the
        same value for all E2E transformers.
    :ivar min_ok_state_init: Minimal number of checks in which
        ProfileStatus equal to E2E_P_OK was determined, within the last
        WindowSize checks, for the state E2E_SM_INIT. The minimum value
        is 1.
    :ivar min_ok_state_invalid: Minimal number of checks in which
        ProfileStatus equal to E2E_P_OK was determined, within the last
        WindowSize checks, for the state E2E_SM_INVALID. The minimum
        value is 1.
    :ivar min_ok_state_valid: Minimal number of checks in which
        ProfileStatus equal to E2E_P_OK was determined, within the last
        WindowSize checks, for the state E2E_SM_VALID. The minimum value
        is 1.
    :ivar sync_counter_init: EndToEndTransformationDescription holds
        these attributes which are profile specific and have the same
        value for all E2E transformers.
    :ivar window_size: Size of the monitoring window for the E2E state
        machine. The meaning is the number of correct cycles (E2E_P_OK)
        that are required in E2E_SM_INITCOM before the transition to
        E2E_SM_VALID. The minimum allowed value is 1.
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
        name = "END-TO-END-TRANSFORMATION-COM-SPEC-PROPS"

    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    clear_from_valid_to_invalid: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CLEAR-FROM-VALID-TO-INVALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    disable_end_to_end_check: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "DISABLE-END-TO-END-CHECK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    disable_end_to_end_state_machine: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "DISABLE-END-TO-END-STATE-MACHINE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    e_2_e_profile_compatibility_props_ref: Optional["EndToEndTransformationComSpecProps.E2EProfileCompatibilityPropsRef"] = field(
        default=None,
        metadata={
            "name": "E-2-E-PROFILE-COMPATIBILITY-PROPS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_delta_counter: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-DELTA-COUNTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_error_state_init: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-ERROR-STATE-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_error_state_invalid: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-ERROR-STATE-INVALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_error_state_valid: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-ERROR-STATE-VALID",
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
    min_ok_state_init: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MIN-OK-STATE-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    min_ok_state_invalid: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MIN-OK-STATE-INVALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    min_ok_state_valid: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MIN-OK-STATE-VALID",
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
    window_size: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "WINDOW-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    window_size_init: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "WINDOW-SIZE-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    window_size_invalid: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "WINDOW-SIZE-INVALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    window_size_valid: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "WINDOW-SIZE-VALID",
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
    class E2EProfileCompatibilityPropsRef(Ref):
        dest: Optional[E2EProfileCompatibilityPropsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
