from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .diagnostic_access_permission_subtypes_enum import (
    DiagnosticAccessPermissionSubtypesEnum,
)
from .diagnostic_data_change_trigger import DiagnosticDataChangeTrigger
from .diagnostic_dtc_change_trigger import DiagnosticDtcChangeTrigger
from .diagnostic_event_window import DiagnosticEventWindow
from .diagnostic_response_on_event_action_enum import (
    DiagnosticResponseOnEventActionEnum,
)
from .diagnostic_response_on_event_class_subtypes_enum import (
    DiagnosticResponseOnEventClassSubtypesEnum,
)
from .diagnostic_store_event_support_enum import (
    DiagnosticStoreEventSupportEnum,
)
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticResponseOnEvent:
    """
    This represents an instance of the "Response on Event" diagnostic service.

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
    :ivar access_permission_ref: This represents the collection of
        DiagnosticAccessPermissions that allow for the execution of the
        referencing DiagnosticServiceInstance..
    :ivar events: This represents the collection of
        DiagnosticResponseOnEventTriggers defined in the context of the
        enclosing DiagnosticResponseOnEvent.
    :ivar event_windows: This represents the applicable
        DiagnosticEventWindows
    :ivar response_on_event_action: Defines sub-functions of the service
        ResponseOnEvent.
    :ivar response_on_event_class_ref: This reference substantiates that
        abstract reference in the role serviceClass for this specific
        concrete class. Thereby,  the reference represents the ability
        to access shared attributes among all DiagnosticResponseOnEvent
        in the given context.
    :ivar store_event_support: Defines how a specific event shall be
        handled.
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
        name = "DIAGNOSTIC-RESPONSE-ON-EVENT"

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
        "DiagnosticResponseOnEvent.ShortNameFragments"
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
    annotations: Optional["DiagnosticResponseOnEvent.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
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
    access_permission_ref: Optional[
        "DiagnosticResponseOnEvent.AccessPermissionRef"
    ] = field(
        default=None,
        metadata={
            "name": "ACCESS-PERMISSION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    events: Optional["DiagnosticResponseOnEvent.Events"] = field(
        default=None,
        metadata={
            "name": "EVENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_windows: Optional["DiagnosticResponseOnEvent.EventWindows"] = field(
        default=None,
        metadata={
            "name": "EVENT-WINDOWS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    response_on_event_action: Optional[DiagnosticResponseOnEventActionEnum] = (
        field(
            default=None,
            metadata={
                "name": "RESPONSE-ON-EVENT-ACTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    response_on_event_class_ref: Optional[
        "DiagnosticResponseOnEvent.ResponseOnEventClassRef"
    ] = field(
        default=None,
        metadata={
            "name": "RESPONSE-ON-EVENT-CLASS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    store_event_support: Optional[DiagnosticStoreEventSupportEnum] = field(
        default=None,
        metadata={
            "name": "STORE-EVENT-SUPPORT",
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
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class AccessPermissionRef(Ref):
        dest: Optional[DiagnosticAccessPermissionSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class Events:
        diagnostic_data_change_trigger: list[DiagnosticDataChangeTrigger] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-DATA-CHANGE-TRIGGER",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_dtc_change_trigger: list[DiagnosticDtcChangeTrigger] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-DTC-CHANGE-TRIGGER",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass
    class EventWindows:
        diagnostic_event_window: list[DiagnosticEventWindow] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-EVENT-WINDOW",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ResponseOnEventClassRef(Ref):
        dest: Optional[DiagnosticResponseOnEventClassSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
