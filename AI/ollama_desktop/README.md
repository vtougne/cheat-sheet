



```
api_ip=172.17.112.1
api_ip=172.28.240.1
```

```bash
curl -X POST http://$api_ip:11434/api/generate -H "Content-Type: application/json" -d '{
  "model": "gpt-oss:20b",
  "prompt": "Ollama is 22 years old and is busy saving the world. Respond using JSON",
  "stream": false,
  "format": {
    "type": "object",
    "properties": {
      "age": {
        "type": "integer"
      },
      "available": {
        "type": "boolean"
      }
    },
    "required": [
      "age",
      "available"
    ]
  }
}'
```

```bash
curl http://$api_ip:11434/api/generate -d '{
  "model": "gpt-oss:20b",
  "prompt": "What color is the sky at different times of the day? Respond using JSON",
  "format": "json",
  "stream": false
}'
```

```bash
curl http://$api_ip:11434/api/generate -d '{
  "model": "gpt-oss:20b",
  "prompt": "Why is the sky blue?"
}'>response_2.json
```

```bash
curl -X POST -H "Content-Type: application/json" -d '{"model":"gpt-oss:20b","messages":[{"role":"user","content":"Bonjour, comment ça va?"}]}' http://$api_ip:11434/api/chat
```


```bash
curl -N -X POST \
     -H "Content-Type: application/json" \
     -d '{"model":"gpt-oss:20b","messages":[{"role":"user","content":"Bonjour, comment ça va?"}]}' \
     http://$api_ip:11434/api/chat
```
