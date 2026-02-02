from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

excel_path = os.path.join(BASE_DIR, "Vector_Database.xlsx")
db_location = os.path.join(BASE_DIR, "chroma_langchain_db")

df = pd.read_excel(excel_path)

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

add_documents = not os.path.exists(db_location)

vector_store = Chroma(
    collection_name="Vaccine_Names",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        doc = Document(
            page_content=(
                f"Disease: {row['Disease_name']}. "
                f"Vaccine: {row['Vaccine_name']}. "
                f"Age group: {row['Age_name']} ({row['Age']}). "
                f"Dose: {row['Vaccine_dose']}. "
                f"Number of doses: {row['Number_of _doses']}. "
                f"Interval between doses: {row['Interval_between_doses']}. "
                f"Correct age for vaccination: {row['Correct_age_for_vaccination']}. "
                f"Site of injection: {row['Site_of_injection']}. "
                f"Route of administration: {row['Route_of_administration']}. "
                f"Special condition: {row['Special condition']}."
            ),
            metadata={
                "disease": str(row["Disease_name"]),
                "vaccine": str(row["Vaccine_name"]),
                "age_group": str(row["Age_name"]),
                "age_group_id": str(row["Age_group"]),
            },
            id=str(i),
        )
        documents.append(doc)
        ids.append(str(i))

    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
