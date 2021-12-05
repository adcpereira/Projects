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
        #{"id" : Agent_id, "id2" : Agent_id2}

    def creat_document(self, name, manager, d_level, des):
        manager_obj = self.dict_agents[manager]
        self.dict_documents[name] = Document(name, d_level, manager_obj, desc)
        manager_obj.upload_doc(self.dict_documents[name])

    def get_doc_by_name(self, name):
        return self.dict_documents[name]

    def get_agent_by_id(self, id):
        return self.dict_agents[id]

    def list_docs(self):
        return sorted(self.dict_documents.keys())

    def list_ids(self):
        return sorted(self.dict_agents.keys())

    def level_by_id(self, id):
        agent = self.dict_agents[id]
        return agent.get_level_agent()

    def docs_by_id(self, id):
        agent = self.dict_agents[id]
        list_docs = agent.names_docs()
        return list_docs

    def names_docs_by_id(self, id):
        agent = self.dict_agents[id]
        list_docs = agent.names_docs()
        return list_docs

    def level_by_doc(self, doc_name):
        doc = self.dict_documents[doc_name]
        return doc.get_d_level_document()

    def write_document(self, doc_name, id, desc):
        doc = self.dict_documents[doc_name]
        doc.new_description(desc)
        agent = self.dict_agents[id]
        doc.add_acess(agent, WRITE)
        #criar uma funcao para atualizar os acessos

    def read_doc(self, doc_name, id):
        agent = self.dict_agents[id]
        doc = self.dict_documents[doc_name]
        doc.add_acess(agent, READ)
        return doc.get_description()
