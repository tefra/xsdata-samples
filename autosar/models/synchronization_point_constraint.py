from dataclasses import dataclass, field
from typing import List, Optional
from .abstract_event_subtypes_enum import AbstractEventSubtypesEnum
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .eoc_executable_entity_ref_group_subtypes_enum import EocExecutableEntityRefGroupSubtypesEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .timing_condition_subtypes_enum import TimingConditionSubtypesEnum
from .traceable_subtypes_enum import TraceableSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SynchronizationPointConstraint:
    """
    This constraint is used to specify a synchronization point either between
    groups of executable entities or individual executable entities referenced
    via their corresponding RTE or BSW events.

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
    :ivar trace_refs: This assocation represents the ability to trace to
        upstream requirements / constraints. This supports for example
        the bottom up tracing ProjectObjectives &lt;- MainRequirements
        &lt;- Features &lt;- RequirementSpecs &lt;- BSW/AI
    :ivar timing_condition_ref: A timing condition the timing constraint
        depends on. In other words it specifies the condition the timing
        constraint holds.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar source_eec_refs: The source executable entities cluster
        containing the executable entities that shall finish execution
        before the synchronization point.
    :ivar source_event_refs: The executable entities --- referenced by
        their events --- that shall finish execution before the
        synchronization point.
    :ivar target_eec_refs: The target executable entities cluster
        containing the executable entities that shall start execution
        after the synchronization point.
    :ivar target_event_refs: The executable entities --- referenced by
        their events --- that shall start execution after the
        synchronization point.
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
        name = "SYNCHRONIZATION-POINT-CONSTRAINT"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["SynchronizationPointConstraint.ShortNameFragments"] = field(
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
    annotations: Optional["SynchronizationPointConstraint.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    trace_refs: Optional["SynchronizationPointConstraint.TraceRefs"] = field(
        default=None,
        metadata={
            "name": "TRACE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    timing_condition_ref: Optional["SynchronizationPointConstraint.TimingConditionRef"] = field(
        default=None,
        metadata={
            "name": "TIMING-CONDITION-REF",
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
    source_eec_refs: Optional["SynchronizationPointConstraint.SourceEecRefs"] = field(
        default=None,
        metadata={
            "name": "SOURCE-EEC-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    source_event_refs: Optional["SynchronizationPointConstraint.SourceEventRefs"] = field(
        default=None,
        metadata={
            "name": "SOURCE-EVENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_eec_refs: Optional["SynchronizationPointConstraint.TargetEecRefs"] = field(
        default=None,
        metadata={
            "name": "TARGET-EEC-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_event_refs: Optional["SynchronizationPointConstraint.TargetEventRefs"] = field(
        default=None,
        metadata={
            "name": "TARGET-EVENT-REFS",
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
    class TraceRefs:
        trace_ref: List["SynchronizationPointConstraint.TraceRefs.TraceRef"] = field(
            default_factory=list,
            metadata={
                "name": "TRACE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class TraceRef(Ref):
            dest: Optional[TraceableSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class TimingConditionRef(Ref):
        dest: Optional[TimingConditionSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SourceEecRefs:
        source_eec_ref: List["SynchronizationPointConstraint.SourceEecRefs.SourceEecRef"] = field(
            default_factory=list,
            metadata={
                "name": "SOURCE-EEC-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class SourceEecRef(Ref):
            dest: Optional[EocExecutableEntityRefGroupSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class SourceEventRefs:
        source_event_ref: List["SynchronizationPointConstraint.SourceEventRefs.SourceEventRef"] = field(
            default_factory=list,
            metadata={
                "name": "SOURCE-EVENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class SourceEventRef(Ref):
            dest: Optional[AbstractEventSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class TargetEecRefs:
        target_eec_ref: List["SynchronizationPointConstraint.TargetEecRefs.TargetEecRef"] = field(
            default_factory=list,
            metadata={
                "name": "TARGET-EEC-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class TargetEecRef(Ref):
            dest: Optional[EocExecutableEntityRefGroupSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class TargetEventRefs:
        target_event_ref: List["SynchronizationPointConstraint.TargetEventRefs.TargetEventRef"] = field(
            default_factory=list,
            metadata={
                "name": "TARGET-EVENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class TargetEventRef(Ref):
            dest: Optional[AbstractEventSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
