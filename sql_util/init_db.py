from sqlalchemy import create_engine
from sql_util.models import Base

# 初始化数据库模型
if __name__ == '__main__':
    sqlite_filepath = 'tel_bot.db'
    engine = create_engine(f"sqlite:///{sqlite_filepath}")
    Base.metadata.create_all(engine)
