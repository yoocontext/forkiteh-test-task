from adaptix import (
    Retort,
    name_mapping,
)


account_response_retort = Retort(
    recipe=[
        name_mapping(
            map={
                "frozen_v2": "frozenV2",
                "asset_v2": "assetV2",
                "free_asset_net_usage_v2": "free_asset_net_usageV2",
            }
        ),
    ]
)