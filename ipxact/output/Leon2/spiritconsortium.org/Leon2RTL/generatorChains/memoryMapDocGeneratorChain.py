from ipxact.models.api_type import ApiType
from ipxact.models.description import Description
from ipxact.models.generator import Generator
from ipxact.models.generator_chain import GeneratorChain
from ipxact.models.generator_type import GeneratorType
from ipxact.models.ipxact_uri import IpxactUri


obj = GeneratorChain(
    vendor='spiritconsortium.org',
    library='Leon2RTL',
    name='MemoryMapDocGeneratorChain',
    version='1.0',
    description=Description(
        value='Simple generator definition'
    ),
    generator=[
        Generator(
            name='memoryMapDoc',
            description=Description(
                value='This generator displays for each bus interface master the base addresses and ranges for all connected bus interface slaves.'
            ),
            api_type=GeneratorType.ApiType(
                value=ApiType.TGI_2009
            ),
            generator_exe=IpxactUri(
                value='java -jar ../../../../Examples/TGIGeneratorExample2/Generators/MemoryMapDoc.jar'
            )
        ),
    ],
    chain_group=[
        GeneratorChain.ChainGroup(
            value='ExampleDocumentation'
        ),
    ]
)
