from dataclasses import dataclass

from sdmx_ml.models.registry_interface_type import RegistryInterfaceType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class RegistryInterface(RegistryInterfaceType):
    """
    RegistryInterface is used to conduct all interactions with the SDMX
    Registry Services.
    """

    class Meta:
        namespace = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"
