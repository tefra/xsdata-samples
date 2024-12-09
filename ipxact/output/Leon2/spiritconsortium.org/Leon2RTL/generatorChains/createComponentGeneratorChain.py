from ipxact.models.api_type import ApiType
from ipxact.models.description import Description
from ipxact.models.generator import Generator
from ipxact.models.generator_chain import GeneratorChain
from ipxact.models.generator_type import GeneratorType
from ipxact.models.ipxact_uri import IpxactUri


obj = GeneratorChain(
    vendor='spiritconsortium.org',
    library='Leon2RTL',
    name='createComponentGeneratorChain',
    version='1.0',
    description=Description(
        value='Simple generator definition'
    ),
    generator=[
        Generator(
            name='createComponent',
            description=Description(
                value='Generator that creates a component, registers it and adds it to a design'
            ),
            api_type=GeneratorType.ApiType(
                value=ApiType.TGI_2009
            ),
            generator_exe=IpxactUri(
                value='createComponent/createComponent.tcl'
            )
        ),
    ],
    chain_group=[
        GeneratorChain.ChainGroup(
            value='Example'
        ),
    ]
)
