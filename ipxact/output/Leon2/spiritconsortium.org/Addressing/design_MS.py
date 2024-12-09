from ipxact.models.active_interface import ActiveInterface
from ipxact.models.component_instance import ComponentInstance
from ipxact.models.component_instances import ComponentInstances
from ipxact.models.configurable_element_value import ConfigurableElementValue
from ipxact.models.configurable_element_values import ConfigurableElementValues
from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.description import Description
from ipxact.models.design import Design
from ipxact.models.instance_name import InstanceName
from ipxact.models.interconnection import Interconnection
from ipxact.models.interconnections import Interconnections


obj = Design(
    vendor='spiritconsortium.org',
    library='Addressing',
    name='design_MS',
    version='1.0',
    description=Description(
        value='Addressing example, master-slave'
    ),
    component_instances=ComponentInstances(
        component_instance=[
            ComponentInstance(
                instance_name=InstanceName(
                    value='i_directMaster'
                ),
                component_ref=ConfigurableLibraryRefType(
                    configurable_element_values=ConfigurableElementValues(
                        configurable_element_value=[
                            ConfigurableElementValue(
                                value='0',
                                reference_id='asBase'
                            ),
                            ConfigurableElementValue(
                                value='off',
                                reference_id='mSteer'
                            ),
                            ConfigurableElementValue(
                                value='4 * (2 ** 30)',
                                reference_id='asRange'
                            ),
                            ConfigurableElementValue(
                                value='32',
                                reference_id='asWidth'
                            ),
                            ConfigurableElementValue(
                                value='32',
                                reference_id='dataWidth'
                            ),
                            ConfigurableElementValue(
                                value='0',
                                reference_id='addr'
                            ),
                        ]
                    ),
                    vendor='spiritconsortium.org',
                    library='Addressing',
                    name='directMaster',
                    version='1.0'
                )
            ),
            ComponentInstance(
                instance_name=InstanceName(
                    value='i_directSlave'
                ),
                component_ref=ConfigurableLibraryRefType(
                    configurable_element_values=ConfigurableElementValues(
                        configurable_element_value=[
                            ConfigurableElementValue(
                                value='off',
                                reference_id='sSteer'
                            ),
                            ConfigurableElementValue(
                                value='0',
                                reference_id='mmBase'
                            ),
                            ConfigurableElementValue(
                                value="'h400",
                                reference_id='mmRange'
                            ),
                            ConfigurableElementValue(
                                value='32',
                                reference_id='mmWidth'
                            ),
                            ConfigurableElementValue(
                                value='32',
                                reference_id='dataWidth'
                            ),
                            ConfigurableElementValue(
                                value='0',
                                reference_id='addr'
                            ),
                        ]
                    ),
                    vendor='spiritconsortium.org',
                    library='Addressing',
                    name='directSlave',
                    version='1.0'
                )
            ),
        ]
    ),
    interconnections=Interconnections(
        interconnection=[
            Interconnection(
                name='m2s',
                active_interface=[
                    ActiveInterface(
                        component_instance_ref='i_directMaster',
                        bus_ref='directMaster'
                    ),
                    ActiveInterface(
                        component_instance_ref='i_directSlave',
                        bus_ref='directSlave'
                    ),
                ]
            ),
        ]
    )
)
