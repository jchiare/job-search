from components.database.db import db
from components.jobs.db import Base

Base.metadata.create_all(db)
