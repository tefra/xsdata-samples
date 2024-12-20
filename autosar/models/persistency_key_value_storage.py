from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .persistency_collection_level_update_strategy_enum import (
    PersistencyCollectionLevelUpdateStrategyEnum,
)
from .persistency_key_value_pair import PersistencyKeyValuePair
from .persistency_redundancy_crc import PersistencyRedundancyCrc
from .persistency_redundancy_hash import PersistencyRedundancyHash
from .persistency_redundancy_m_out_of_n import PersistencyRedundancyMOutOfN
from .positive_integer import PositiveInteger
from .positive_unlimited_integer import PositiveUnlimitedInteger
from .short_name_fragment import ShortNameFragment
from .uri_string import UriString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PersistencyKeyValueStorage:
    """
    This meta-class represents the ability to model a key-value storage  on
    deployment level.

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
    :ivar maximum_allowed_size: The value of this attribute represents
        the maximum size allowed at deployment time for the enclosing
        PersistencyDeployment.
    :ivar minimum_sustained_size: The value of this attribute represents
        the minimum size guaranteed at deployment time for the enclosing
        PersistencyDeployment.
    :ivar redundancy_handlings: This aggregation represents the chosen
        approaches to handle redundancy.
    :ivar update_strategy: This attribute shall be used to specify the
        update strategy of the respective PersistencyDeployment as a
        whole.
    :ivar key_value_pairs: This aggregation represents the key-value-
        pairs owned by the enclosing PersistencyKeyValueStorage.
    :ivar uri: This attribute holds the storage location for the
        PersistencyKeyValueStorage, e.g. file on the file system.
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
        name = "PERSISTENCY-KEY-VALUE-STORAGE"

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
        "PersistencyKeyValueStorage.ShortNameFragments"
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
    annotations: Optional["PersistencyKeyValueStorage.Annotations"] = field(
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
    maximum_allowed_size: Optional[PositiveUnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "MAXIMUM-ALLOWED-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minimum_sustained_size: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MINIMUM-SUSTAINED-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    redundancy_handlings: Optional[
        "PersistencyKeyValueStorage.RedundancyHandlings"
    ] = field(
        default=None,
        metadata={
            "name": "REDUNDANCY-HANDLINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    update_strategy: Optional[PersistencyCollectionLevelUpdateStrategyEnum] = (
        field(
            default=None,
            metadata={
                "name": "UPDATE-STRATEGY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    key_value_pairs: Optional["PersistencyKeyValueStorage.KeyValuePairs"] = (
        field(
            default=None,
            metadata={
                "name": "KEY-VALUE-PAIRS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    uri: Optional[UriString] = field(
        default=None,
        metadata={
            "name": "URI",
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
    class RedundancyHandlings:
        persistency_redundancy_crc: list[PersistencyRedundancyCrc] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-REDUNDANCY-CRC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        persistency_redundancy_hash: list[PersistencyRedundancyHash] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-REDUNDANCY-HASH",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        persistency_redundancy_m_out_of_n: list[
            PersistencyRedundancyMOutOfN
        ] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-REDUNDANCY-M-OUT-OF-N",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class KeyValuePairs:
        persistency_key_value_pair: list[PersistencyKeyValuePair] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-KEY-VALUE-PAIR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
