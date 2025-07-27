from adaptix import (
    Retort,
    NameStyle,
    name_mapping,
)


account_resource_response_retort = Retort(
    recipe=[
        name_mapping(
    name_style=NameStyle.CAMEL,
            map={
                "total_energy_limit": "TotalEnergyLimit",
                "total_energy_weight": "TotalEnergyWeight",
                "total_net_weight": "TotalNetWeight",
                "total_net_limit": "TotalNetLimit",
            },
        )
    ]
)
