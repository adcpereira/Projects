from Agency import Agency

#Commands
REGISTER    = "register"
LISTUSERS   = "listusers"
UPLOAD      = "upload"
READ        = "read"
WRITE       = "write"
READ        = "read"
GRANT       = "grant"
USERDOCS    = "userdocs"
TOPLEAKED   = "topleaked"
TOPGRANTERS = "topgranters"
HELP        = "help"
EXIT        = "exit"

#Levels
OFFICIAL     = "official"
CONFIDENTIAL = "confidential"
SECRET       = "secret"
TOPSECRET    = "topsecret"

#Print Statments
UNKNOWN_COMMAND         = "Unknown command. Type help to see available commands"
USER_ALREADY_REGISTERED = "Identifier {} is already assigned to another user."
USER_REGISTER           = "User {} was registered."
NOT_REGISTERED_USER     = "Not a registered user"
DOC_ALREADY             = "Document {} already exists in the user account."
INSUFFICIENCENT_LEVEL   = "Insufficient security clearance."
DOC_UPLOADED            = "Document {} was uploaded"
DOC_NOT_EXIST_USER      = "Document {} does not exist in the user account."
DOC_UPDATED             = "Document {} was updated."

#Print Statements for HELP
REGISTER_HELP           = "register - registers a new user"
LISTUSERS_HELP          = "listusers - list all registered users"
UPLOAD_HELP             = "upload - upload a document"
READ_HELP               = "read - read a document"
WRITE_HELP              = "write - write a document"
GRANT_HELP              = "grant - grant access to a document"
USERDOCS_HELP           = "userdocs - list the official or classified documents of an user"
TOPLEAKED_HELP          = "topleaked - list the top 10 documents with more grants"
TOPGRANTERS_HELP        = "topgranters - list the top 10 users that have given more grants"
HELP_HELP               = "help - shows the available commands"
EXIT_HELP               = "exit - terminates the execution of the program"
DOCUMENT_DOES_NOT_EXIST = "Document {} does not exist in the user account."



def alguma():
    #print_inicial nome 0 0
    for list_access(manager):

    if len(access) == 0 and len(granst) == 0:
        print("nao ha acess")
        print("nao ha grants")

    DICT_DOC = agency.accese_by_doc(doc) #dicionário
    DICT_DOC[id_person]
    #oi ,oi
    for:
        texto
        texto = texto + ", " + str(id, action)
    print(texto)
    print("THERE ARE NO GRANTS")











def next_command():
    return input()

def register(agency):
    id = input()
    level = input()
    if id in agency.list_ids():
        print(USER_ALREADY_REGISTERED.format(id))
    else:
        agency.creat_agent(id, level)
        print(USER_REGISTER.format(id))

def list_users(agency):
    lista_agents = agency.list_ids()
    for agent in lista_agents:
        print(agent, agency.level_by_id(agent))

def upload(agency):
    name = input()
    id = input()
    d_level = input()
    desc = input()
    if id not in agency.list_ids():
        print(NOT_REGISTERED_USER)
    elif name in agency.names_docs_by_id(id):
        print(DOC_ALREADY.format(name))
    elif not can_access(agency.level_by_id(id), d_level):
        print(INSUFFICIENCENT_LEVEL)
    else:
        agency.creat_document(name, id, d_level, desc)
        print(DOC_UPLOADED.format(name))

def write(agency):
    doc_name = input()
    id_upload = input()
    id_write = input()
    desc = input()
    if (id_upload or id_write) not in agency.list_ids():
        print(NOT_REGISTERED_USER)
    elif doc_name not in agency.names_docs_by_id(id_upload):
        print(DOC_NOT_EXIST_USER.format(doc_name))
    elif not can_access(agency.level_by_id(id_write), agency.level_by_doc(doc_name)):
        print(INSUFFICIENCENT_LEVEL)
    else:
        agency.write_document(doc_name, id_write, desc)
        print(DOC_UPDATED.format(doc_name))

def read(agency):
    doc_name = input()
    id_upload = input()
    id_read = input()
    if (id_upload or id_read) not in agency.list_ids():
        print(NOT_REGISTERED_USER)
    elif doc_name not in agency.names_docs_by_id(id_upload):
        print(DOC_NOT_EXIST_USER.format(doc_name))
    elif not can_access(agency.level_by_id(id_read), agency.level_by_doc(doc_name)):
        print(INSUFFICIENCENT_LEVEL)
    else:
        print(agency.read_doc(doc_name, id_read)) #depois dividir a funcao

def grant(agency):
    pass

def userdocs(agency):
    pass

def topleaked(agency):
    pass

def topgranters(agency):
    pass

def help_print():
    print(REGISTER_HELP)
    print(LISTUSERS_HELP)
    print(UPLOAD_HELP)
    print(READ_HELP)
    print(WRITE_HELP)
    print(GRANT_HELP)
    print(USERDOCS_HELP)
    print(TOPLEAKED_HELP)
    print(TOPGRANTERS_HELP)
    print(HELP_HELP)
    print(EXIT_HELP)

#Auxiliary Functions
def assign_levels(level):
    if level == OFFICIAL:
        level = 1
    elif level == CONFIDENTIAL:
        level = 2
    elif level == SECRET:
        level = 3
    else:
        level = 4
    return level

def can_access(level1, level2):
    n_level1 = assign_levels(level1)
    n_level2 = assign_levels(level2)
    return n_level1 >= n_level2

def main():
    agency = Agency()
    #exemples
    """agency.creat_agent("A", OFFICIAL)
    agency.creat_agent("B", TOPSECRET)
    agency.creat_document("official.doc", "B", "official")
    agency.creat_document("top.doc", "B", "topsecret")
    agency.write_document("top.doc","B", "oi")"""
    #start program
    command = next_command()
    while command != EXIT:
        if command == REGISTER:
            register(agency)
        elif command == LISTUSERS:
            list_users(agency)
        elif command == UPLOAD:
            upload(agency)
        elif command == WRITE:
            write(agency)
        #falta daqui
        elif command == READ:
            read(agency)
        elif command == GRANT:
            grant(agency)
        elif command == USERDOCS:
            userdocs(agency)
        elif command == TOPLEAKED:
            topleaked(agency)
        elif command == TOPGRANTERS:
            topgranters(agency)
        #Ate aqui
        elif command == HELP:
            help_print()
        else:
            print(UNKNOWN_COMMAND)
        command = next_command()
    print(BYE)

main()