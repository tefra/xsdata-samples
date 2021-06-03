from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from autosar.models.blueprint_policy_list import BlueprintPolicyList
from autosar.models.blueprint_policy_not_modifiable import BlueprintPolicyNotModifiable
from autosar.models.blueprint_policy_single import BlueprintPolicySingle
from autosar.models.boolean import Boolean
from autosar.models.category_string import CategoryString
from autosar.models.crypto_key_slot_allowed_modification import CryptoKeySlotAllowedModification
from autosar.models.crypto_key_slot_content_allowed_usage import CryptoKeySlotContentAllowedUsage
from autosar.models.crypto_key_slot_type_enum import CryptoKeySlotTypeEnum
from autosar.models.crypto_object_type_enum import CryptoObjectTypeEnum
from autosar.models.identifier import Identifier
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.positive_integer import PositiveInteger
from autosar.models.service_provider_enum import ServiceProviderEnum
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.string import String
from autosar.models.symbol_props import SymbolProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CryptoKeySlotInterface:
    """
    This meta-class provides the ability to define a PortInterface for Crypto
    Key Slots.

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
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar blueprint_policys: This role indicates whether the
        blueprintable element will be modifiable or not motifiable.
    :ivar short_name_pattern: This attribute represents the pattern
        which shall be used to build the shortName of the derived
        elements. As of now it is modeled as a String.  In general it
        should follow the pattern:    pattern = (placeholder |
        namePart)*   placeholder = "{" namePart "}"   namePart =
        identifier | "_"  This is subject to be refined in subsequent
        versions.  Note that this is marked as obsolete. Use the xml
        attribute namePattern instead as it applies to Identifier and
        CIdentifier (shortName, symbol etc.)
    :ivar is_service: This flag is set if the PortInterface is to be
        used for communication between an * ApplicationSwComponentType
        or * ServiceProxySwComponentType or *
        SensorActuatorSwComponentType or *
        ComplexDeviceDriverSwComponentType * ServiceSwComponentType *
        EcuAbstractionSwComponentType  and a ServiceSwComponentType
        (namely an AUTOSAR Service) located on the same ECU. Otherwise
        the flag is not set.
    :ivar namespaces: This represents the SymbolProps used for the
        definition of a hierarchical namespace applicable for the
        generation of code artifacts out of the definition of a
        ServiceInterface.
    :ivar service_kind: This attribute provides further details about
        the nature of the applied service.
    :ivar allocate_shadow_copy: This attribute defines whether a shadow
        copy of this KeySlot shall be allocated to enable rollback of a
        failed KeySlot update campaign (see interface BeginTransaction).
    :ivar crypto_alg_id: This attribute defines a crypto algorithm
        restriction (kAlgIdAny means without restriction). The algorithm
        can be specified partially: family &amp; length, mode, padding.
        Future Crypto Providers can support some crypto algorithms that
        are not well known/ standardized today, therefore AUTOSAR
        doesn't provide a concrete list of crypto algorithms'
        identifiers and doesn't suppose usage of numerical identifiers.
        Instead of this a provider supplier should provide string names
        of supported algorithms in accompanying documentation. The name
        of a crypto algorithm shall follow the rules defined in the
        specification of cryptography for Adaptive Platform.
    :ivar crypto_object_type: Object type that can be stored in the
        slot.  If this field contains "Undefined" then mSlotCapacity
        must be provided and larger then 0
    :ivar key_slot_allowed_modification: Restricts how this keySlot may
        be used
    :ivar key_slot_content_allowed_usages: Restriction of allowed usage
        of a key stored to the slot.
    :ivar slot_capacity: Capacity of the slot in bytes to be reserved by
        the stack vendor. One use case is to define this value in case
        that the cryptoObjectType is undefined and the slot size can not
        be deduced from cryptoObjectType and cryptoAlgId.  "0" means
        slot size can be deduced from cryptoObjectType and cryptoAlgId.
    :ivar slot_type: This attribute defines whether the keySlot is
        exclusively used by the Application; or whether it is used by
        Stack Services and managed by a Key Manager Application.
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
        name = "CRYPTO-KEY-SLOT-INTERFACE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["CryptoKeySlotInterface.ShortNameFragments"] = field(
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
    annotations: Optional["CryptoKeySlotInterface.Annotations"] = field(
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
    blueprint_policys: Optional["CryptoKeySlotInterface.BlueprintPolicys"] = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    short_name_pattern: Optional[String] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-PATTERN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    is_service: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "IS-SERVICE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    namespaces: Optional["CryptoKeySlotInterface.Namespaces"] = field(
        default=None,
        metadata={
            "name": "NAMESPACES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    service_kind: Optional[ServiceProviderEnum] = field(
        default=None,
        metadata={
            "name": "SERVICE-KIND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    allocate_shadow_copy: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "ALLOCATE-SHADOW-COPY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    crypto_alg_id: Optional[String] = field(
        default=None,
        metadata={
            "name": "CRYPTO-ALG-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    crypto_object_type: Optional[CryptoObjectTypeEnum] = field(
        default=None,
        metadata={
            "name": "CRYPTO-OBJECT-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    key_slot_allowed_modification: Optional[CryptoKeySlotAllowedModification] = field(
        default=None,
        metadata={
            "name": "KEY-SLOT-ALLOWED-MODIFICATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    key_slot_content_allowed_usages: Optional["CryptoKeySlotInterface.KeySlotContentAllowedUsages"] = field(
        default=None,
        metadata={
            "name": "KEY-SLOT-CONTENT-ALLOWED-USAGES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    slot_capacity: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SLOT-CAPACITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    slot_type: Optional[CryptoKeySlotTypeEnum] = field(
        default=None,
        metadata={
            "name": "SLOT-TYPE",
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
    class BlueprintPolicys:
        blueprint_policy_list: List[BlueprintPolicyList] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-LIST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        blueprint_policy_not_modifiable: List[BlueprintPolicyNotModifiable] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-NOT-MODIFIABLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        blueprint_policy_single: List[BlueprintPolicySingle] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-SINGLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Namespaces:
        symbol_props: List[SymbolProps] = field(
            default_factory=list,
            metadata={
                "name": "SYMBOL-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class KeySlotContentAllowedUsages:
        crypto_key_slot_content_allowed_usage: List[CryptoKeySlotContentAllowedUsage] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-KEY-SLOT-CONTENT-ALLOWED-USAGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
