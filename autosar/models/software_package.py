from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .crypto_service_certificate_subtypes_enum import CryptoServiceCertificateSubtypesEnum
from .function_group_state_in_function_group_set_instance_ref import FunctionGroupStateInFunctionGroupSetInstanceRef
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .revision_label_string import RevisionLabelString
from .short_name_fragment import ShortNameFragment
from .software_cluster_subtypes_enum import SoftwareClusterSubtypesEnum
from .software_package_action_type_enum import SoftwarePackageActionTypeEnum
from .strong_revision_label_string import StrongRevisionLabelString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SoftwarePackage:
    """
    This meta-class represents the ability to formalize the content of a
    software package.

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
    :ivar action_type: This attribute defines the action to be taken in
        the step of processing the enclosing SoftwarePackage.
    :ivar compressed_software_package_size: This size represents the
        size of the compressed SoftwarePackage.
    :ivar delta_package_applicable_version: This attribute identifies
        the version of the included SoftwareCluster for which the
        enclosing SoftwarePackage can be used as a delta update
    :ivar maximum_supported_ucm_version: This attribute identifies the
        maximum supported version of the UCM for this SoftwarePackage.
    :ivar minimum_supported_ucm_version: This attribute identifies the
        minimum supported version of the UCM for this SoftwarePackage.
    :ivar packager_id: This attribute identifies Id of the organization
        that provides the packager generating the SoftwarePackage.
    :ivar packager_signature_ref: This reference identifies the
        certificate that represents the packager's signature.
    :ivar post_verification_reboot: Reboot the platform after the
        verification of the activated software.
    :ivar pre_activate_irefs: The referenced function group states shall
        be established for the switch between the already installed and
        the activated software.
    :ivar pre_activation_reboot: Reboot the platform before the switch
        to the activated software.
    :ivar software_cluster_ref: This reference identifies the
        SoftwareCluster that belongs to the SoftwarePackage. The nature
        of this relation is actually more like an aggregation than a
        reference. But the relation is still modelled as a reference
        because two ARElements cannot aggregate each other.
    :ivar uncompressed_software_cluster_size: This attribute gives an
        indication about the storage that has to be available on the
        target.
    :ivar verify_irefs: The referenced function group states shall be
        established for the verification of the activated software.
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
        name = "SOFTWARE-PACKAGE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["SoftwarePackage.ShortNameFragments"] = field(
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
    annotations: Optional["SoftwarePackage.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
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
    action_type: Optional[SoftwarePackageActionTypeEnum] = field(
        default=None,
        metadata={
            "name": "ACTION-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    compressed_software_package_size: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "COMPRESSED-SOFTWARE-PACKAGE-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    delta_package_applicable_version: Optional[StrongRevisionLabelString] = field(
        default=None,
        metadata={
            "name": "DELTA-PACKAGE-APPLICABLE-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    maximum_supported_ucm_version: Optional[RevisionLabelString] = field(
        default=None,
        metadata={
            "name": "MAXIMUM-SUPPORTED-UCM-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    minimum_supported_ucm_version: Optional[RevisionLabelString] = field(
        default=None,
        metadata={
            "name": "MINIMUM-SUPPORTED-UCM-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    packager_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PACKAGER-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    packager_signature_ref: Optional["SoftwarePackage.PackagerSignatureRef"] = field(
        default=None,
        metadata={
            "name": "PACKAGER-SIGNATURE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    post_verification_reboot: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "POST-VERIFICATION-REBOOT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pre_activate_irefs: Optional["SoftwarePackage.PreActivateIrefs"] = field(
        default=None,
        metadata={
            "name": "PRE-ACTIVATE-IREFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pre_activation_reboot: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "PRE-ACTIVATION-REBOOT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    software_cluster_ref: Optional["SoftwarePackage.SoftwareClusterRef"] = field(
        default=None,
        metadata={
            "name": "SOFTWARE-CLUSTER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    uncompressed_software_cluster_size: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "UNCOMPRESSED-SOFTWARE-CLUSTER-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    verify_irefs: Optional["SoftwarePackage.VerifyIrefs"] = field(
        default=None,
        metadata={
            "name": "VERIFY-IREFS",
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
    class PackagerSignatureRef(Ref):
        dest: Optional[CryptoServiceCertificateSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class PreActivateIrefs:
        pre_activate_iref: List[FunctionGroupStateInFunctionGroupSetInstanceRef] = field(
            default_factory=list,
            metadata={
                "name": "PRE-ACTIVATE-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class SoftwareClusterRef(Ref):
        dest: Optional[SoftwareClusterSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class VerifyIrefs:
        verify_iref: List[FunctionGroupStateInFunctionGroupSetInstanceRef] = field(
            default_factory=list,
            metadata={
                "name": "VERIFY-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
