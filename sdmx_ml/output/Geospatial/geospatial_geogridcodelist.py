from sdmx_ml.models.description import Description
from sdmx_ml.models.geo_grid_codelist_type import GeoGridCodelistType
from sdmx_ml.models.geo_grid_codelists_type import GeoGridCodelistsType
from sdmx_ml.models.item_type import GeoGridCode
from sdmx_ml.models.name import Name
from sdmx_ml.models.party_type import PartyType
from sdmx_ml.models.sender_type import SenderType
from sdmx_ml.models.structure import Structure
from sdmx_ml.models.structure_header_type import StructureHeaderType
from sdmx_ml.models.structures_type import StructuresType
from xsdata.models.datatype import XmlDateTime


obj = Structure(
    header=StructureHeaderType(
        id='IREF257793',
        prepared=XmlDateTime(2021, 3, 8, 17, 49, 35, 0, 0),
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
        geo_grid_codelists=GeoGridCodelistsType(
            geo_grid_codelist=[
                GeoGridCodelistType(
                    id='CL_GRID_LOCATION',
                    urn='urn:sdmx:org.sdmx.infomodel.codelist.Codelist=EXAMPLE:CL_GRID_LOCATION(1.0)',
                    name=[
                        Name(
                            value='Grid Location'
                        ),
                    ],
                    description=[
                        Description(
                            value='Example GeoGrid Codelist. The grid system is defined at the code list level, with each code being assigned to a specific cell in the grid by defining its row and column in GeoCell.'
                        ),
                    ],
                    version='1.0',
                    agency_id='EXAMPLE',
                    choice=[
                        GeoGridCode(
                            id='L1',
                            urn='urn:sdmx:org.sdmx.infomodel.codelist.Code=EXAMPLE:CL_GRID_LOCATION(1.0).L1',
                            name=[
                                Name(
                                    value='Location 1'
                                ),
                            ],
                            geo_cell='\n\t\t\t\t\t\tGEO_COL, GEO_ROW: GEO_TAG\n                    '
                        ),
                        GeoGridCode(
                            id='L2',
                            urn='urn:sdmx:org.sdmx.infomodel.codelist.Code=EXAMPLE:CL_GRID_LOCATION(1.0).L2',
                            name=[
                                Name(
                                    value='Location 2'
                                ),
                            ],
                            geo_cell='\n\t\t\t\t\t\tGEO_COL, GEO_ROW: GEO_TAG\n                    '
                        ),
                        GeoGridCode(
                            id='L3',
                            urn='urn:sdmx:org.sdmx.infomodel.codelist.Code=EXAMPLE:CL_GRID_LOCATION(1.0).L3',
                            name=[
                                Name(
                                    value='Location 3'
                                ),
                            ],
                            geo_cell='\n\t\t\t\t\t\tGEO_COL, GEO_ROW: GEO_TAG\n                    '
                        ),
                    ],
                    grid_definition='\n                    CRS:REFERENCE_CORNER; X_COORDINATE, Y_COORDINATE; CELL_WIDTH, CELL_HEIGHT: GEO_STD\n                '
                ),
            ]
        )
    )
)
