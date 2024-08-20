# docker run
                docker pull ollama/ollama:latest
                docker run -d -p 15000:11434 ollama/ollama

                docker exec -it {id container}> ollama pull mistral
                docker exec -it f455d69e6edcd67678b8924c44eebe1b936ec295a0ef2af7a2051abe7cb57e69 ollama pull mistral

# api usage

https://www.postman.com/bstraehle/workspace/generative-ai-llm-rest-apis/documentation/7643177-2ea8088c-43df-440a-b6de-4a84ac3fa60c

                curl --location 'http://127.0.0.:15000/api/generate' \
                --header 'Content-Type: application/json' \
                --data '{
                    "model": "mistral",
                    "prompt": "What is the meaning of life?",
                    "raw": true,
                    "stream": false
                }'

https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings

                curl http://localhost:11434/api/embed -d '{
                "model": "mistral",
                "input": "Why is the sky blue?"
                }'