class Agent:
    def __init__(self, id, a_level):
        self.id = id
        self.a_level = a_level
        self.uploaded_documents = []

    def get_id(self):
        return self.id

    def get_level_agent(self):
        return self.a_level

    def upload_doc(self, doc):
        self.uploaded_documents.append(doc)

    def get_uploaded_documents(self):
        return self.uploaded_documents

    def names_docs(self):
        list_name_docs = []
        for doc in self.uploaded_documents:
            list_name_docs.append(doc.get_name_document())
        return list_name_docs