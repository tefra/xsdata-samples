from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .diagnostic_clear_event_allowed_behavior_enum import (
    DiagnosticClearEventAllowedBehaviorEnum,
)
from .diagnostic_clear_event_behavior_enum import (
    DiagnosticClearEventBehaviorEnum,
)
from .diagnostic_connected_indicator import DiagnosticConnectedIndicator
from .diagnostic_event_clear_allowed_enum import (
    DiagnosticEventClearAllowedEnum,
)
from .diagnostic_event_kind_enum import DiagnosticEventKindEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .positive_integer_value_variation_point import (
    PositiveIntegerValueVariationPoint,
)
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class DiagnosticEvent:
    """
    This element is used to configure DiagnosticEvents.

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
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar aging_allowed: This represents the decision whether aging is
        allowed for this DiagnosticEvent.
    :ivar associated_event_identification: This attribute represents the
        identification number that is associated with the enclosing
        DiagnosticEvent and allows to identify it when placed into a
        snapshot record or extended data record storage. This value can
        be reported as internal data element in snapshot records or
        extended data records.
    :ivar clear_event_allowed_behavior: This attribute defines the
        resulting UDS status byte for the related event, which shall not
        be cleared according to the ClearEventAllowed callback
    :ivar clear_event_behavior: @RESTRICT_TO_STANDARD:AP! This attribute
        defines the resulting UDS DTC status byte for the related event,
        which shall not be cleared according to the ClearEventAllowed
        callback. @END_RESTRICT_TO_STANDARD! @RESTRICT_TO_STANDARD:CP!
        This attribute defines the resulting UDS status byte for the
        related event, which shall not be cleared according to the
        ClearEventAllowed callback. @END_RESTRICT_TO_STANDARD!
    :ivar confirmation_threshold: This attribute defines the number of
        operation cycles with a failed result before a confirmed DTC is
        set to 1. The semantic of this attribute is a by "1" increased
        value compared to the confirmation threshold of the "trip
        counter" mentioned in ISO 14229-1 in figure D.4. A value of "1"
        defines the immediate confirmation of the DTC along with the
        first reported failed. This is also sometimes called "zero trip
        DTC". A value of "2" defines a DTC confirmation in the operation
        cycle after the first occurred failed. A value of "2" is
        typically used in the US for OBD DTC confirmation.
    :ivar connected_indicators: Event specific description of
        Indicators. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar event_clear_allowed: This attribute defines whether the Dem
        has access to a "ClearEventAllowed" callback.
    :ivar event_failure_cycle_counter_threshold: This attribute defines
        the number of failure cycles for the event based fault
        confirmation.
    :ivar event_kind: This attribute is used to distinguish between SWC
        and BSW events.
    :ivar prestorage_freeze_frame: This attribute describes whether the
        Prestorage of FreezeFrames is supported by the assigned event or
        not. True: Prestorage of FreezeFrames is supported False:
        Prestorage of FreezeFrames is not supported
    :ivar prestored_freezeframe_stored_in_nvm: If the Event uses a
        prestored freeze-frame (using the operations PrestoreFreezeFrame
        and ClearPrestoredFreezeFrame of the service interface
        DiagnosticMonitor) this attribute indicates if the Event
        requires the data to be stored in non-volatile memory. TRUE =
        Dem shall store the prestored data in non-volatile memory, FALSE
        = Data can be lost at shutdown (not stored in Nvm)
    :ivar recoverable_in_same_operation_cycle: If the attribute is set
        to true then reporting PASSED will reset the indication of a
        failed test in the current operation cycle. If the attribute is
        set to false then reporting PASSED will be ignored and not lead
        to a reset of the indication of a failed test.
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
        name = "DIAGNOSTIC-EVENT"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: None | DiagnosticEvent.ShortNameFragments = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: None | MultilanguageLongName = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
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
    admin_data: None | AdminData = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
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
    annotations: None | DiagnosticEvent.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
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
    aging_allowed: None | Boolean = field(
        default=None,
        metadata={
            "name": "AGING-ALLOWED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    associated_event_identification: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "ASSOCIATED-EVENT-IDENTIFICATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    clear_event_allowed_behavior: (
        None | DiagnosticClearEventAllowedBehaviorEnum
    ) = field(
        default=None,
        metadata={
            "name": "CLEAR-EVENT-ALLOWED-BEHAVIOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    clear_event_behavior: None | DiagnosticClearEventBehaviorEnum = field(
        default=None,
        metadata={
            "name": "CLEAR-EVENT-BEHAVIOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    confirmation_threshold: None | PositiveIntegerValueVariationPoint = field(
        default=None,
        metadata={
            "name": "CONFIRMATION-THRESHOLD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    connected_indicators: None | DiagnosticEvent.ConnectedIndicators = field(
        default=None,
        metadata={
            "name": "CONNECTED-INDICATORS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_clear_allowed: None | DiagnosticEventClearAllowedEnum = field(
        default=None,
        metadata={
            "name": "EVENT-CLEAR-ALLOWED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_failure_cycle_counter_threshold: (
        None | PositiveIntegerValueVariationPoint
    ) = field(
        default=None,
        metadata={
            "name": "EVENT-FAILURE-CYCLE-COUNTER-THRESHOLD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_kind: None | DiagnosticEventKindEnum = field(
        default=None,
        metadata={
            "name": "EVENT-KIND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    prestorage_freeze_frame: None | Boolean = field(
        default=None,
        metadata={
            "name": "PRESTORAGE-FREEZE-FRAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    prestored_freezeframe_stored_in_nvm: None | Boolean = field(
        default=None,
        metadata={
            "name": "PRESTORED-FREEZEFRAME-STORED-IN-NVM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    recoverable_in_same_operation_cycle: None | Boolean = field(
        default=None,
        metadata={
            "name": "RECOVERABLE-IN-SAME-OPERATION-CYCLE",
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
    uuid: None | str = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ConnectedIndicators:
        diagnostic_connected_indicator: list[DiagnosticConnectedIndicator] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-CONNECTED-INDICATOR",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
