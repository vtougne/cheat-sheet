#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Usage
-----

1️⃣  Question uniquement  
    $ python3 ollam_cli.py "Quelle est la capitale de la France ?"

2️⃣  Question + pièce jointe (tout ce qui arrive sur STDIN est écrit
    dans un fichier temporaire et transmis à l’API sous forme
    Base‑64)  
    $ cat mon_fichier.txt | python3 ollam_cli.py "Quel est son contenu ?"
"""

import argparse
import base64
import httpx
import json
import os
import sys
import tempfile
from typing import Optional

# ------------------------------------------------------------------
# 1️⃣  URL de l’endpoint Ollama (nom « elton »)
# ------------------------------------------------------------------
API_URL = "http://elton:11434/api/chat"
MODEL_NAME = "gpt-oss:20b"   # modèle par défaut (modifiable)

# ------------------------------------------------------------------
# 2️⃣  Envoi de la requête streaming
# ------------------------------------------------------------------
def stream_response(question: str, file_path: Optional[str] = None) -> str:
    """Envoie la requête POST en streaming à /api/chat."""

    # ----------------- Préparer le payload -----------------
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": question}],
    }

    # Si un fichier est présent, l'encoder en Base‑64
    if file_path:
        with open(file_path, "rb") as fp:
            encoded = base64.b64encode(fp.read()).decode("utf-8")
        payload["file"] = encoded   # clé attendue par Ollama

    headers = {"Content-Type": "application/json"}

    # ----------------- Envoyer en streaming -----------------
    with httpx.stream("POST", API_URL, headers=headers, json=payload) as resp:
        resp.raise_for_status()

        full_text = ""

        for line_raw in resp.iter_lines():
            if not line_raw:
                continue

            line = (
                line_raw.decode("utf-8")
                if isinstance(line_raw, bytes)
                else line_raw
            )

            # La plupart des réponses commencent par "data: "
            if line.startswith("data: "):
                line = line[6:]

            if not line.strip() or line.strip() == "data: [DONE]":
                continue

            try:
                chunk = json.loads(line)
            except json.JSONDecodeError:
                continue

            fragment = chunk.get("message", {}).get("content", "")
            full_text += fragment

            if chunk.get("done"):
                break

        return full_text

# ------------------------------------------------------------------
# 3️⃣  Lecture de la question + création d’un attachement
# ------------------------------------------------------------------
def read_question_and_attachment() -> tuple[str, Optional[str]]:
    """Retourne (question, file_path)"""
    file_path = None

    # STDIN → fichier temporaire
    if not sys.stdin.isatty():
        raw_data = sys.stdin.buffer.read()
        if raw_data:
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".tmp")
            tmp.write(raw_data)
            tmp.flush()
            tmp.close()
            file_path = tmp.name

    # Argument(s) → question
    parser = argparse.ArgumentParser(
        description="Chat avec Ollama via /api/chat (nom 'elton')."
    )
    parser.add_argument(
        "question",
        nargs="+",
        help="La question (ou phrase) à poser au modèle.",
    )
    args = parser.parse_args()

    question = " ".join(args.question).strip()
    return question, file_path

# ------------------------------------------------------------------
# 4️⃣  Point d’entrée
# ------------------------------------------------------------------
def main() -> None:
    question, file_path = read_question_and_attachment()

    if not question:
        print("\n✖️ Aucun texte de question fourni.")
        print("\nExemple :")
        print("  python3 ollam_cli.py \"Qui a inventé le Python ?\"")
        print("  cat mon_fichier.txt | python3 ollam_cli.py \"Quel est son contenu ?\"")
        sys.exit(1)

    print("📝 Question envoyée :", question)
    if file_path:
        print(
            "📎 Pièce jointe : {} ({} octets)".format(
                os.path.basename(file_path),
                os.path.getsize(file_path),
            )
        )

    answer = stream_response(question, file_path)
    print("\n🗨️ Réponse du modèle :")
    print(answer)

    # Nettoyage du fichier temporaire
    if file_path:
        try:
            os.remove(file_path)
        except OSError:
            pass


if __name__ == "__main__":
    main()
