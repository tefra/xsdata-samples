from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .event_occurrence_kind_enum import EventOccurrenceKindEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multidimensional_time import MultidimensionalTime
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .synchronization_type_enum import SynchronizationTypeEnum
from .timing_condition_subtypes_enum import TimingConditionSubtypesEnum
from .timing_description_event_chain_subtypes_enum import TimingDescriptionEventChainSubtypesEnum
from .timing_description_event_subtypes_enum import TimingDescriptionEventSubtypesEnum
from .traceable_subtypes_enum import TraceableSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SynchronizationTimingConstraint:
    """This constraint is used to restrict the timing behavior of different, but
    correlated events or event chains, with regard to synchronization.

    Thereby, in case of imposing a synchronization timing constraint on events or event chains the following two scenarios are supported:
    1) [synchronizationConstraintType=responseSynchronization] Events: An arbitrary number of correlated events which play the role of responses shall occur synchronously with respect to a predefined tolerance. Event Chains: An arbitrary number of correlated event chains with a common stimulus, but different responses, where the responses shall occur synchronously with respect to a predefined tolerance.
    2) [synchronizationConstraintType=stimulusSynchronization] Events: An arbitrary number of correlated events which play the role of stimuli shall occur synchronously with respect to a predefined tolerance. Event Chains: An arbitrary number of correlated event chains with a common response, but different stimuli, where the stimuli shall occur synchronously with respect to a predefined tolerance.
    In case of imposing a synchronization timing constraint on events the following two scenarios are supported:
    1) [eventOccurrenceKind=singleOccurrence] Any of the events shall occur only once in the given time interval.
    2) [eventOccurrenceKind=multipleOccurrences] Any of the events may occur more than once in the given time interval. In other words multiple occurrences of an event within the given time interval are permitted.

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
    :ivar event_occurrence_kind: The specific occurrence kind of an
        event occurring within the given time interval.
    :ivar scope_event_refs: The events that are in the scope of the
        constraint.
    :ivar scope_refs: The event chains that are in the scope of the
        constraint.
    :ivar synchronization_constraint_type: The specific type of this
        synchronization constraint.
    :ivar tolerance: The maximum time interval, within which the
        synchronized events shall occur.
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
        name = "SYNCHRONIZATION-TIMING-CONSTRAINT"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["SynchronizationTimingConstraint.ShortNameFragments"] = field(
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
    annotations: Optional["SynchronizationTimingConstraint.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    trace_refs: Optional["SynchronizationTimingConstraint.TraceRefs"] = field(
        default=None,
        metadata={
            "name": "TRACE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    timing_condition_ref: Optional["SynchronizationTimingConstraint.TimingConditionRef"] = field(
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
    event_occurrence_kind: Optional[EventOccurrenceKindEnum] = field(
        default=None,
        metadata={
            "name": "EVENT-OCCURRENCE-KIND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    scope_event_refs: Optional["SynchronizationTimingConstraint.ScopeEventRefs"] = field(
        default=None,
        metadata={
            "name": "SCOPE-EVENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    scope_refs: Optional["SynchronizationTimingConstraint.ScopeRefs"] = field(
        default=None,
        metadata={
            "name": "SCOPE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    synchronization_constraint_type: Optional[SynchronizationTypeEnum] = field(
        default=None,
        metadata={
            "name": "SYNCHRONIZATION-CONSTRAINT-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tolerance: Optional[MultidimensionalTime] = field(
        default=None,
        metadata={
            "name": "TOLERANCE",
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
        trace_ref: List["SynchronizationTimingConstraint.TraceRefs.TraceRef"] = field(
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
    class ScopeEventRefs:
        scope_event_ref: List["SynchronizationTimingConstraint.ScopeEventRefs.ScopeEventRef"] = field(
            default_factory=list,
            metadata={
                "name": "SCOPE-EVENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ScopeEventRef(Ref):
            dest: Optional[TimingDescriptionEventSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class ScopeRefs:
        scope_ref: List["SynchronizationTimingConstraint.ScopeRefs.ScopeRef"] = field(
            default_factory=list,
            metadata={
                "name": "SCOPE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ScopeRef(Ref):
            dest: Optional[TimingDescriptionEventChainSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
