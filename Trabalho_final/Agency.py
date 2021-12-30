from Agent import Agent
from Document import Document
READ = "read"
WRITE = "write"

class Agency:

    def __init__(self):
        self.dict_agents = {}
        self.dict_documents = {}

    def creat_agent(self, id, a_level):
        self.dict_agents[id] = Agent(id, a_level)
        # {"id" : Agent_id, "id2" : Agent_id2}

    def creat_document(self, doc_name, manager, d_level, desc):
        manager_obj = self.dict_agents[manager]
        self.dict_documents[doc_name + f"_{manager}"] = Document(doc_name, d_level, manager_obj, desc)
        manager_obj.upload_doc(self.dict_documents[doc_name + f"_{manager}"])

    def get_agent_by_id(self, id):
        return self.dict_agents[id]

    def list_docs(self):
        return list(self.dict_documents.keys())

    def list_ids(self):
        return list(self.dict_agents.keys())

    def level_by_id(self, id):
        agent = self.dict_agents[id]
        return agent.get_level_agent()

    def docs_by_id(self, id):
        agent = self.dict_agents[id]
        list_docs = list(agent.names_docs())
        return sorted(list_docs)

    def names_docs_by_id(self, id):
        agent = self.dict_agents[id]
        list_docs = agent.names_docs()
        return list_docs

    def level_by_doc(self, doc_name, manager):
        doc = self.dict_documents[doc_name + f"_{manager}"]
        return doc.get_d_level_document()

    def write_document(self, doc_name, id, manager, desc):
        doc = self.dict_documents[doc_name+ f"_{manager}"]
        doc.new_description(desc)
        doc.add_access(id, WRITE)

    def read_doc(self, doc_name, id, manager):
        doc = self.dict_documents[doc_name + f"_{manager}"]
        doc.add_access(id, READ)
        return doc.get_description()

    def grant(self, doc_name, id_grant, manager):
        doc = self.dict_documents[doc_name + f"_{manager}"]
        doc.add_grants_documents(id_grant)

    def grants_by_doc(self, doc_name, manager):
        doc = self.dict_documents[doc_name + f"_{manager}"]
        return doc.get_grants_documents()

    def accesses_by_doc(self, doc_name, manager):
        doc = self.dict_documents[doc_name + f"_{manager}"]
        return doc.get_accesses()
