from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .dependency_on_artifact_subtypes_enum import (
    DependencyOnArtifactSubtypesEnum,
)
from .exclusive_area_subtypes_enum import ExclusiveAreaSubtypesEnum
from .executable_entity_subtypes_enum import ExecutableEntitySubtypesEnum
from .hardware_configuration import HardwareConfiguration
from .hw_element_subtypes_enum import HwElementSubtypesEnum
from .identifier import Identifier
from .memory_section_location import MemorySectionLocation
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multidimensional_time import MultidimensionalTime
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .software_context import SoftwareContext

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class MeasuredExecutionTime:
    """
    Specifies the ExecutionTime which has been gathered using measurement means.

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
    :ivar exclusive_area_ref: Reference to the ExclusiveArea this
        execution time is provided for.
    :ivar executable_entity_ref: The executable entity for which this
        execution time is described.
    :ivar hardware_configuration: Provides information on the
        HardwareConfiguration used to specify this ExecutionTime.
    :ivar hw_element_ref: The hardware element (e.g. type of ECU) for
        which the execution time is specified.
    :ivar included_library_refs: If this dependency is specified, the
        execution time of the library code is included in the execution
        time data for the runnable.
    :ivar memory_section_locations: Provides information on the
        MemorySectionLocation which is involved in the ExecutionTime
        description.
    :ivar software_context: Provides information on the detailed
        SoftwareContext used to provide the ExecutionTime description.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar maximum_execution_time: The maximum measured execution time.
    :ivar minimum_execution_time: The minimum measured execution time.
    :ivar nominal_execution_time: The nominal measured execution time.
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
        name = "MEASURED-EXECUTION-TIME"

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
        "MeasuredExecutionTime.ShortNameFragments"
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
    annotations: Optional["MeasuredExecutionTime.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    exclusive_area_ref: Optional["MeasuredExecutionTime.ExclusiveAreaRef"] = (
        field(
            default=None,
            metadata={
                "name": "EXCLUSIVE-AREA-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    executable_entity_ref: Optional[
        "MeasuredExecutionTime.ExecutableEntityRef"
    ] = field(
        default=None,
        metadata={
            "name": "EXECUTABLE-ENTITY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    hardware_configuration: Optional[HardwareConfiguration] = field(
        default=None,
        metadata={
            "name": "HARDWARE-CONFIGURATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    hw_element_ref: Optional["MeasuredExecutionTime.HwElementRef"] = field(
        default=None,
        metadata={
            "name": "HW-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    included_library_refs: Optional[
        "MeasuredExecutionTime.IncludedLibraryRefs"
    ] = field(
        default=None,
        metadata={
            "name": "INCLUDED-LIBRARY-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    memory_section_locations: Optional[
        "MeasuredExecutionTime.MemorySectionLocations"
    ] = field(
        default=None,
        metadata={
            "name": "MEMORY-SECTION-LOCATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    software_context: Optional[SoftwareContext] = field(
        default=None,
        metadata={
            "name": "SOFTWARE-CONTEXT",
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
    maximum_execution_time: Optional[MultidimensionalTime] = field(
        default=None,
        metadata={
            "name": "MAXIMUM-EXECUTION-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minimum_execution_time: Optional[MultidimensionalTime] = field(
        default=None,
        metadata={
            "name": "MINIMUM-EXECUTION-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nominal_execution_time: Optional[MultidimensionalTime] = field(
        default=None,
        metadata={
            "name": "NOMINAL-EXECUTION-TIME",
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
    class ExclusiveAreaRef(Ref):
        dest: Optional[ExclusiveAreaSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ExecutableEntityRef(Ref):
        dest: Optional[ExecutableEntitySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class HwElementRef(Ref):
        dest: Optional[HwElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class IncludedLibraryRefs:
        included_library_ref: list[
            "MeasuredExecutionTime.IncludedLibraryRefs.IncludedLibraryRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "INCLUDED-LIBRARY-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class IncludedLibraryRef(Ref):
            dest: Optional[DependencyOnArtifactSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class MemorySectionLocations:
        memory_section_location: list[MemorySectionLocation] = field(
            default_factory=list,
            metadata={
                "name": "MEMORY-SECTION-LOCATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
