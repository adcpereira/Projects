class Document:
    def __init__(self, name, d_level, manager, desc):
        self.name = name
        self.d_level = d_level
        self.manager = manager
        self.acesses = {}
        self.grants = []
        self.description = desc

    def new_description(self, description):
        self.description = description

    def get_name_document(self):
        return self.name

    def get_d_level_document(self):
        return self.d_level

    def get_manager_document(self):
        return self.manager

    def get_acesses_document(self):
        return self.acesses

    def get_grants_documents(self):
        return self.grants

    def get_description(self):
        return self.description

    def add_acess(self, manager, action):
        self.acesses[manager] = "read"





    """self.access = {}
    if "B" not in self.access:
        self.acces["B"] = []
    else:
        lista = self.acces["B"]
        lista.append()
    
    
    self.access = {"B" : ["read"] }
    self.access = {"B": ["read"].append("write")}"""
