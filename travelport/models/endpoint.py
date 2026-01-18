from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_endpoint_data_type import TypeEndpointDataType

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class Endpoint:
    """
    Endpoint information.

    Parameters
    ----------
    id
        Endpoint Id.
    name
        Endpoint Name.
    description
        Endpoint Description.
    data_type
        Data type (Boolean, String, etc) that defines what the endpoint
        consists of.
    min_occurs
        Refers to minimum times the endpoint can ocurr on the consuming
        system's page.  Default to 0.
    max_occurs
        Refers to the maximum times the endpoint can occur on the conuming
        system's page.
    end_point_code
        End Point Code description.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: int = field(
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    data_type: TypeEndpointDataType = field(
        metadata={
            "name": "DataType",
            "type": "Attribute",
            "required": True,
        }
    )
    min_occurs: int = field(
        default=0,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: None | int = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        },
    )
    end_point_code: str = field(
        metadata={
            "name": "EndPointCode",
            "type": "Attribute",
            "required": True,
        }
    )
