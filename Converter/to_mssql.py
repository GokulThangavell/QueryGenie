import ollama

class mssql_helper:
    def to_sql(question:str, schema:str) -> str:
        prompt =f"""
        You are an expert in MSSQL
        User question: "{question}"
        Database schema: "{schema}"
        Write an MSSQL query  (T-SQL) that answers the question.
        Do not add explanations, only return the sql query.
        """
        response = ollama.chat(model="mistral", messages=[{"role":"user", "content":prompt}])
        return response["message"]["content"]

