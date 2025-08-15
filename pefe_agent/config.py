CONFIG_FILE = "config.json"

from typing import List
from pefe_common.config import Config

schema = {
    "loader": ({
        "host": (str, None),
        "port": (int, None),
    }, None),

    "self": ({
        "lmdb_path": (str, None),
    }, None),

    "debug": (bool, False),

    # More examples:
    # "allowed_ips": (List[str], []),  # list of strings
    # "thresholds": (List[int], None, "Thresholds must be provided and be integers."),
    # "nested_list": (List[nested_item_schema], [])
}

config = Config.load(schema, CONFIG_FILE)

# Examples
# print(config["self"]["host"])         # nested get
# print(config["allowed_ips"])            # list[str]
# print(config["nested_list"][0]["name"]) # list of nested dicts
