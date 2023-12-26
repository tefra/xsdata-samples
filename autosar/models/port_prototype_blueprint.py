from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .blueprint_policy_list import BlueprintPolicyList
from .blueprint_policy_not_modifiable import BlueprintPolicyNotModifiable
from .blueprint_policy_single import BlueprintPolicySingle
from .category_string import CategoryString
from .client_com_spec import ClientComSpec
from .crypto_r_port_com_spec import CryptoRPortComSpec
from .field_sender_com_spec import FieldSenderComSpec
from .identifier import Identifier
from .mode_switch_receiver_com_spec import ModeSwitchReceiverComSpec
from .mode_switch_sender_com_spec import ModeSwitchSenderComSpec
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .nonqueued_receiver_com_spec import NonqueuedReceiverComSpec
from .nonqueued_sender_com_spec import NonqueuedSenderComSpec
from .nv_provide_com_spec import NvProvideComSpec
from .nv_require_com_spec import NvRequireComSpec
from .parameter_provide_com_spec import ParameterProvideComSpec
from .parameter_require_com_spec import ParameterRequireComSpec
from .persistency_data_required_com_spec import PersistencyDataRequiredComSpec
from .port_interface_subtypes_enum import PortInterfaceSubtypesEnum
from .port_prototype_blueprint_init_value import (
    PortPrototypeBlueprintInitValue,
)
from .queued_receiver_com_spec import QueuedReceiverComSpec
from .queued_sender_com_spec import QueuedSenderComSpec
from .ref import Ref
from .server_com_spec import ServerComSpec
from .short_name_fragment import ShortNameFragment
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PortPrototypeBlueprint:
    """This meta-class represents the ability to express a blueprint of a
    PortPrototype by referring to a particular PortInterface.

    This blueprint can then be used as a guidance to create particular
    PortPrototypes which are defined according to this blueprint. By
    this it is possible to standardize application interfaces without
    the need to also standardize software-components with PortPrototypes
    typed by the standardized PortInterfaces.

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
    :ivar blueprint_policys: This role indicates whether the
        blueprintable element will be modifiable or not motifiable.
    :ivar short_name_pattern: This attribute represents the pattern
        which shall be used to build the shortName of the derived
        elements. As of now it is modeled as a String.  In general it
        should follow the pattern: pattern = (placeholder | namePart)*
        placeholder = "{" namePart "}" namePart = identifier | "_" This
        is subject to be refined in subsequent versions. Note that this
        is marked as obsolete. Use the xml attribute namePattern instead
        as it applies to Identifier and CIdentifier (shortName, symbol
        etc.)
    :ivar init_values: This specifies the init values for the
        dataElements in the particular PortPrototypeBlueprint.
    :ivar interface_ref: This is the interface for which the blueprint
        is defined. It may be a blueprint itself  or a standardized
        PortInterface
    :ivar provided_com_specs: Provided communication attributes per
        interface element (data element or operation).
    :ivar required_com_specs: Required communication attributes, one for
        each interface element.
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
        name = "PORT-PROTOTYPE-BLUEPRINT"

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
        "PortPrototypeBlueprint.ShortNameFragments"
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
    annotations: Optional["PortPrototypeBlueprint.Annotations"] = field(
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
    blueprint_policys: Optional[
        "PortPrototypeBlueprint.BlueprintPolicys"
    ] = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    short_name_pattern: Optional[String] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-PATTERN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    init_values: Optional["PortPrototypeBlueprint.InitValues"] = field(
        default=None,
        metadata={
            "name": "INIT-VALUES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    interface_ref: Optional["PortPrototypeBlueprint.InterfaceRef"] = field(
        default=None,
        metadata={
            "name": "INTERFACE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    provided_com_specs: Optional[
        "PortPrototypeBlueprint.ProvidedComSpecs"
    ] = field(
        default=None,
        metadata={
            "name": "PROVIDED-COM-SPECS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_com_specs: Optional[
        "PortPrototypeBlueprint.RequiredComSpecs"
    ] = field(
        default=None,
        metadata={
            "name": "REQUIRED-COM-SPECS",
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
    class BlueprintPolicys:
        blueprint_policy_list: List[BlueprintPolicyList] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-LIST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        blueprint_policy_not_modifiable: List[
            BlueprintPolicyNotModifiable
        ] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-NOT-MODIFIABLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        blueprint_policy_single: List[BlueprintPolicySingle] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-SINGLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class InitValues:
        port_prototype_blueprint_init_value: List[
            PortPrototypeBlueprintInitValue
        ] = field(
            default_factory=list,
            metadata={
                "name": "PORT-PROTOTYPE-BLUEPRINT-INIT-VALUE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class InterfaceRef(Ref):
        dest: Optional[PortInterfaceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ProvidedComSpecs:
        field_sender_com_spec: List[FieldSenderComSpec] = field(
            default_factory=list,
            metadata={
                "name": "FIELD-SENDER-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        mode_switch_sender_com_spec: List[ModeSwitchSenderComSpec] = field(
            default_factory=list,
            metadata={
                "name": "MODE-SWITCH-SENDER-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        nonqueued_sender_com_spec: List[NonqueuedSenderComSpec] = field(
            default_factory=list,
            metadata={
                "name": "NONQUEUED-SENDER-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        nv_provide_com_spec: List[NvProvideComSpec] = field(
            default_factory=list,
            metadata={
                "name": "NV-PROVIDE-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        parameter_provide_com_spec: List[ParameterProvideComSpec] = field(
            default_factory=list,
            metadata={
                "name": "PARAMETER-PROVIDE-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        queued_sender_com_spec: List[QueuedSenderComSpec] = field(
            default_factory=list,
            metadata={
                "name": "QUEUED-SENDER-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        server_com_spec: List[ServerComSpec] = field(
            default_factory=list,
            metadata={
                "name": "SERVER-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RequiredComSpecs:
        client_com_spec: List[ClientComSpec] = field(
            default_factory=list,
            metadata={
                "name": "CLIENT-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        crypto_r_port_com_spec: List[CryptoRPortComSpec] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-R-PORT-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        mode_switch_receiver_com_spec: List[ModeSwitchReceiverComSpec] = field(
            default_factory=list,
            metadata={
                "name": "MODE-SWITCH-RECEIVER-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        nonqueued_receiver_com_spec: List[NonqueuedReceiverComSpec] = field(
            default_factory=list,
            metadata={
                "name": "NONQUEUED-RECEIVER-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        nv_require_com_spec: List[NvRequireComSpec] = field(
            default_factory=list,
            metadata={
                "name": "NV-REQUIRE-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        parameter_require_com_spec: List[ParameterRequireComSpec] = field(
            default_factory=list,
            metadata={
                "name": "PARAMETER-REQUIRE-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        persistency_data_required_com_spec: List[
            PersistencyDataRequiredComSpec
        ] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-DATA-REQUIRED-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        queued_receiver_com_spec: List[QueuedReceiverComSpec] = field(
            default_factory=list,
            metadata={
                "name": "QUEUED-RECEIVER-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
