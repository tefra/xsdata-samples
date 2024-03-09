from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .boolean import Boolean
from .category_string import CategoryString
from .data_id_mode_enum import DataIdModeEnum
from .e_2_e_profile_compatibility_props_subtypes_enum import (
    E2EProfileCompatibilityPropsSubtypesEnum,
)
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .nmtoken_string import NmtokenString
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class E2EProfileConfiguration:
    """
    This element holds E2E profile specific configuration settings.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name: This specifies the long name of the object. Long
        name is targeted to human readers and acts like a headline.
    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particular
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Identifiable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar admin_data: This represents the administrative data for the
        identifiable object.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar annotations: Possibility to provide additional notes while
        defining a model element (e.g. the ECU Configuration Parameter
        Values). These are not intended as documentation but are mere
        design notes.
    :ivar clear_from_valid_to_invalid: Clear monitoring window on
        transition from state Valid to state Invalid.
    :ivar data_id_mode: This attribute describes the inclusion mode that
        is used to include the implicit Data ID in the one-byte CRC.
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
    :ivar min_ok_state_init: Minimal number of checks in which
        ProfileStatus equal to E2E_P_OK was determined, within the last
        WindowSize checks, for the state E2E_SM_INIT.
    :ivar min_ok_state_invalid: Minimal number of checks in which
        ProfileStatus equal to E2E_P_OK was determined, within the last
        WindowSize checks, for the state E2E_SM_INVALID.
    :ivar min_ok_state_valid: Minimal number of checks in which
        ProfileStatus equal to E2E_P_OK was determined, within the last
        WindowSize checks, for the state E2E_SM_VALID.
    :ivar profile_name: Definition of the E2E profile.
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
    :ivar uuid: The purpose of this attribute is to provide a globally
        unique identifier for an instance of a meta-class. The values of
        this attribute should be globally unique strings prefixed by the
        type of identifier.  For example, to include a DCE UUID as
        defined by The Open Group, the UUID would be preceded by "DCE:".
        The values of this attribute may be used to support merging of
        different AUTOSAR models. The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed. An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "E-2-E-PROFILE-CONFIGURATION"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional[
        "E2EProfileConfiguration.ShortNameFragments"
    ] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: Optional["E2EProfileConfiguration.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    clear_from_valid_to_invalid: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CLEAR-FROM-VALID-TO-INVALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_id_mode: Optional[DataIdModeEnum] = field(
        default=None,
        metadata={
            "name": "DATA-ID-MODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    e_2_e_profile_compatibility_props_ref: Optional[
        "E2EProfileConfiguration.E2EProfileCompatibilityPropsRef"
    ] = field(
        default=None,
        metadata={
            "name": "E-2-E-PROFILE-COMPATIBILITY-PROPS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_delta_counter: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-DELTA-COUNTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_error_state_init: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-ERROR-STATE-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_error_state_invalid: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-ERROR-STATE-INVALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_error_state_valid: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-ERROR-STATE-VALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min_ok_state_init: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MIN-OK-STATE-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min_ok_state_invalid: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MIN-OK-STATE-INVALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min_ok_state_valid: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MIN-OK-STATE-VALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    profile_name: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "PROFILE-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    window_size_init: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "WINDOW-SIZE-INIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    window_size_invalid: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "WINDOW-SIZE-INVALID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    window_size_valid: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "WINDOW-SIZE-VALID",
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
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class E2EProfileCompatibilityPropsRef(Ref):
        dest: Optional[E2EProfileCompatibilityPropsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
