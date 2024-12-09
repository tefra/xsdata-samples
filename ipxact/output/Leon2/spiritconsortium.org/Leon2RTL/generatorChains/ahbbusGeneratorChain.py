from ipxact.models.api_type import ApiType
from ipxact.models.description import Description
from ipxact.models.generator import Generator
from ipxact.models.generator_chain import GeneratorChain
from ipxact.models.generator_type import GeneratorType
from ipxact.models.ipxact_uri import IpxactUri


obj = GeneratorChain(
    vendor='spiritconsortium.org',
    library='Leon2RTL',
    name='ahbbusGeneratorChain',
    version='1.0',
    description=Description(
        value='Simple generator definition'
    ),
    generator=[
        Generator(
            name='rotateDefaultMaster',
            description=Description(
                value='Generator to increment the default master on a component with a vendor=spiritConsortium.org, library=Leon2RTL and name=ahbbus*'
            ),
            api_type=GeneratorType.ApiType(
                value=ApiType.TGI_2009
            ),
            generator_exe=IpxactUri(
                value='../ahbbus/1.2/generator/rotateDefaultMaster.tcl'
            )
        ),
    ],
    chain_group=[
        GeneratorChain.ChainGroup(
            value='Example'
        ),
    ]
)
