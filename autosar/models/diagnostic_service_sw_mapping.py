from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .bsw_service_dependency_ident_subtypes_enum import (
    BswServiceDependencyIdentSubtypesEnum,
)
from .category_string import CategoryString
from .diagnostic_data_element_subtypes_enum import (
    DiagnosticDataElementSubtypesEnum,
)
from .diagnostic_service_instance_subtypes_enum import (
    DiagnosticServiceInstanceSubtypesEnum,
)
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .process_design_subtypes_enum import ProcessDesignSubtypesEnum
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .swc_service_dependency_in_composition_instance_ref import (
    SwcServiceDependencyInCompositionInstanceRef,
)
from .swc_service_dependency_in_executable_instance_ref import (
    SwcServiceDependencyInExecutableInstanceRef,
)
from .swc_service_dependency_in_system_instance_ref import (
    SwcServiceDependencyInSystemInstanceRef,
)
from .swc_service_dependency_subtypes_enum import (
    SwcServiceDependencySubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticServiceSwMapping:
    """
    This represents the ability to define a mapping of a diagnostic service
    to a software-component or a basic-software module.

    If the former is used then this kind of service mapping is applicable
    for the usage of ClientServerInterfaces.

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
    :ivar diagnostic_data_element_ref: This represents a
        DiagnosticDataElement required to execute the respective
        diagnostic service in the context of the diagnostic service
        mapping,
    :ivar mapped_bsw_service_dependency_ref: This is supposed to
        represent a reference to a BswServiceDependency. the latter is
        not derived from Referrable and therefore this detour needs to
        be implemented to still let BswServiceDependency become the
        target of a reference.
    :ivar mapped_flat_swc_service_dependency_ref: This represents the
        ability to refer to an AtomicSwComponentType that is available
        without the definition of how it will be embedded into the
        component hierarchy.
    :ivar mapped_swc_service_dependency_in_executable_iref: This
        represents the ability to point into the component hiearchy of
        an adaptive AUTOSAR model (under possible consideration of the
        rootSoftwareComposition)
    :ivar mapped_swc_service_dependency_in_system_iref: This represents
        the ability to point into the component hiearchy (under possible
        consideration of the rootSoftwareComposition)
    :ivar mapped_swc_service_dependency_iref: This represents the
        ability to point into the component hiearchy (under possible
        consideration of the rootSoftwareComposition)
    :ivar process_ref: Reference to the representation of a Process that
        is required because the mapping could be different for different
        Processes referring to a specific Executable.
    :ivar service_instance_ref: This represents the service instance
        that needs to be considered in this diagnostics service mapping.
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
        name = "DIAGNOSTIC-SERVICE-SW-MAPPING"

    short_name: None | Identifier = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: (
        None | DiagnosticServiceSwMapping.ShortNameFragments
    ) = field(
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
    annotations: None | DiagnosticServiceSwMapping.Annotations = field(
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
    diagnostic_data_element_ref: (
        None | DiagnosticServiceSwMapping.DiagnosticDataElementRef
    ) = field(
        default=None,
        metadata={
            "name": "DIAGNOSTIC-DATA-ELEMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mapped_bsw_service_dependency_ref: (
        None | DiagnosticServiceSwMapping.MappedBswServiceDependencyRef
    ) = field(
        default=None,
        metadata={
            "name": "MAPPED-BSW-SERVICE-DEPENDENCY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mapped_flat_swc_service_dependency_ref: (
        None | DiagnosticServiceSwMapping.MappedFlatSwcServiceDependencyRef
    ) = field(
        default=None,
        metadata={
            "name": "MAPPED-FLAT-SWC-SERVICE-DEPENDENCY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mapped_swc_service_dependency_in_executable_iref: (
        None | SwcServiceDependencyInExecutableInstanceRef
    ) = field(
        default=None,
        metadata={
            "name": "MAPPED-SWC-SERVICE-DEPENDENCY-IN-EXECUTABLE-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mapped_swc_service_dependency_in_system_iref: (
        None | SwcServiceDependencyInSystemInstanceRef
    ) = field(
        default=None,
        metadata={
            "name": "MAPPED-SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mapped_swc_service_dependency_iref: (
        None | SwcServiceDependencyInCompositionInstanceRef
    ) = field(
        default=None,
        metadata={
            "name": "MAPPED-SWC-SERVICE-DEPENDENCY-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    process_ref: None | DiagnosticServiceSwMapping.ProcessRef = field(
        default=None,
        metadata={
            "name": "PROCESS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_instance_ref: (
        None | DiagnosticServiceSwMapping.ServiceInstanceRef
    ) = field(
        default=None,
        metadata={
            "name": "SERVICE-INSTANCE-REF",
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
    class DiagnosticDataElementRef(Ref):
        dest: None | DiagnosticDataElementSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class MappedBswServiceDependencyRef(Ref):
        dest: None | BswServiceDependencyIdentSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class MappedFlatSwcServiceDependencyRef(Ref):
        dest: None | SwcServiceDependencySubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ProcessRef(Ref):
        dest: None | ProcessDesignSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ServiceInstanceRef(Ref):
        dest: None | DiagnosticServiceInstanceSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
