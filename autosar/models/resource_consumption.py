from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.access_count_set import AccessCountSet
from autosar.models.analyzed_execution_time import AnalyzedExecutionTime
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from autosar.models.category_string import CategoryString
from autosar.models.identifier import Identifier
from autosar.models.measured_execution_time import MeasuredExecutionTime
from autosar.models.measured_heap_usage import MeasuredHeapUsage
from autosar.models.measured_stack_usage import MeasuredStackUsage
from autosar.models.memory_section import MemorySection
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.rough_estimate_heap_usage import RoughEstimateHeapUsage
from autosar.models.rough_estimate_of_execution_time import RoughEstimateOfExecutionTime
from autosar.models.rough_estimate_stack_usage import RoughEstimateStackUsage
from autosar.models.section_name_prefix import SectionNamePrefix
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.simulated_execution_time import SimulatedExecutionTime
from autosar.models.system_memory_usage import SystemMemoryUsage
from autosar.models.worst_case_heap_usage import WorstCaseHeapUsage
from autosar.models.worst_case_stack_usage import WorstCaseStackUsage

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ResourceConsumption:
    """
    Description of consumed resources by one implementation of a software.

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
    :ivar access_count_sets: Set of access count values The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar execution_times: Collection of the execution time descriptions
        for this implementation. The aggregation of executionTime is
        subject to variability with the purpose to support the
        conditional existence of runnable entities. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar heap_usages: Collection of the heap memory allocated by this
        implementation. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar memory_sections: An abstract memory section required by this
        Implementation. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar section_name_prefixs: A prefix to be used for the memory
        section symbol in the code. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar stack_usages: Collection of the stack memory usage for each
        runnable entity of this implementation. The aggregation of
        StackUsage is subject to variability with the purpose to support
        the conditional existence of runnable entities. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar system_memory_usages: Collection of the system memory
        allocated by the owner.
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
        name = "RESOURCE-CONSUMPTION"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["ResourceConsumption.ShortNameFragments"] = field(
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
    annotations: Optional["ResourceConsumption.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    access_count_sets: Optional["ResourceConsumption.AccessCountSets"] = field(
        default=None,
        metadata={
            "name": "ACCESS-COUNT-SETS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    execution_times: Optional["ResourceConsumption.ExecutionTimes"] = field(
        default=None,
        metadata={
            "name": "EXECUTION-TIMES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    heap_usages: Optional["ResourceConsumption.HeapUsages"] = field(
        default=None,
        metadata={
            "name": "HEAP-USAGES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    memory_sections: Optional["ResourceConsumption.MemorySections"] = field(
        default=None,
        metadata={
            "name": "MEMORY-SECTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    section_name_prefixs: Optional["ResourceConsumption.SectionNamePrefixs"] = field(
        default=None,
        metadata={
            "name": "SECTION-NAME-PREFIXS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    stack_usages: Optional["ResourceConsumption.StackUsages"] = field(
        default=None,
        metadata={
            "name": "STACK-USAGES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    system_memory_usages: Optional["ResourceConsumption.SystemMemoryUsages"] = field(
        default=None,
        metadata={
            "name": "SYSTEM-MEMORY-USAGES",
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
    class AccessCountSets:
        access_count_set: List[AccessCountSet] = field(
            default_factory=list,
            metadata={
                "name": "ACCESS-COUNT-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class ExecutionTimes:
        analyzed_execution_time: List[AnalyzedExecutionTime] = field(
            default_factory=list,
            metadata={
                "name": "ANALYZED-EXECUTION-TIME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        measured_execution_time: List[MeasuredExecutionTime] = field(
            default_factory=list,
            metadata={
                "name": "MEASURED-EXECUTION-TIME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        rough_estimate_of_execution_time: List[RoughEstimateOfExecutionTime] = field(
            default_factory=list,
            metadata={
                "name": "ROUGH-ESTIMATE-OF-EXECUTION-TIME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        simulated_execution_time: List[SimulatedExecutionTime] = field(
            default_factory=list,
            metadata={
                "name": "SIMULATED-EXECUTION-TIME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class HeapUsages:
        measured_heap_usage: List[MeasuredHeapUsage] = field(
            default_factory=list,
            metadata={
                "name": "MEASURED-HEAP-USAGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        rough_estimate_heap_usage: List[RoughEstimateHeapUsage] = field(
            default_factory=list,
            metadata={
                "name": "ROUGH-ESTIMATE-HEAP-USAGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        worst_case_heap_usage: List[WorstCaseHeapUsage] = field(
            default_factory=list,
            metadata={
                "name": "WORST-CASE-HEAP-USAGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class MemorySections:
        memory_section: List[MemorySection] = field(
            default_factory=list,
            metadata={
                "name": "MEMORY-SECTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class SectionNamePrefixs:
        section_name_prefix: List[SectionNamePrefix] = field(
            default_factory=list,
            metadata={
                "name": "SECTION-NAME-PREFIX",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class StackUsages:
        measured_stack_usage: List[MeasuredStackUsage] = field(
            default_factory=list,
            metadata={
                "name": "MEASURED-STACK-USAGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        rough_estimate_stack_usage: List[RoughEstimateStackUsage] = field(
            default_factory=list,
            metadata={
                "name": "ROUGH-ESTIMATE-STACK-USAGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        worst_case_stack_usage: List[WorstCaseStackUsage] = field(
            default_factory=list,
            metadata={
                "name": "WORST-CASE-STACK-USAGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class SystemMemoryUsages:
        system_memory_usage: List[SystemMemoryUsage] = field(
            default_factory=list,
            metadata={
                "name": "SYSTEM-MEMORY-USAGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
