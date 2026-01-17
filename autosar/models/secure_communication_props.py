from dataclasses import dataclass, field
from typing import Optional

from .boolean import Boolean
from .positive_integer import PositiveInteger
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SecureCommunicationProps:
    """
    This meta-class contains configuration settings that are specific for
    an individual SecuredIPdu.

    :ivar auth_algorithm: This attribute defines the authentication
        algorithm used for MAC generation and verification.
    :ivar auth_data_freshness_length: This attribute defines the length
        in bits of the authentic PDU data that is passed to the SWC that
        verifies and generates the Freshness.
    :ivar auth_data_freshness_start_position: This value determines the
        start position in bits of the Authentic PDU that shall be passed
        on to the SWC that verifies and generates the Freshness. The bit
        counting is done according to TPS_SYST_01068.
    :ivar auth_info_tx_length: This attribute defines the length in bits
        of the authentication code to be included in the payload of the
        authenticated Pdu.
    :ivar authentication_build_attempts: This attribute specifies the
        number of authentication build attempts.
    :ivar authentication_retries: This attribute defines the additional
        number of authentication attempts that are to be carried out
        when the generation of the authentication information failed for
        a given SecuredIPdu. If zero is set than only one authentication
        attempt is done.
    :ivar data_id: This attribute defines a numerical identifier for the
        Secured I-PDU.
    :ivar freshness_counter_sync_attempts: This attribute defines the
        number of Freshness Counter re-synchronization attempts when a
        verification failed for a Secured I-PDU. If the value is zero,
        there will be no additional verification attempt to synchronize
        with a potentially better fitting Freshness Counter value. This
        attribute is only applicable if useFreshnessTimestamp is FALSE.
    :ivar freshness_timestamp_time_period_factor: This attribute defines
        a factor that specifies the time period for the Freshness
        Timestamp. It holds a multiplication factor that specifies the
        concrete meaning of a Freshness Timestamp increment by one on
        basis of microseconds.
    :ivar freshness_value_id: This attribute defines the Id of the
        Freshness Value. The Freshness Value might be a normal counter
        or a time value.
    :ivar freshness_value_length: This attribute defines the complete
        length in bits of the Freshness Value. As long as the key
        doesn't change the counter shall not overflow. The length of the
        counter shall be determined based on the expected life time of
        the corresponding key and frequency of usage of the counter.
    :ivar freshness_value_tx_length: This attribute defines the length
        in bits of the Freshness Value to be included in the payload of
        the Secured I-PDU. This length is specific to the least
        significant bits of the complete Freshness Counter. If the
        attribute is 0 no Freshness Value is included in the Secured
        I-PDU.
    :ivar message_link_length: SecOC links an AuthenticIPdu and
        CryptographicIPdu together by repeating a specific part (Message
        Linker) of the AuthenticIPdu in the CryptographicIPdu. This
        attribute defines the length in bits of the messageLinker.
    :ivar message_link_position: SecOC links an AuthenticIPdu and
        CryptographicIPdu together by repeating a specific part (Message
        Linker) of the AuthenticIPdu in the CryptographicIPdu. This
        attribute defines the startPosition in bits of the
        messageLinker.
    :ivar secondary_freshness_value_id: This attribute defines the Id of
        the Secondary Freshness Value. The Secondary Freshness Value
        might be a normal counter or a time value. Please note that this
        attribute is for documentation only to allow the configuration
        of required freshness value manager and no upstream mapping is
        defined for it.
    :ivar secured_area_length: This attribute defines the length in
        bytes of the area within the payload Pdu which will be secured.
    :ivar secured_area_offset: This attribute defines the start position
        (offset in byte) of the area within the payload Pdu which will
        be secured.
    :ivar use_freshness_timestamp: This attribute specifies whether the
        Freshness Value is generated through individual Freshness
        Counters or by a Timestamps. The value is set to TRUE when
        Timestamps are used.
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
    """

    class Meta:
        name = "SECURE-COMMUNICATION-PROPS"

    auth_algorithm: Optional[String] = field(
        default=None,
        metadata={
            "name": "AUTH-ALGORITHM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    auth_data_freshness_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "AUTH-DATA-FRESHNESS-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    auth_data_freshness_start_position: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "AUTH-DATA-FRESHNESS-START-POSITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    auth_info_tx_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "AUTH-INFO-TX-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    authentication_build_attempts: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "AUTHENTICATION-BUILD-ATTEMPTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    authentication_retries: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "AUTHENTICATION-RETRIES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "DATA-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    freshness_counter_sync_attempts: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "FRESHNESS-COUNTER-SYNC-ATTEMPTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    freshness_timestamp_time_period_factor: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "FRESHNESS-TIMESTAMP-TIME-PERIOD-FACTOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    freshness_value_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "FRESHNESS-VALUE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    freshness_value_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "FRESHNESS-VALUE-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    freshness_value_tx_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "FRESHNESS-VALUE-TX-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    message_link_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MESSAGE-LINK-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    message_link_position: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MESSAGE-LINK-POSITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    secondary_freshness_value_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SECONDARY-FRESHNESS-VALUE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    secured_area_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SECURED-AREA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    secured_area_offset: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SECURED-AREA-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    use_freshness_timestamp: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "USE-FRESHNESS-TIMESTAMP",
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
