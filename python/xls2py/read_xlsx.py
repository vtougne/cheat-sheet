import pandas as pd
import json

def read_xlsx_to_json(file_path):
    try:
        df = pd.read_excel(file_path)
        data = df.to_dict('records')
        return json.dumps(data, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Erreur lors de la lecture du fichier: {e}"

if __name__ == "__main__":
    file_path = "sample.xlsx"
    json_content = read_xlsx_to_json(file_path)
    print(json_content)