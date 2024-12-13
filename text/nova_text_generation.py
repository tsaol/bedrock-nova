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
# model id list
# https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html
# https://docs.aws.amazon.com/nova/latest/userguide/additional-resources.html
# mode id :us.amazon.nova-pro-v1:0

model_response = client.converse(
    modelId="us.amazon.nova-lite-v1:0", 
    messages=messages, 
    system=system, 
    inferenceConfig=inf_params,
    additionalModelRequestFields=additionalModelRequestFields
)

print("\n[Full Response]")
print(json.dumps(model_response, indent=2))

print("\n[Response Content Text]")
print(model_response["output"]["message"]["content"][0]["text"])