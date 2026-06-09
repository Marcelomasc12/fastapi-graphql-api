from sqlalchemy import Column, Integer, String

from app.database import Base


class PostModel(Base):
    __tablename__ = "posts"
    #Definindo o modelo da tabela 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)