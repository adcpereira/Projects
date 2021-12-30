from Agency import Agency
# Commands
REGISTER     = "register"
LISTUSERS    = "listusers"
UPLOAD       = "upload"
READ         = "read"
WRITE        = "write"
READ         = "read"
GRANT        = "grant"
USERDOCS     = "userdocs"
TOPLEAKED    = "topleaked"
TOPGRANTERS  = "topgranters"
HELP         = "help"
EXIT         = "exit"

# Levels
OFFICIAL     = "official"
CONFIDENTIAL = "confidential"
SECRET       = "secret"
TOPSECRET    = "topsecret"

# Print Statments
NO_USERS                = "There are no registered users."
UNKNOWN_COMMAND         = "Unknown command. Type help to see available commands."
USER_ALREADY_REGISTERED = "Identifier {} is already assigned to another user."
USER_REGISTER           = "User {} was registered."
NOT_REGISTERED_USER     = "Not a registered user."
DOC_ALREADY             = "Document {} already exists in the user account."
INSUFFICIENCENT_LEVEL   = "Insufficient security clearance."
DOC_UPLOADED            = "Document {} was uploaded."
DOC_NOT_EXIST_USER      = "Document {} does not exist in the user account."
DOC_UPDATED             = "Document {} was updated."
DOCUMENT                = "Document:"
ALREADY_ACCESS          = "Already has access to document {}."
GRANT_ACCESS            = "Access to document {} has been granted."
NO_DOCS                 = "There are no documents."
NO_GRANTS               = "There are no grants."
NO_ACCESSES             = "There are no accesses."
NO_LEAKED               = "There are no leaked documents."
NO_U_GRANTS             = "No user has given grants."
BYE                     = "Bye!"


# Print Statements for HELP
REGISTER_HELP           = "register - registers a new user"
LISTUSERS_HELP          = "listusers - list all registered users"
UPLOAD_HELP             = "upload - upload a document"
READ_HELP               = "read - read a document"
WRITE_HELP              = "write - write a document"
GRANT_HELP              = "grant - grant access to a document"
USERDOCS_HELP           = "userdocs - list the documents of an user"
TOPLEAKED_HELP          = "topleaked - list the top 10 documents with more grants"
TOPGRANTERS_HELP        = "topgranters - list the top 10 users that have given more grants"
HELP_HELP               = "help - shows the available commands"
EXIT_HELP               = "exit - terminates the execution of the program"

#DICT_CONST
LIST_HELP               = [REGISTER_HELP, LISTUSERS_HELP, UPLOAD_HELP, READ_HELP, WRITE_HELP, GRANT_HELP,
                           USERDOCS_HELP, TOPLEAKED_HELP, TOPGRANTERS_HELP, HELP_HELP, EXIT_HELP]
DICT_LEVELS             = {OFFICIAL : 1, CONFIDENTIAL : 2, SECRET : 3, TOPSECRET : 4}

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
    list_agents = sorted(agency.list_ids(), key = str.casefold)
    if len(agency.list_ids()) == 0:
        print(NO_USERS)
    for agent in list_agents:
        print(agent, agency.level_by_id(agent))

def upload(agency):
    doc_name = input()
    id = input()
    d_level = input()
    desc = input()
    if id not in agency.list_ids():
        print(NOT_REGISTERED_USER)
    elif doc_name in agency.names_docs_by_id(id):
        print(DOC_ALREADY.format(doc_name))
    elif not can_access(agency.level_by_id(id), d_level):
        print(INSUFFICIENCENT_LEVEL)
    else:
        agency.creat_document(doc_name, id, d_level, desc)
        print(DOC_UPLOADED.format(doc_name))

def write(agency):
    doc_name = input()
    id_upload = input()
    id_write = input()
    desc = input()
    if not ids_exist(agency, id_upload, id_write):
        print(NOT_REGISTERED_USER)
    elif not doc_exists_id(agency, doc_name, id_upload):
        print(DOC_NOT_EXIST_USER.format(doc_name))
    elif not can_access(agency.level_by_id(id_write), agency.level_by_doc(doc_name, id_upload)):
        print(INSUFFICIENCENT_LEVEL)
    else:
        agency.write_document(doc_name, id_write, id_upload, desc)
        print(DOC_UPDATED.format(doc_name))

def read(agency):
    doc_name = input()
    id_upload = input()
    id_read = input()
    if not ids_exist(agency, id_upload, id_read):
        print(NOT_REGISTERED_USER)
    elif not doc_exists_id(agency, doc_name, id_upload):
        print(DOC_NOT_EXIST_USER.format(doc_name))
    elif not can_access(agency.level_by_id(id_read), agency.level_by_doc(doc_name, id_upload))\
            and id_read not in agency.grants_by_doc(doc_name, id_upload):
        print(INSUFFICIENCENT_LEVEL)
    else:
        print(DOCUMENT, agency.read_doc(doc_name, id_read, id_upload))  # depois dividir a funcao

