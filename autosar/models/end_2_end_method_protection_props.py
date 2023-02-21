from dataclasses import dataclass, field
from typing import List, Optional
from .e_2_e_profile_configuration_subtypes_enum import E2EProfileConfigurationSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .service_method_deployment_subtypes_enum import ServiceMethodDeploymentSubtypesEnum
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class End2EndMethodProtectionProps:
    """
    This element allows to protect a method, a field setter or a field getter with
    an E2E profile.

    :ivar data_ids:
    :ivar data_length: Length of payload including E2E header in bits.
    :ivar data_update_period: This attribute describes the period in
        which the applications are assumed to process E2E-protected
        messages. The middleware does not use this attribute at all.
    :ivar e_2_e_profile_configuration_ref: Reference to E2E profile
        configuration settings that are valid to protect the referenced
        method, field getter or field setter.
    :ivar max_data_length: Maximum length of payload including E2E
        header in bits.
    :ivar method_ref: Reference to a method, a field getter or a field
        setter that is protected by the E2E profile.
    :ivar min_data_length: Minimum length of payload including E2E
        header in bits.
    :ivar source_id: This represents a unique numerical identifier
        identifying the source of a certain transmission. In case of C/S
        communication, this ID uniquely identifies the client. Note: ID
        is used for protection against masquerading. The details
        concerning the maximum number of values (this information is
        specific for each E2E profile) applicable for this attribute are
        controlled by a semantic constraint that depends on the category
        of the EndToEndProtection.
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
        name = "END-2-END-METHOD-PROTECTION-PROPS"

    data_ids: Optional["End2EndMethodProtectionProps.DataIds"] = field(
        default=None,
        metadata={
            "name": "DATA-IDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    data_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "DATA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    data_update_period: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "DATA-UPDATE-PERIOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    e_2_e_profile_configuration_ref: Optional["End2EndMethodProtectionProps.E2EProfileConfigurationRef"] = field(
        default=None,
        metadata={
            "name": "E-2-E-PROFILE-CONFIGURATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_data_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-DATA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    method_ref: Optional["End2EndMethodProtectionProps.MethodRef"] = field(
        default=None,
        metadata={
            "name": "METHOD-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    min_data_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MIN-DATA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    source_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SOURCE-ID",
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

    @dataclass
    class DataIds:
        """
        :ivar data_id: This represents a numerical identifier that is
            included in the CRC calculation. This dataId is used for
            call and response. Note: ID is used for protection against
            masquerading. The details concerning the maximum number of
            values (this information is specific for each E2E profile)
            applicable for this attribute are controlled by a semantic
            constraint that depends on the category of the
            EndToEndProtection.
        """
        data_id: List[PositiveInteger] = field(
            default_factory=list,
            metadata={
                "name": "DATA-ID",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class E2EProfileConfigurationRef(Ref):
        dest: Optional[E2EProfileConfigurationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class MethodRef(Ref):
        dest: Optional[ServiceMethodDeploymentSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
