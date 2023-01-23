from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 10248430
    API_HASH = "42396a6ff14a569b9d59931643897d0d"
    # the name to display in your alive message
    ALIVE_NAME = "rishabh"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://dnwkixld:q-SaQDtzYsYi4-ELb8-KCxoQSj0qZXQl@satao.db.elephantsql.com/dnwkixld"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOHABuxFYFvtQxxPrOkw8_J3CxnE00G0Byz9nbqsHRpcpzpxPHYJ3RJUeaz_LM0OB-f8Hp63n1fJyZ9OEVpfTCvwXOk69YDMrcHe96nr7nkvguRTgAoqxKyO5i9KvWUMXYW8nASkJY2SHheMChUc8_g9KJsJN55ZaqK-WwU9e-AMMAD-zGiZhd1QGLaTtB7N_mW-aAuHeWHIn4FHE-JQ39uEfovSCZiMN3SCjHR7r7tD4elCOBJLeGxk7Weu4FaHMc50S8ml1G3CpslK0wux408NxJvdKe5kJPdgvwP2a7LemyoiaeN0K_iUFKAZ2h4BW9SgP7mYsAmNxKPG4iuUNpRDO7O0"
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5897278567:AAHL9VS7qvfQ_OEDWxfvJjdlSdobIHUJIZY"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001804739290
    # command handler
    COMMAND_HAND_LER = "."
    VCMODE = "True"
    VC_SESSION = "your 2nd id telethon session" #note don't use maim account to vc player
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/rishabhanand2/tha_plugins"
    #don't edit this 
    THANOSABUSE = "False"#don't edit this else error in 
