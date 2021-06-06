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
from .boolean import Boolean
from .category_string import CategoryString
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .persistency_collection_level_update_strategy_enum import PersistencyCollectionLevelUpdateStrategyEnum
from .persistency_file_element import PersistencyFileElement
from .persistency_redundancy_crc import PersistencyRedundancyCrc
from .persistency_redundancy_enum import PersistencyRedundancyEnum
from .persistency_redundancy_hash import PersistencyRedundancyHash
from .persistency_redundancy_m_out_of_n import PersistencyRedundancyMOutOfN
from .positive_integer import PositiveInteger
from .service_provider_enum import ServiceProviderEnum
from .short_name_fragment import ShortNameFragment
from .string import String
from .symbol_props import SymbolProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PersistencyFileStorageInterface:
    """
    This meta-class provides the ability to implement a PortInterface for
    supporting persistency use cases for files.

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
    :ivar is_service: This flag is set if the PortInterface is to be
        used for communication between an * ApplicationSwComponentType
        or * ServiceProxySwComponentType or *
        SensorActuatorSwComponentType or *
        ComplexDeviceDriverSwComponentType * ServiceSwComponentType *
        EcuAbstractionSwComponentType and a ServiceSwComponentType
        (namely an AUTOSAR Service) located on the same ECU. Otherwise
        the flag is not set.
    :ivar namespaces: This represents the SymbolProps used for the
        definition of a hierarchical namespace applicable for the
        generation of code artifacts out of the definition of a
        ServiceInterface.
    :ivar service_kind: This attribute provides further details about
        the nature of the applied service.
    :ivar minimum_sustained_size: The value of this attribute represents
        the minimum size required at design time for the enclosing
        PersistencyInterface.
    :ivar redundancy: This attribute represents a requirement towards
        the redundancy of storage.
    :ivar redundancy_handlings: This aggregation represents the chosen
        approaches to handle redundancy for the various use cases
        implemented by subclasses
    :ivar update_strategy: This attribute can be used to specify the
        update strategy of the respective PersistencyInterface as a
        whole.
    :ivar file_elements: This aggregation represents the collection of
        PersistencyFileStorages in the context of the enclosing
        PersistencyFileStorageInterface.
    :ivar max_number_of_files: This attribute represents the definition
        of an upper bound for the handling of files at run-time in the
        context of the enclosing PersistencyFileStorageInterface.
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
        name = "PERSISTENCY-FILE-STORAGE-INTERFACE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["PersistencyFileStorageInterface.ShortNameFragments"] = field(
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
    annotations: Optional["PersistencyFileStorageInterface.Annotations"] = field(
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
    blueprint_policys: Optional["PersistencyFileStorageInterface.BlueprintPolicys"] = field(
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
    namespaces: Optional["PersistencyFileStorageInterface.Namespaces"] = field(
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
    minimum_sustained_size: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MINIMUM-SUSTAINED-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    redundancy: Optional[PersistencyRedundancyEnum] = field(
        default=None,
        metadata={
            "name": "REDUNDANCY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    redundancy_handlings: Optional["PersistencyFileStorageInterface.RedundancyHandlings"] = field(
        default=None,
        metadata={
            "name": "REDUNDANCY-HANDLINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    update_strategy: Optional[PersistencyCollectionLevelUpdateStrategyEnum] = field(
        default=None,
        metadata={
            "name": "UPDATE-STRATEGY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    file_elements: Optional["PersistencyFileStorageInterface.FileElements"] = field(
        default=None,
        metadata={
            "name": "FILE-ELEMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_number_of_files: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-NUMBER-OF-FILES",
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
    class RedundancyHandlings:
        persistency_redundancy_crc: List[PersistencyRedundancyCrc] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-REDUNDANCY-CRC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        persistency_redundancy_hash: List[PersistencyRedundancyHash] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-REDUNDANCY-HASH",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        persistency_redundancy_m_out_of_n: List[PersistencyRedundancyMOutOfN] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-REDUNDANCY-M-OUT-OF-N",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class FileElements:
        persistency_file_element: List[PersistencyFileElement] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-FILE-ELEMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
