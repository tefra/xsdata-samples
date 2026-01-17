from dataclasses import dataclass, field
from typing import Optional

from .adaptive_module_instantiation_subtypes_enum import (
    AdaptiveModuleInstantiationSubtypesEnum,
)
from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .ar_element_subtypes_enum import ArElementSubtypesEnum
from .category_string import CategoryString
from .crypto_service_certificate_subtypes_enum import (
    CryptoServiceCertificateSubtypesEnum,
)
from .diagnostic_contribution_set_subtypes_enum import (
    DiagnosticContributionSetSubtypesEnum,
)
from .documentation_subtypes_enum import DocumentationSubtypesEnum
from .fibex_element_subtypes_enum import FibexElementSubtypesEnum
from .identifier import Identifier
from .mode_declaration_group_prototype_subtypes_enum import (
    ModeDeclarationGroupPrototypeSubtypesEnum,
)
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .process_subtypes_enum import ProcessSubtypesEnum
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .software_cluster_dependency_formula import (
    SoftwareClusterDependencyFormula,
)
from .software_cluster_design_subtypes_enum import (
    SoftwareClusterDesignSubtypesEnum,
)
from .software_cluster_doip_diagnostic_address import (
    SoftwareClusterDoipDiagnosticAddress,
)
from .string import String
from .strong_revision_label_string import StrongRevisionLabelString
from .uploadable_package_element_subtypes_enum import (
    UploadablePackageElementSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SoftwareCluster:
    """
    This meta-class represents the ability to define an uploadable
    software-package, i.e. the SoftwareCluster shall contain all software
    and configuration for a given purpose.

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
    :ivar claimed_function_group_refs: Each SoftwareCluster can reserve
        the usage of a given functionGroup such that no other
        SoftwareCluster is allowed to use it
    :ivar conflicts_to: This aggregation handles conflicts. If it yields
        true then the SoftwareCluster shall not be installed.
    :ivar contained_ar_element_refs: This reference represents the
        collection of model elements that cannot derive from
        UploadablePackageElement and  that contribute to the
        completeness of the definition of the SoftwareCluster.
    :ivar contained_fibex_element_refs: This allows for referencing
        FibexElements that need to be considered in the context of a
        SoftwareCluster.
    :ivar contained_package_element_refs: This reference identifies
        model elements that are required to complete the manifest
        content.
    :ivar contained_process_refs: This reference represent the processes
        contained in the enclosing SoftwareCluster.
    :ivar depends_on: This aggregation can be taken to identify a
        dependency for the enclosing SoftwareCluster.
    :ivar design_refs: This reference represents the identification of
        all SoftwareClusterDesigns applicable for the enclosing
        SoftwareCluster.
    :ivar diagnostic_addresss: This aggregation represents the
        collection of diagnostic addresses that apply for the
        SoftwareCluster.
    :ivar diagnostic_extract_ref: This reference represents the
        definition of the diagnostic extract applicable to the
        referencing SoftwareCluster
    :ivar license_refs: This attribute allows for the inclusion of the
        the full text of a license of the enclosing SoftwareCluster. In
        many cases open source licenses require the inclusion of the
        full license text to any software that is released under the
        respective license.
    :ivar module_instantiation_refs: This reference identifies
        AdaptiveModuleInstantiations that need to be included with the
        SoftwareCluster in order to establish infrastructure required
        for the installation of the SoftwareCluster.
    :ivar release_notes_ref: This attribute allows for the explanations
        of changes since the previous version. The list of changes might
        require the creation of multiple paragraphs of test.
    :ivar type_approval: This attribute carries the homologation
        information that may be specific for a given country.
    :ivar vendor_id: Vendor ID of this Implementation according to the
        AUTOSAR vendor list.
    :ivar vendor_signature_ref: This reference identifies the
        certificate that represents the vendor's signature.
    :ivar version: This attribute can be used to describe a version
        information for the enclosing SoftwareCluster.
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
        name = "SOFTWARE-CLUSTER"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["SoftwareCluster.ShortNameFragments"] = (
        field(
            default=None,
            metadata={
                "name": "SHORT-NAME-FRAGMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    annotations: Optional["SoftwareCluster.Annotations"] = field(
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
    claimed_function_group_refs: Optional[
        "SoftwareCluster.ClaimedFunctionGroupRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CLAIMED-FUNCTION-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    conflicts_to: Optional[SoftwareClusterDependencyFormula] = field(
        default=None,
        metadata={
            "name": "CONFLICTS-TO",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    contained_ar_element_refs: Optional[
        "SoftwareCluster.ContainedArElementRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CONTAINED-AR-ELEMENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    contained_fibex_element_refs: Optional[
        "SoftwareCluster.ContainedFibexElementRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CONTAINED-FIBEX-ELEMENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    contained_package_element_refs: Optional[
        "SoftwareCluster.ContainedPackageElementRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CONTAINED-PACKAGE-ELEMENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    contained_process_refs: Optional[
        "SoftwareCluster.ContainedProcessRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CONTAINED-PROCESS-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    depends_on: Optional[SoftwareClusterDependencyFormula] = field(
        default=None,
        metadata={
            "name": "DEPENDS-ON",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    design_refs: Optional["SoftwareCluster.DesignRefs"] = field(
        default=None,
        metadata={
            "name": "DESIGN-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    diagnostic_addresss: Optional["SoftwareCluster.DiagnosticAddresss"] = (
        field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-ADDRESSS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    diagnostic_extract_ref: Optional[
        "SoftwareCluster.DiagnosticExtractRef"
    ] = field(
        default=None,
        metadata={
            "name": "DIAGNOSTIC-EXTRACT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    license_refs: Optional["SoftwareCluster.LicenseRefs"] = field(
        default=None,
        metadata={
            "name": "LICENSE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    module_instantiation_refs: Optional[
        "SoftwareCluster.ModuleInstantiationRefs"
    ] = field(
        default=None,
        metadata={
            "name": "MODULE-INSTANTIATION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    release_notes_ref: Optional["SoftwareCluster.ReleaseNotesRef"] = field(
        default=None,
        metadata={
            "name": "RELEASE-NOTES-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    type_approval: Optional[String] = field(
        default=None,
        metadata={
            "name": "TYPE-APPROVAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vendor_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "VENDOR-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vendor_signature_ref: Optional["SoftwareCluster.VendorSignatureRef"] = (
        field(
            default=None,
            metadata={
                "name": "VENDOR-SIGNATURE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    version: Optional[StrongRevisionLabelString] = field(
        default=None,
        metadata={
            "name": "VERSION",
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
    class ClaimedFunctionGroupRefs:
        claimed_function_group_ref: list[
            "SoftwareCluster.ClaimedFunctionGroupRefs.ClaimedFunctionGroupRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "CLAIMED-FUNCTION-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ClaimedFunctionGroupRef(Ref):
            dest: Optional[ModeDeclarationGroupPrototypeSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class ContainedArElementRefs:
        contained_ar_element_ref: list[
            "SoftwareCluster.ContainedArElementRefs.ContainedArElementRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONTAINED-AR-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ContainedArElementRef(Ref):
            dest: Optional[ArElementSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class ContainedFibexElementRefs:
        contained_fibex_element_ref: list[
            "SoftwareCluster.ContainedFibexElementRefs.ContainedFibexElementRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONTAINED-FIBEX-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ContainedFibexElementRef(Ref):
            dest: Optional[FibexElementSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class ContainedPackageElementRefs:
        contained_package_element_ref: list[
            "SoftwareCluster.ContainedPackageElementRefs.ContainedPackageElementRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONTAINED-PACKAGE-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ContainedPackageElementRef(Ref):
            dest: Optional[UploadablePackageElementSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class ContainedProcessRefs:
        contained_process_ref: list[
            "SoftwareCluster.ContainedProcessRefs.ContainedProcessRef"
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
            dest: Optional[ProcessSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class DesignRefs:
        design_ref: list["SoftwareCluster.DesignRefs.DesignRef"] = field(
            default_factory=list,
            metadata={
                "name": "DESIGN-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class DesignRef(Ref):
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
        software_cluster_doip_diagnostic_address: list[
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
    class DiagnosticExtractRef(Ref):
        dest: Optional[DiagnosticContributionSetSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class LicenseRefs:
        license_ref: list["SoftwareCluster.LicenseRefs.LicenseRef"] = field(
            default_factory=list,
            metadata={
                "name": "LICENSE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class LicenseRef(Ref):
            dest: Optional[DocumentationSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class ModuleInstantiationRefs:
        module_instantiation_ref: list[
            "SoftwareCluster.ModuleInstantiationRefs.ModuleInstantiationRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "MODULE-INSTANTIATION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ModuleInstantiationRef(Ref):
            dest: Optional[AdaptiveModuleInstantiationSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class ReleaseNotesRef(Ref):
        dest: Optional[DocumentationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class VendorSignatureRef(Ref):
        dest: Optional[CryptoServiceCertificateSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
