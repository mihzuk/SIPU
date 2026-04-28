from backend.core.bootstrap import bootstrap_database


if __name__ == "__main__":
    bootstrap_database()
    print("Base de datos lista.")
    print("Inicia el servidor con: uvicorn backend.main:app --reload")
