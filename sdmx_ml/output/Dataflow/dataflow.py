from sdmx_ml.models.dataflow_type import DataflowType
from sdmx_ml.models.dataflows_type import DataflowsType
from sdmx_ml.models.description import Description
from sdmx_ml.models.name import Name
from sdmx_ml.models.party_type import PartyType
from sdmx_ml.models.sender_type import SenderType
from sdmx_ml.models.structure import Structure
from sdmx_ml.models.structure_header_type import StructureHeaderType
from sdmx_ml.models.structures_type import StructuresType
from xsdata.models.datatype import XmlDateTime


obj = Structure(
    header=StructureHeaderType(
        id='IREF409212',
        prepared=XmlDateTime(2021, 3, 8, 22, 2, 1, 0, 0),
        sender=SenderType(
            id='Unknown'
        ),
        receiver=[
            PartyType(
                id='not_supplied'
            ),
        ]
    ),
    structures=StructuresType(
        dataflows=DataflowsType(
            dataflow=[
                DataflowType(
                    id='EXR',
                    urn='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=ECB:EXR(1.0)',
                    name=[
                        Name(
                            value='ECB Exchange Rates'
                        ),
                    ],
                    description=[
                        Description(
                            value="ECB Exchange Rates - example of a 'non-country-specific' data source"
                        ),
                    ],
                    version='1.0',
                    agency_id='ECB',
                    structure='urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=ECB:EXR(1.0)'
                ),
            ]
        )
    )
)
