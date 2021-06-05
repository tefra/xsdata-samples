from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from autosar.models.boolean_value_variation_point import BooleanValueVariationPoint
from autosar.models.category_string import CategoryString
from autosar.models.identifier import Identifier
from autosar.models.integer import Integer
from autosar.models.integer_value_variation_point import IntegerValueVariationPoint
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagEventDebounceCounterBased:
    """This meta-class represents the ability to indicate that the counter-
    based debounce algorithm shall be used by the DEM for this diagnostic
    monitor.

    This is related to set the ECUC choice container
    DemDebounceAlgorithmClass to DemDebounceCounterBased.

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
    :ivar counter_based_fdc_threshold_storage_value: Threshold to
        allocate an event memory entry and to capture the Freeze Frame.
    :ivar counter_decrement_step_size: This value shall be taken to
        decrement the internal debounce counter.
    :ivar counter_failed_threshold: This value defines the event-
        specific limit that indicates the "failed" counter status.
    :ivar counter_increment_step_size: This value shall be taken to
        increment the internal debounce counter.
    :ivar counter_jump_down: This value activates or deactivates the
        counter jump-down behavior.
    :ivar counter_jump_down_value: This value represents the initial
        value of the internal debounce counter if the counting direction
        changes from incrementing to decrementing.
    :ivar counter_jump_up: This value activates or deactivates the
        counter jump-up behavior.
    :ivar counter_jump_up_value: This value represents the initial value
        of the internal debounce counter if the counting direction
        changes from decrementing to incrementing.
    :ivar counter_passed_threshold: This value defines the event-
        specific limit that indicates the "passed" counter status.
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
        name = "DIAG-EVENT-DEBOUNCE-COUNTER-BASED"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["DiagEventDebounceCounterBased.ShortNameFragments"] = field(
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
    annotations: Optional["DiagEventDebounceCounterBased.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    counter_based_fdc_threshold_storage_value: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "COUNTER-BASED-FDC-THRESHOLD-STORAGE-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    counter_decrement_step_size: Optional[IntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "COUNTER-DECREMENT-STEP-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    counter_failed_threshold: Optional[IntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "COUNTER-FAILED-THRESHOLD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    counter_increment_step_size: Optional[IntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "COUNTER-INCREMENT-STEP-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    counter_jump_down: Optional[BooleanValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "COUNTER-JUMP-DOWN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    counter_jump_down_value: Optional[IntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "COUNTER-JUMP-DOWN-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    counter_jump_up: Optional[BooleanValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "COUNTER-JUMP-UP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    counter_jump_up_value: Optional[IntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "COUNTER-JUMP-UP-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    counter_passed_threshold: Optional[IntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "COUNTER-PASSED-THRESHOLD",
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
