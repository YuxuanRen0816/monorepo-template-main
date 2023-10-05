import json

# Subclass of json.JSONEncoder
class CustomJSONEncoder(json.JSONEncoder):
    def encode(self, obj):
        if isinstance(obj, complex):
            return {"type": "complex", "real": obj.real, "imag": obj.imag}
        return super(CustomJSONEncoder, self).encode(obj)

# Subclass of json.JSONDecoder
class CustomJSONDecoder(json.JSONDecoder):
    def decode(self, json_string):
        obj = super(CustomJSONDecoder, self).decode(json_string)
        if "type" in obj and obj["type"] == "complex":
            return complex(obj["real"], obj["imag"])
        return obj

# Function named 'dumps' as a wrapper around json.dumps
def dumps(obj, **kwargs):
    return json.dumps(obj, cls=CustomJSONEncoder, **kwargs)

# Function named 'loads' as a wrapper around json.loads
def loads(json_string, **kwargs):
    return json.loads(json_string, cls=CustomJSONDecoder, **kwargs)

# Example usage
if __name__ == "__main__":
    # Using dumps
    complex_obj = complex(2, 3)
    json_str = dumps({"number": complex_obj})
    print("Custom dumps:", json_str)

    # Using loads
    decoded_obj = loads(json_str)
    print("Custom loads:", decoded_obj)
