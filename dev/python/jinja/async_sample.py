#!/usr/bin/env python3

import asyncio
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Définir une fonction asynchrone pour simuler des données async
async def fetch_data(item):
    print(item)
    await asyncio.sleep(5)
    print(f"item {item} done")
    
    return f"Data for {item}"

# Configuration de l'environnement Jinja2 avec support async
env = Environment(
    loader=FileSystemLoader('templates'),  # Assurez-vous que le chemin est correct
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=True  # Activer le support async
)

async def render_template():
    try:
        template = env.get_template('async_template.html')
        title = "Async Rendering Example"
        
        # Simuler des appels async et attendre leur résolution
        items = await asyncio.gather(*(fetch_data(i) for i in range(5)))
        
        rendered_template = await template.render_async(title=title, items=items)
        print(rendered_template)
    except Exception as e:
        print(f"An error occurred: {e}")

# Exécuter la fonction async
asyncio.run(render_template())
