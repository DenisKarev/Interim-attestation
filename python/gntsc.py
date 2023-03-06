from controller.controller import controller
from gntsviews.commandline import commandline
from dbase.gnotesdb import gnotes_db
from controller.options import dbfilename

db = gnotes_db(dbfilename)
v = commandline()

contr = controller(v, db)

# print(type(db))
# print(type(v))
# print(type(contr))
# contr.db.get_status()
contr.run()