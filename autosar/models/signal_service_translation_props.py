from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from autosar.models.category_string import CategoryString
from autosar.models.consumed_event_group_subtypes_enum import ConsumedEventGroupSubtypesEnum
from autosar.models.event_handler_subtypes_enum import EventHandlerSubtypesEnum
from autosar.models.identifier import Identifier
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.pnc_mapping_ident_subtypes_enum import PncMappingIdentSubtypesEnum
from autosar.models.ref import Ref
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.signal_service_translation_control_enum import SignalServiceTranslationControlEnum
from autosar.models.signal_service_translation_event_props import SignalServiceTranslationEventProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SignalServiceTranslationProps:
    """
    This element allows to define the properties which are applicable for the
    signal-service-translation service.

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
        object in question.  More elaborate documentation, (in
        particular how the object is built or used) should go to
        "introduction".
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
    :ivar control_consumed_event_group_refs: Reference to the EventGroup
        which encapsulates the signal-based payload.
    :ivar control_pnc_refs: Reference to the PNCs which control the
        offer/subscribe behavior of the translated service instance.
    :ivar control_provided_event_group_refs: Reference to the provided
        event groups (aka EventHandler) which control the availability
        of the service instance.
    :ivar service_control: Defines how the service instance control
        shall behave.
    :ivar signal_service_translation_event_propss: Defines properties
        for a single translated event.
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
        different AUTOSAR models.  The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed.  An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """
    class Meta:
        name = "SIGNAL-SERVICE-TRANSLATION-PROPS"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["SignalServiceTranslationProps.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
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
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
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
    annotations: Optional["SignalServiceTranslationProps.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    control_consumed_event_group_refs: Optional["SignalServiceTranslationProps.ControlConsumedEventGroupRefs"] = field(
        default=None,
        metadata={
            "name": "CONTROL-CONSUMED-EVENT-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    control_pnc_refs: Optional["SignalServiceTranslationProps.ControlPncRefs"] = field(
        default=None,
        metadata={
            "name": "CONTROL-PNC-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    control_provided_event_group_refs: Optional["SignalServiceTranslationProps.ControlProvidedEventGroupRefs"] = field(
        default=None,
        metadata={
            "name": "CONTROL-PROVIDED-EVENT-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    service_control: Optional[SignalServiceTranslationControlEnum] = field(
        default=None,
        metadata={
            "name": "SERVICE-CONTROL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    signal_service_translation_event_propss: Optional["SignalServiceTranslationProps.SignalServiceTranslationEventPropss"] = field(
        default=None,
        metadata={
            "name": "SIGNAL-SERVICE-TRANSLATION-EVENT-PROPSS",
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
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        }
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class ControlConsumedEventGroupRefs:
        control_consumed_event_group_ref: List["SignalServiceTranslationProps.ControlConsumedEventGroupRefs.ControlConsumedEventGroupRef"] = field(
            default_factory=list,
            metadata={
                "name": "CONTROL-CONSUMED-EVENT-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ControlConsumedEventGroupRef(Ref):
            dest: Optional[ConsumedEventGroupSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class ControlPncRefs:
        control_pnc_ref: List["SignalServiceTranslationProps.ControlPncRefs.ControlPncRef"] = field(
            default_factory=list,
            metadata={
                "name": "CONTROL-PNC-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ControlPncRef(Ref):
            dest: Optional[PncMappingIdentSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class ControlProvidedEventGroupRefs:
        control_provided_event_group_ref: List["SignalServiceTranslationProps.ControlProvidedEventGroupRefs.ControlProvidedEventGroupRef"] = field(
            default_factory=list,
            metadata={
                "name": "CONTROL-PROVIDED-EVENT-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ControlProvidedEventGroupRef(Ref):
            dest: Optional[EventHandlerSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class SignalServiceTranslationEventPropss:
        signal_service_translation_event_props: List[SignalServiceTranslationEventProps] = field(
            default_factory=list,
            metadata={
                "name": "SIGNAL-SERVICE-TRANSLATION-EVENT-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
