from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.design_configuration import DesignConfiguration
from ipxact.models.library_ref_type import LibraryRefType


obj = DesignConfiguration(
    vendor='spiritconsortium.org',
    library='Leon2RTL',
    name='uartHierDesignConfig',
    version='1.0',
    design_ref=LibraryRefType(
        vendor='spiritconsortium.org',
        library='Leon2RTL',
        name='uartHierDesign',
        version='1.0'
    ),
    interconnection_configuration=[
        DesignConfiguration.InterconnectionConfiguration(
            interconnection_ref='ambaAPB',
            abstractor_instances=[
                DesignConfiguration.InterconnectionConfiguration.AbstractorInstances(
                    abstractor_instance=[
                        DesignConfiguration.InterconnectionConfiguration.AbstractorInstances.AbstractorInstance(
                            instance_name='APBRTLAbstractor',
                            abstractor_ref=ConfigurableLibraryRefType(
                                vendor='spiritconsortium.org',
                                library='Leon2RTL',
                                name='SpiritAPB2ArmAPB',
                                version='1.0'
                            ),
                            view_name='vhdlsource'
                        ),
                    ]
                ),
            ]
        ),
    ]
)
