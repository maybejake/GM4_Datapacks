import logging

from beet import Context, subproject

logger = logging.getLogger(__name__)

def beet_default(ctx: Context):
    # List of supported swing colors defined in beet.yaml as well as the guidebook page
    # for each supported swing color, generate all required code
    for color in ctx.meta['colors']:
        subproject_config = {
            "resource_pack": {
                "load": [
                    {
                        f"assets/gm4_swings/items/{color}_swing.json": "assets/gm4_swings/templates/items/swing.json"
                    }
                ],
                "render": {
                    "items": "*"
                }
            },
            "meta": {
                "swing_color": color
            }
        }

        ctx.require(subproject(subproject_config))
