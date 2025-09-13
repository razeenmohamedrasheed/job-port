def clean_metatdata(data: dict) -> dict:
    """
    Cleans only the 'experience' field in metadata by lowercasing keys and string values.
    """
    if "experience" in data and isinstance(data["experience"], dict):
        history = data["experience"].get("history", [])
        cleaned_history = []

        for exp in history:
            cleaned_exp = {}
            for key, value in exp.items():
                new_key = key.lower() if isinstance(key, str) else key
                if isinstance(value, str):
                    cleaned_exp[new_key] = value.lower()
                else:
                    cleaned_exp[new_key] = value
            cleaned_history.append(cleaned_exp)

        data["experience"]["history"] = cleaned_history
        
    return data