def grant(agency):
    doc_name = input()
    id_upload = input()
    id_grant = input()
    if not ids_exist(agency, id_upload, id_grant):
        print(NOT_REGISTERED_USER)
    elif not doc_exists_id(agency, doc_name, id_upload):
        print(DOC_NOT_EXIST_USER.format(doc_name))
    elif can_access(agency.level_by_id(id_grant), agency.level_by_doc(doc_name, id_upload))\
            or id_grant in agency.grants_by_doc(doc_name, id_upload):
        print(ALREADY_ACCESS.format(doc_name))
    else:
        agency.grant(doc_name, id_grant, id_upload)
        print(GRANT_ACCESS.format(doc_name))

def userdocs(agency):
    id_person = input()
    if id_person not in agency.list_ids():
        print(NOT_REGISTERED_USER)
    elif len(agency.docs_by_id(id_person)) == 0:
        print(NO_DOCS)
    else:
        for doc in sort_user_docs(agency, id_person):  # foreach document that the user as make an upload
            list_a_doc = agency.accesses_by_doc(doc, id_person)  # dicionário de acessos
            print(doc, agency.level_by_doc(doc, id_person), len(list_a_doc), len(agency.grants_by_doc(doc, id_person)))
            if len(agency.accesses_by_doc(doc, id_person)) == 0:
                print(NO_ACCESSES)
            else:
                i = 0
                for id, action in list_a_doc: #[(id, action), (id, action)]
                    if i == 0:
                        text_new = "{} [{}]".format(id, action)
                    else:
                        text_new += ", {} [{}]".format(id, action)
                    i += 1
                print(text_new)
            if len(agency.grants_by_doc(doc, id_person)) == 0:
                print(NO_GRANTS)
            else:
                list_grants = agency.grants_by_doc(doc, id_person)
                q = 0
                for id in list_grants: #["C", "A", "D"]
                    if q == 0:
                        text_new = "{}".format(id)
                    else:
                        text_new += ", {}".format(id)
                    q += 1
                print(text_new)

def topleaked(agency):
    list_docs = agency.list_docs()
    grants_docs = {}
    for doc_name in list_docs:
        grants_docs[doc_name] = len(agency.grants_by_doc(process_name(doc_name)[0], process_name(doc_name)[1]))
    if len(list_docs) == 0:
        print(NO_LEAKED)
    elif max(list(grants_docs.values())) == 0:
        print(NO_LEAKED)
    else:
        list_sorted = sorted(list(grants_docs.items()), key = lambda a : a[0])
        list_sorted = sorted(list_sorted, key = lambda tuple : tuple[1], reverse = True)
        for tuple in list_sorted[: 10]:
            doc_name = process_name(tuple[0])[0]
            manager = process_name(tuple[0])[1]
            n_ac = len(agency.accesses_by_doc(doc_name, manager))
            if tuple[1] == 0:
                break
            print(doc_name, manager, agency.level_by_doc(doc_name, manager), n_ac, tuple[1])

def topgranters(agency):
    grants_docs = []
    for id in agency.list_ids():
        soma = 0
        for doc_name in agency.names_docs_by_id(id):
            soma += len(agency.grants_by_doc(doc_name, id))
        grants_docs.append((id, soma))
    if len(grants_docs) == 0:
        print(NO_U_GRANTS)
    else:
        grants_docs.sort(key = lambda a : a[0])
        grants_docs.sort(key = lambda a : a[1], reverse = True)
        for tuplo in grants_docs[: 10]:
            id_level = agency.level_by_id(tuplo[0])
            n_docs = len(agency.names_docs_by_id(tuplo[0]))
            if tuplo[1] == 0:
                break
            print(tuplo[0], id_level, n_docs, tuplo[1])

def help_print():
    for string in LIST_HELP:
        print(string)

# Auxiliary Functions
def can_access(level1, level2):
    return DICT_LEVELS[level1] >= DICT_LEVELS[level2]

def ids_exist(agency, id1, id2):
    return (id1 in agency.list_ids() and id2 in agency.list_ids())

def doc_exists(agency, doc_name):
    return doc_name in agency.names_docs_by_id()

def doc_exists_id(agency, doc_name, id):
    return doc_name in agency.names_docs_by_id(id)

def sort_user_docs(agency, id):
    list_docs = agency.docs_by_id(id)
    list_docs = sorted(list_docs, key = str.casefold)
    list_final = sorted(list_docs, key = lambda doc : DICT_LEVELS[agency.level_by_doc(doc, id)], reverse = True)
    return list_final

def process_name(name):
    list_name = list(name)
    list_name.reverse()
    n = list_name.index("_")
    return name[: len(list_name) - n - 1], name[len(list_name) - n:]

def main():
    agency = Agency()
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
        elif command == HELP:
            help_print()
        else:
            print(UNKNOWN_COMMAND)
        command = next_command()
    print(BYE)

main()

