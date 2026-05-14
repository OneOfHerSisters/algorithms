import pandas as pd


def dict_to_dataframe(data: dict) -> pd.DataFrame:
    def flatten(obj, prefix=""):
        items = {}
        for key, value in obj.items():
            new_key = f"{prefix}__{key}" if prefix else key
            if isinstance(value, dict):
                items.update(flatten(value, new_key))
            else:
                items[new_key] = value
        return items

    flat = flatten(data)
    return pd.DataFrame([flat])
