from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.design_configuration import DesignConfiguration
from ipxact.models.library_ref_type import LibraryRefType


obj = DesignConfiguration(
    vendor='spiritconsortium.org',
    library='Leon2RTL',
    name='designConfig_apbSubSystem',
    version='4.0',
    design_ref=LibraryRefType(
        vendor='spiritconsortium.org',
        library='Leon2RTL',
        name='design_apbSubSystem',
        version='4.0'
    ),
    interconnection_configuration=[
        DesignConfiguration.InterconnectionConfiguration(
            interconnection_ref='defaultid4490193',
            abstractor_instances=[
                DesignConfiguration.InterconnectionConfiguration.AbstractorInstances(
                    abstractor_instance=[
                        DesignConfiguration.InterconnectionConfiguration.AbstractorInstances.AbstractorInstance(
                            instance_name='i_ArmAPB2SpiritAPB',
                            abstractor_ref=ConfigurableLibraryRefType(
                                vendor='spiritconsortium.org',
                                library='Leon2RTL',
                                name='ArmAPB2SpiritAPB',
                                version='1.0'
                            ),
                            view_name='vhdlsource'
                        ),
                    ]
                ),
            ]
        ),
        DesignConfiguration.InterconnectionConfiguration(
            interconnection_ref='defaultid4490210',
            abstractor_instances=[
                DesignConfiguration.InterconnectionConfiguration.AbstractorInstances(
                    abstractor_instance=[
                        DesignConfiguration.InterconnectionConfiguration.AbstractorInstances.AbstractorInstance(
                            instance_name='i_ArmAPB2SpiritAPB_1',
                            abstractor_ref=ConfigurableLibraryRefType(
                                vendor='spiritconsortium.org',
                                library='Leon2RTL',
                                name='ArmAPB2SpiritAPB',
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
