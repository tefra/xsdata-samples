from dataclasses import dataclass, field
from typing import Optional
from autosar.models.ecuc_configuration_class_enum import EcucConfigurationClassEnum
from autosar.models.ecuc_configuration_variant_enum import EcucConfigurationVariantEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucImplementationConfigurationClass:
    """Specifies which ConfigurationClass this parameter has in the individual
    ConfigurationVariants.

    This element is removed from the specifications and therefore it
    shall not be used.

    :ivar config_class: Specifies the ConfigurationClass for the given
        ConfigurationVariant.
    :ivar config_variant: Specifies the ConfigurationVariant the
        ConfigurationClass is specified for.
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
        name = "ECUC-IMPLEMENTATION-CONFIGURATION-CLASS"

    config_class: Optional[EcucConfigurationClassEnum] = field(
        default=None,
        metadata={
            "name": "CONFIG-CLASS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    config_variant: Optional[EcucConfigurationVariantEnum] = field(
        default=None,
        metadata={
            "name": "CONFIG-VARIANT",
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
