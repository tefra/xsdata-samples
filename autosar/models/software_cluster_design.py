from dataclasses import dataclass, field
from typing import List, Optional
from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .ar_element_subtypes_enum import ArElementSubtypesEnum
from .category_string import CategoryString
from .diagnostic_contribution_set_subtypes_enum import (
    DiagnosticContributionSetSubtypesEnum,
)
from .fibex_element_subtypes_enum import FibexElementSubtypesEnum
from .identifier import Identifier
from .machine_design_subtypes_enum import MachineDesignSubtypesEnum
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .process_design_subtypes_enum import ProcessDesignSubtypesEnum
from .ref import Ref
from .root_sw_cluster_design_component_prototype import (
    RootSwClusterDesignComponentPrototype,
)
from .short_name_fragment import ShortNameFragment
from .software_cluster_design_subtypes_enum import (
    SoftwareClusterDesignSubtypesEnum,
)
from .software_cluster_doip_diagnostic_address import (
    SoftwareClusterDoipDiagnosticAddress,
)
from .uploadable_package_element_subtypes_enum import (
    UploadablePackageElementSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SoftwareClusterDesign:
    """
    This meta-class represents the ability for the OEM to design the grouping of
    software uploadable to a specific target Machine.

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
    :ivar contained_process_refs: This reference represent the
        ProcessDesigns contained in the enclosing SoftwareCluster.
    :ivar depends_on_refs: The owner SoftwareClusterDesign dependes on
        the referenced SoftwareClusterDesign
    :ivar diagnostic_addresss: This aggregaton is used to specify the
        diagnsotic address.
    :ivar diagnostic_contribution_refs: This reference identifes the
        corresponding collection of DiagnosticContributionSet.
    :ivar intended_target_machine_ref: This reference can be taken to
        identify the MachineDesign for which the final SoftwareCluster
        shall be developed.
    :ivar required_ar_element_refs: This reference represents the
        collection of ARElements that are required for the completeness
        of the definition of the SoftwareCluster.
    :ivar required_fibex_element_refs: This reference represents the
        collection of fibexElements that are required for the
        completeness of the definition of the SoftwareCluster.
    :ivar required_package_element_refs: This reference points to
        uploadable elements that have been identified as relevant in the
        context of the enclosing SoftwareClusterDesign.
    :ivar root_composition: This aggregation represents the design of
        the software inside the SwClusterDesign terms of the
        communication endpoints.
    :ivar sub_software_cluster_refs: This reference is used to identify
        the sub-SoftwareClusterDesigns of an "umbrella"
        SoftwareClusterDesign.
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
        name = "SOFTWARE-CLUSTER-DESIGN"

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
        "SoftwareClusterDesign.ShortNameFragments"
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
    annotations: Optional["SoftwareClusterDesign.Annotations"] = field(
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
    contained_process_refs: Optional[
        "SoftwareClusterDesign.ContainedProcessRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CONTAINED-PROCESS-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    depends_on_refs: Optional["SoftwareClusterDesign.DependsOnRefs"] = field(
        default=None,
        metadata={
            "name": "DEPENDS-ON-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    diagnostic_addresss: Optional[
        "SoftwareClusterDesign.DiagnosticAddresss"
    ] = field(
        default=None,
        metadata={
            "name": "DIAGNOSTIC-ADDRESSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    diagnostic_contribution_refs: Optional[
        "SoftwareClusterDesign.DiagnosticContributionRefs"
    ] = field(
        default=None,
        metadata={
            "name": "DIAGNOSTIC-CONTRIBUTION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    intended_target_machine_ref: Optional[
        "SoftwareClusterDesign.IntendedTargetMachineRef"
    ] = field(
        default=None,
        metadata={
            "name": "INTENDED-TARGET-MACHINE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_ar_element_refs: Optional[
        "SoftwareClusterDesign.RequiredArElementRefs"
    ] = field(
        default=None,
        metadata={
            "name": "REQUIRED-AR-ELEMENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_fibex_element_refs: Optional[
        "SoftwareClusterDesign.RequiredFibexElementRefs"
    ] = field(
        default=None,
        metadata={
            "name": "REQUIRED-FIBEX-ELEMENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_package_element_refs: Optional[
        "SoftwareClusterDesign.RequiredPackageElementRefs"
    ] = field(
        default=None,
        metadata={
            "name": "REQUIRED-PACKAGE-ELEMENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    root_composition: Optional[RootSwClusterDesignComponentPrototype] = field(
        default=None,
        metadata={
            "name": "ROOT-COMPOSITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sub_software_cluster_refs: Optional[
        "SoftwareClusterDesign.SubSoftwareClusterRefs"
    ] = field(
        default=None,
        metadata={
            "name": "SUB-SOFTWARE-CLUSTER-REFS",
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
    class ContainedProcessRefs:
        contained_process_ref: List[
            "SoftwareClusterDesign.ContainedProcessRefs.ContainedProcessRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONTAINED-PROCESS-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ContainedProcessRef(Ref):
            dest: Optional[ProcessDesignSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class DependsOnRefs:
        depends_on_ref: List[
            "SoftwareClusterDesign.DependsOnRefs.DependsOnRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "DEPENDS-ON-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class DependsOnRef(Ref):
            dest: Optional[SoftwareClusterDesignSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class DiagnosticAddresss:
        software_cluster_doip_diagnostic_address: List[
            SoftwareClusterDoipDiagnosticAddress
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOFTWARE-CLUSTER-DOIP-DIAGNOSTIC-ADDRESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DiagnosticContributionRefs:
        diagnostic_contribution_ref: List[
            "SoftwareClusterDesign.DiagnosticContributionRefs.DiagnosticContributionRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CONTRIBUTION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class DiagnosticContributionRef(Ref):
            dest: Optional[DiagnosticContributionSetSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class IntendedTargetMachineRef(Ref):
        dest: Optional[MachineDesignSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class RequiredArElementRefs:
        required_ar_element_ref: List[
            "SoftwareClusterDesign.RequiredArElementRefs.RequiredArElementRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "REQUIRED-AR-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class RequiredArElementRef(Ref):
            dest: Optional[ArElementSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class RequiredFibexElementRefs:
        required_fibex_element_ref: List[
            "SoftwareClusterDesign.RequiredFibexElementRefs.RequiredFibexElementRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "REQUIRED-FIBEX-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class RequiredFibexElementRef(Ref):
            dest: Optional[FibexElementSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class RequiredPackageElementRefs:
        required_package_element_ref: List[
            "SoftwareClusterDesign.RequiredPackageElementRefs.RequiredPackageElementRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "REQUIRED-PACKAGE-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class RequiredPackageElementRef(Ref):
            dest: Optional[UploadablePackageElementSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class SubSoftwareClusterRefs:
        sub_software_cluster_ref: List[
            "SoftwareClusterDesign.SubSoftwareClusterRefs.SubSoftwareClusterRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "SUB-SOFTWARE-CLUSTER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class SubSoftwareClusterRef(Ref):
            dest: Optional[SoftwareClusterDesignSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
