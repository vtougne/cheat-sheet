#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import httpx
import argparse
import sys

API_URL = "http://172.28.240.1:11434/api/chat"

def stream_response(question: str) -> str:
    """
    Envoie la requête POST en mode streaming à Ollama
    et concatène les fragments de texte jusqu’à ce que le champ
    "done" soit True.
    """
    payload = {
        "model": "gpt-oss:20b",
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    headers = {"Content-Type": "application/json"}

    with httpx.stream("POST", API_URL, headers=headers, json=payload) as resp:
        resp.raise_for_status()

        full_text = ""

        for line_raw in resp.iter_lines():
            if not line_raw:
                continue

            # httpx peut renvoyer bytes ou str
            line = (
                line_raw.decode("utf-8")
                if isinstance(line_raw, bytes)
                else line_raw
            )

            # Supprimer le préfixe SSE éventuel
            if line.startswith("data: "):
                line = line[6:]

            # Ignorer les lignes spéciales
            if not line.strip() or line.strip() == "data: [DONE]":
                continue

            try:
                chunk = json.loads(line)
            except json.JSONDecodeError:
                # Ligne non‑JSON, on l’ignore silencieusement
                continue

            fragment = chunk.get("message", {}).get("content", "")
            full_text += fragment

            if chunk.get("done"):
                break

        return full_text

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Chat avec un modèle Ollama en streaming."
    )
    parser.add_argument(
        "question",
        nargs="+",
        help="La question (ou phrase) à poser au modèle."
    )
    args = parser.parse_args()

    # On regroupe les morceaux pour former la phrase complète
    question = " ".join(args.question)

    print("📝 Question envoyée :", question)
    answer = stream_response(question)
    print("\n🗨️ Réponse du modèle :")
    print(answer)

if __name__ == "__main__":
    # Si aucune question n’est fournie, afficher l’aide
    if len(sys.argv) == 1:
        sys.argv.append("--help")
    main()
