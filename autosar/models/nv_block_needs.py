from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from autosar.models.boolean import Boolean
from autosar.models.category_string import CategoryString
from autosar.models.identifier import Identifier
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.nv_block_needs_reliability_enum import NvBlockNeedsReliabilityEnum
from autosar.models.nv_block_needs_writing_priority_enum import NvBlockNeedsWritingPriorityEnum
from autosar.models.positive_integer import PositiveInteger
from autosar.models.ram_block_status_control_enum import RamBlockStatusControlEnum
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class NvBlockNeeds:
    """
    Specifies the abstract needs on the configuration of a single NVRAM Block.

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
    :ivar calc_ram_block_crc: Defines if CRC (re)calculation for the
        permanent RAM Block is required.
    :ivar check_static_block_id: Defines if the Static Block Id check
        shall be enabled.
    :ivar cyclic_writing_period: This represents the period for cyclic
        writing of NvData to store the associated RAM Block.
    :ivar n_data_sets: Number of data sets to be provided by the NVRAM
        manager for this block. This is the total number of ROM Blocks
        and RAM Blocks.
    :ivar n_rom_blocks: Number of ROM Blocks to be provided by the NVRAM
        manager for this block. Please note that these multiple ROM
        Blocks are given in a contiguous area.
    :ivar ram_block_status_control: This attribute defines how the
        management of the RAM Block status is controlled.
    :ivar readonly: True: data of this NVRAM Block are write protected
        for normal operation (but protection can be disabled) false: no
        restriction
    :ivar reliability: Reliability against data loss on the non-volatile
        medium.
    :ivar resistant_to_changed_sw: Defines whether an NVRAM Block shall
        be treated resistant to configuration changes (true) or not
        (false). For details how to handle initialization in the latter
        case, please refer to the NVRAM specification.
    :ivar restore_at_start: Defines whether the associated RAM Block
        shall be implicitly restored during startup by the basic
        software.
    :ivar select_block_for_first_init_all: If this attribute is set to
        true the NvM shall process this block in the NvM_FirstInitAll()
        function.
    :ivar store_at_shutdown: Defines whether or not the associated RAM
        Block shall be implicitly stored during shutdown by the basic
        software.
    :ivar store_cyclic: Defines whether or not the associated RAM Block
        shall be implicitly stored periodically by the basic software.
    :ivar store_emergency: Defines whether or not the associated RAM
        Block shall be implicitly stored in case of ECU failure (e.g.
        loss of power) by the basic software. If the attribute
        storeEmergency is set to true the associated RAM Block shall be
        configured to have immediate priority.
    :ivar store_immediate: Defines whether or not the associated RAM
        Block shall be implicitly stored immediately during or after
        execution of the according SW-C RunnableEntity by the basic
        software.
    :ivar use_auto_validation_at_shut_down: If set to true the RAM Block
        shall be auto validated during shutdown phase.
    :ivar use_crc_comp_mechanism: If set to true the CRC of the RAM
        Block shall be compared during a write job with the CRC which
        was calculated during the last successful read or write job in
        order to skip unnecessary NVRAM writings.
    :ivar write_only_once: Defines write protection after first write:
        true: This block is prevented from being changed/erased or being
        replaced with the default ROM data after first initialization by
        the software-component. false: No such restriction.
    :ivar write_verification: Defines if Write Verification shall be
        enabled for this NVRAM Block.
    :ivar writing_frequency: Provides the amount of updates to this
        block from the application point of view. It has to be provided
        in "number of write access per year".
    :ivar writing_priority: Requires the priority of writing this block
        in case of concurrent requests to write other blocks.
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
        name = "NV-BLOCK-NEEDS"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["NvBlockNeeds.ShortNameFragments"] = field(
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
    annotations: Optional["NvBlockNeeds.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    calc_ram_block_crc: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CALC-RAM-BLOCK-CRC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    check_static_block_id: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CHECK-STATIC-BLOCK-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    cyclic_writing_period: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "CYCLIC-WRITING-PERIOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    n_data_sets: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "N-DATA-SETS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    n_rom_blocks: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "N-ROM-BLOCKS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ram_block_status_control: Optional[RamBlockStatusControlEnum] = field(
        default=None,
        metadata={
            "name": "RAM-BLOCK-STATUS-CONTROL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    readonly: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "READONLY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    reliability: Optional[NvBlockNeedsReliabilityEnum] = field(
        default=None,
        metadata={
            "name": "RELIABILITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    resistant_to_changed_sw: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "RESISTANT-TO-CHANGED-SW",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    restore_at_start: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "RESTORE-AT-START",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    select_block_for_first_init_all: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "SELECT-BLOCK-FOR-FIRST-INIT-ALL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    store_at_shutdown: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "STORE-AT-SHUTDOWN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    store_cyclic: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "STORE-CYCLIC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    store_emergency: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "STORE-EMERGENCY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    store_immediate: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "STORE-IMMEDIATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    use_auto_validation_at_shut_down: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "USE-AUTO-VALIDATION-AT-SHUT-DOWN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    use_crc_comp_mechanism: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "USE-CRC-COMP-MECHANISM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    write_only_once: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "WRITE-ONLY-ONCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    write_verification: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "WRITE-VERIFICATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    writing_frequency: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "WRITING-FREQUENCY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    writing_priority: Optional[NvBlockNeedsWritingPriorityEnum] = field(
        default=None,
        metadata={
            "name": "WRITING-PRIORITY",
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
