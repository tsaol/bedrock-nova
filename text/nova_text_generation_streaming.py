import boto3
import json

client = boto3.client("bedrock-runtime")

system = [{ "text": "You are a helpful assistant" }]

messages = [
    {"role": "user", "content": [{"text": "Write a short story about lucky dogs"}]},
]

inf_params = {"maxTokens": 300, "topP": 0.1, "temperature": 0.3}

additionalModelRequestFields = {
    "inferenceConfig": {
         "topK": 20
    }
}

# converse_stream API
stream_response = client.converse_stream(
    modelId="us.amazon.nova-lite-v1:0", 
    messages=messages, 
    system=system, 
    inferenceConfig=inf_params,
    additionalModelRequestFields=additionalModelRequestFields
)


print("\n[Streaming Response]")
for event in stream_response:
    if "chunk" in event:
        chunk = json.loads(event["chunk"]["bytes"].decode())
        if "output" in chunk and "message" in chunk["output"]:
            content = chunk["output"]["message"]["content"]
            if content and len(content) > 0 and "text" in content[0]:
                print(content[0]["text"], end="", flush=True)

print("\nStreaming completed.")
