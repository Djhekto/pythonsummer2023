from typing import Optional,List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
import datetime as dt
import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

import db as _db
import model as _md

def _add_table():
    return _db.Base.metadata.create_all(bind=_db.engine)