from backend.engine import get_engine
from backend.model import Base

def init_db():
    # 1. Engine mit der Postgres-Konfiguration laden
    # Dies nutzt die Logik aus _routes.py
    engine = get_engine("local_postgres_config.json")
    
    print("Erstelle Tabellen in der Datenbank...")
    
    # 2. Alle Tabellen erstellen, die von Base erben
    # Dazu gehören Entity, Person, User und Todo
    Base.metadata.create_all(bind=engine)
    
    print("Tabellen erfolgreich abgeglichen/erstellt.")

if __name__ == "__main__":
    init_db()