from dataclasses import dataclass, field

from ipxact.models.configurable_element_value import ConfigurableElementValue

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ConfigurableElementValues:
    """
    All configuration information for a contained component, generator,
    generator chain or abstractor instance.

    :ivar configurable_element_value: Describes the content of a
        configurable element. The required referenceId attribute refers
        to the ID attribute of the configurable element.
    """

    class Meta:
        name = "configurableElementValues"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    configurable_element_value: list[ConfigurableElementValue] = field(
        default_factory=list,
        metadata={
            "name": "configurableElementValue",
            "type": "Element",
            "min_occurs": 1,
        },
    )
