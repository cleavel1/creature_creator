class Species:
    def __init__(self, attribute_names: list[str]):
        self.attributes = []
        for name in attribute_names:
            self.attributes.append({
                    "name": name,
                    "attribute": ""
                })
            
    def set_attribute(self, name: str, attribute: str):
        for attr in self.attributes:
            if attr["name"] == name:
                attr["attribute"] = attribute


    