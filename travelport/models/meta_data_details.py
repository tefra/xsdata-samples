from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class MetaDataDetails:
    """<xs:annotation xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:documentation>An element under which all other respective attributes for defining the settings are addressed.</xs:documentation>
    </xs:annotation>

    Parameters
    ----------
    element_name
        Whatever field/element name is triggered here, this will do the
        action on that particular field/element in the API database table.
    type_value
        Whatever field/element name is triggered here, this will do the
        action on that particular field/element in the API database table.
    customization
        This attribute captures the option for the action selected by admin
        in the UI screen, say Hide or View only or Edit.
    key
        This attribute will capture the unique identifier number assigned to
        the field.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    element_name: None | str = field(
        default=None,
        metadata={
            "name": "ElementName",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 50,
        },
    )
    customization: None | str = field(
        default=None,
        metadata={
            "name": "Customization",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        },
    )
    key: None | int = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
