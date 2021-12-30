class Document:
    def __init__(self, name, d_level, manager, desc):
        self.name = name
        self.d_level = d_level
        self.manager = manager
        self.accesses = []
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

    def get_accesses_document(self):
        return self.accesses

    def add_grants_documents(self, name):
        self.grants.append(name)

    def get_grants_documents(self):
        return self.grants


    def get_description(self):
        return self.description

    def add_access(self, manager, action):
        self.accesses.append((manager, action))

    def get_accesses(self):
        return self.accesses