from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.acl_scope_enum import AclScopeEnum
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from autosar.models.atp_blueprint_subtypes_enum import AtpBlueprintSubtypesEnum
from autosar.models.atp_definition_subtypes_enum import AtpDefinitionSubtypesEnum
from autosar.models.autosar_engineering_object import AutosarEngineeringObject
from autosar.models.blueprint_policy_list import BlueprintPolicyList
from autosar.models.blueprint_policy_not_modifiable import BlueprintPolicyNotModifiable
from autosar.models.blueprint_policy_single import BlueprintPolicySingle
from autosar.models.category_string import CategoryString
from autosar.models.collection_subtypes_enum import CollectionSubtypesEnum
from autosar.models.identifier import Identifier
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.ref import Ref
from autosar.models.referrable_subtypes_enum import ReferrableSubtypesEnum
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class AclObjectSet:
    """This meta class represents the ability to denote a set of objects for
    which roles and rights (access control lists) shall be defined. It
    basically can define the objects based on.

    * the nature of objects
    * the involved blueprints
    * the artifact in which the objects are serialized
    * the definition of the object (in a definition - value pattern)
    * individual reference objects

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
    :ivar acl_object_classs:
    :ivar acl_scope: this indicates the scope of the referenced objects.
    :ivar collection_ref: This indicates that the relevant objects are
        specified via a collection.
    :ivar derived_from_blueprint_refs: This association indicates that
        the considered objects are the ones being derived from the
        associated blueprint.
    :ivar engineering_objects: This indicates an engineering object. The
        AclPermission relates to all objects in this partial model. This
        also implies that the other objects in this set shall be placed
        in the specified engineering object. Note that semantic
        constraints apply with respect to &lt;&lt;atpSplitable&gt;&gt;
    :ivar object_definition_refs: This denotes an object by its
        definition. For example the right to manipulate the value of a
        particular ecuc parameter is denoted by reference to the
        definition of the parameter. Note that this can also be a
        reference to a Standard Module Definition. Therefore it is
        stereotyped by atpUriDef.
    :ivar object_defintion_refs: Due to miss spell, this element was set
        to obsolete. use instead: objectDefinition.
    :ivar object_refs: This association applies a particular (usually
        small) set of objects (e.g. a singular package). Main usage is,
        if one does not want to create a collection specifically for
        access control.
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
        name = "ACL-OBJECT-SET"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["AclObjectSet.ShortNameFragments"] = field(
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
    annotations: Optional["AclObjectSet.Annotations"] = field(
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
    blueprint_policys: Optional["AclObjectSet.BlueprintPolicys"] = field(
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
    acl_object_classs: Optional["AclObjectSet.AclObjectClasss"] = field(
        default=None,
        metadata={
            "name": "ACL-OBJECT-CLASSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    acl_scope: Optional[AclScopeEnum] = field(
        default=None,
        metadata={
            "name": "ACL-SCOPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    collection_ref: Optional["AclObjectSet.CollectionRef"] = field(
        default=None,
        metadata={
            "name": "COLLECTION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    derived_from_blueprint_refs: Optional["AclObjectSet.DerivedFromBlueprintRefs"] = field(
        default=None,
        metadata={
            "name": "DERIVED-FROM-BLUEPRINT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    engineering_objects: Optional["AclObjectSet.EngineeringObjects"] = field(
        default=None,
        metadata={
            "name": "ENGINEERING-OBJECTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    object_definition_refs: Optional["AclObjectSet.ObjectDefinitionRefs"] = field(
        default=None,
        metadata={
            "name": "OBJECT-DEFINITION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    object_defintion_refs: Optional["AclObjectSet.ObjectDefintionRefs"] = field(
        default=None,
        metadata={
            "name": "OBJECT-DEFINTION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    object_refs: Optional["AclObjectSet.ObjectRefs"] = field(
        default=None,
        metadata={
            "name": "OBJECT-REFS",
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
    class AclObjectClasss:
        """
        :ivar acl_object_class: This specifies that the considered
            objects as instances of the denoted meta class.
        """
        acl_object_class: List[ReferrableSubtypesEnum] = field(
            default_factory=list,
            metadata={
                "name": "ACL-OBJECT-CLASS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class CollectionRef(Ref):
        dest: Optional[CollectionSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class DerivedFromBlueprintRefs:
        derived_from_blueprint_ref: List["AclObjectSet.DerivedFromBlueprintRefs.DerivedFromBlueprintRef"] = field(
            default_factory=list,
            metadata={
                "name": "DERIVED-FROM-BLUEPRINT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class DerivedFromBlueprintRef(Ref):
            dest: Optional[AtpBlueprintSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class EngineeringObjects:
        autosar_engineering_object: List[AutosarEngineeringObject] = field(
            default_factory=list,
            metadata={
                "name": "AUTOSAR-ENGINEERING-OBJECT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class ObjectDefinitionRefs:
        object_definition_ref: List["AclObjectSet.ObjectDefinitionRefs.ObjectDefinitionRef"] = field(
            default_factory=list,
            metadata={
                "name": "OBJECT-DEFINITION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ObjectDefinitionRef(Ref):
            dest: Optional[AtpDefinitionSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class ObjectDefintionRefs:
        object_defintion_ref: List["AclObjectSet.ObjectDefintionRefs.ObjectDefintionRef"] = field(
            default_factory=list,
            metadata={
                "name": "OBJECT-DEFINTION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ObjectDefintionRef(Ref):
            dest: Optional[AtpDefinitionSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class ObjectRefs:
        object_ref: List["AclObjectSet.ObjectRefs.ObjectRef"] = field(
            default_factory=list,
            metadata={
                "name": "OBJECT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ObjectRef(Ref):
            dest: Optional[ReferrableSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
