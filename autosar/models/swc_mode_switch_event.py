from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from autosar.models.category_string import CategoryString
from autosar.models.executable_entity_activation_reason_subtypes_enum import ExecutableEntityActivationReasonSubtypesEnum
from autosar.models.identifier import Identifier
from autosar.models.mode_activation_kind import ModeActivationKind
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.r_mode_in_atomic_swc_instance_ref import RModeInAtomicSwcInstanceRef
from autosar.models.ref import Ref
from autosar.models.runnable_entity_subtypes_enum import RunnableEntitySubtypesEnum
from autosar.models.short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwcModeSwitchEvent:
    """
    This event is raised upon a received mode change.

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
    :ivar activation_reason_representation_ref: If the
        activationReasonRepresentation is referenced from the enclosing
        AbstractEvent this shall be taken as an indication that the
        latter contributes to the activating vector of this
        ExecutableEntity that owns the referenced
        ExecutableEntityActivationReason.
    :ivar disabled_mode_irefs: Reference to the Modes that disable the
        Event.
    :ivar start_on_event_ref: RunnableEntity starts when the
        corresponding RTEEvent occurs.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar activation: Specifies if the event is activated on entering or
        exiting the referenced Mode.
    :ivar mode_irefs: Reference to one or two Modes that initiate the
        SwcModeSwitchEvent.
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
        name = "SWC-MODE-SWITCH-EVENT"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["SwcModeSwitchEvent.ShortNameFragments"] = field(
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
    annotations: Optional["SwcModeSwitchEvent.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    activation_reason_representation_ref: Optional["SwcModeSwitchEvent.ActivationReasonRepresentationRef"] = field(
        default=None,
        metadata={
            "name": "ACTIVATION-REASON-REPRESENTATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    disabled_mode_irefs: Optional["SwcModeSwitchEvent.DisabledModeIrefs"] = field(
        default=None,
        metadata={
            "name": "DISABLED-MODE-IREFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    start_on_event_ref: Optional["SwcModeSwitchEvent.StartOnEventRef"] = field(
        default=None,
        metadata={
            "name": "START-ON-EVENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    activation: Optional[ModeActivationKind] = field(
        default=None,
        metadata={
            "name": "ACTIVATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mode_irefs: Optional["SwcModeSwitchEvent.ModeIrefs"] = field(
        default=None,
        metadata={
            "name": "MODE-IREFS",
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
    class ActivationReasonRepresentationRef(Ref):
        dest: Optional[ExecutableEntityActivationReasonSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class DisabledModeIrefs:
        disabled_mode_iref: List[RModeInAtomicSwcInstanceRef] = field(
            default_factory=list,
            metadata={
                "name": "DISABLED-MODE-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class StartOnEventRef(Ref):
        dest: Optional[RunnableEntitySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ModeIrefs:
        mode_iref: List[RModeInAtomicSwcInstanceRef] = field(
            default_factory=list,
            metadata={
                "name": "MODE-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 2,
            }
        )