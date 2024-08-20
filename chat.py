import ollama
from ollama import Client, ResponseError

# Ensure the Ollama server is running at the correct host and port
client = Client(host="http://localhost:11500")

model_name = "llama3.1"  # Replace with the correct model name if different

# Check if the model is available; if not, pull it first
try:
    response = client.chat(
        model="llama3.1", 
        messages=[
            {'role': 'user', 'content': 'What movies are being displayed today?'},
        ]
    )
except ResponseError as e:
    print('Error:', e.error)
    if e.status_code == 404:  # Model not found
        print(f"Model {"llama3.1"} not found. Pulling the model...")
        ollama.pull("llama3.1")  # Download the model
        response = client.chat(
            model="llama3.1", 
            messages=[
                {'role': 'user', 'content': 'What movies are being displayed today?'},
            ]
        )
    else:
        raise

# Generating a response using the model
generate_response = ollama.generate(model=model_name, prompt='What movies are being displayed today?')
print(generate_response)

# Streaming the chat response
stream = ollama.chat(
    model="llama3.1",
    messages=[{'role': 'user', 'content': 'What movies are being displayed today?'}],
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
