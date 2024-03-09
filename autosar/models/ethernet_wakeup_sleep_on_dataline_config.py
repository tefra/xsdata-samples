from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .boolean import Boolean
from .category_string import CategoryString
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .short_name_fragment import ShortNameFragment
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EthernetWakeupSleepOnDatalineConfig:
    """EthernetWakeupSleepOnDatalineConfigSet is the main element that aggregates
    different config set regarding the wakeup and sleep on data line.

    An EthernetWakeupSleepOnDatalineConfigSet could aggregate multiple
    different configurations regarding the wakeup and sleep on dataline
    (EthernetWakeupSleepOnDatalineConfig).

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
    :ivar sleep_mode_execution_delay: Delay in seconds to perform a
        sleep request if the Ethernet hardware (PHY) detect a pending
        wake-up. This is used to avoid the race condition, if a sleep
        was requested while a wake-up of a neighboring PHY was received
        via a local wake-up connection (e.g. I/O pin).
    :ivar sleep_repetition_delay_of_sleep_request: Delay in seconds for
        a repetition of a sleep request. This is used to retry a
        synchronized shutdown of the connected Ethernet hardware (PHY)
        of the link partner.
    :ivar sleep_repetitions_of_sleep_request: Count of repetitions for a
        sleep on dataline. If a sleep is rejected by the linked
        communication partner, the sleep is repeated until the count of
        repetitions exceed. If count of repetitions exceed, the Ethernet
        hardware (PHY) transit to sleep without acknowledgement of the
        connected link partner.
    :ivar wakeup_forward_local_enabled: If enabled, then a remote wake-
        up received on the physical dataline (e.g. 100BASE-T1) is
        forwarded as local wake-up (e.g. via an I/O pin). If disabled,
        then a remote wake-up is not forwarded as local wake-up.
    :ivar wakeup_forward_remote_enabled: If enabled, then a local wake-
        up is forwarded to the physical dataline (e.g. 100BASE-T1). If
        disabled, then a local wake-up is not forwarded to the physical
        dataline.
    :ivar wakeup_local_detection_time: Specify the detection time if a
        local wake-up in seconds is present on the local wake-up
        connection (e.g. I/O pin). A local wake-up has to be present at
        least for wakeupLocalDetectionTime to be detected a valid local
        wake-up.
    :ivar wakeup_local_duration_time: Specify the duration of a local
        wake-up in seconds to be present on the local wake-up connection
        (e.g. I/O pin).
    :ivar wakeup_local_enabled: If enabled, then a local wake-up
        received via a local connection (e.g. I/O pin) shall be detected
        by the Ethernet hardware (PHY). If disabled, Ethernet hardware
        is not reacting on a local wake-up.
    :ivar wakeup_remote_enabled: If enabled, then a remote wake-up
        received via the physical dataline (e.g. 100BASE-T1) shall be
        detected by the Ethernet hardware (PHY). If disabled, Ethernet
        hardware is not reaction on a remote wake-up.
    :ivar wakeup_repetition_delay_of_wakeup_request: Delay in seconds
        for a repetition of a wake-up. This is used to increase the
        reliability in the network, such that an ECU which initiates the
        wake-up does repeat the wake-up and increase the probability
        that affected ECUs receive the wake-up.
    :ivar wakeup_repetitions_of_wakeup_request: Count of repetitions for
        a wake-up. This is used to increase the reliability in the
        network, such that an ECU which initiates the wake-up does
        repeat the wake-up and increase the probability that affected
        ECUs receive the wake-up.
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
        name = "ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG"

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
        "EthernetWakeupSleepOnDatalineConfig.ShortNameFragments"
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
    annotations: Optional[
        "EthernetWakeupSleepOnDatalineConfig.Annotations"
    ] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sleep_mode_execution_delay: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "SLEEP-MODE-EXECUTION-DELAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sleep_repetition_delay_of_sleep_request: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "SLEEP-REPETITION-DELAY-OF-SLEEP-REQUEST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sleep_repetitions_of_sleep_request: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SLEEP-REPETITIONS-OF-SLEEP-REQUEST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_forward_local_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "WAKEUP-FORWARD-LOCAL-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_forward_remote_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "WAKEUP-FORWARD-REMOTE-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_local_detection_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "WAKEUP-LOCAL-DETECTION-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_local_duration_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "WAKEUP-LOCAL-DURATION-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_local_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "WAKEUP-LOCAL-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_remote_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "WAKEUP-REMOTE-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_repetition_delay_of_wakeup_request: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "WAKEUP-REPETITION-DELAY-OF-WAKEUP-REQUEST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_repetitions_of_wakeup_request: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "WAKEUP-REPETITIONS-OF-WAKEUP-REQUEST",
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
