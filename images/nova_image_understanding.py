# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import base64
import boto3
import json

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1",
)
# model id list
# https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html
# https://docs.aws.amazon.com/nova/latest/userguide/additional-resources.html
# mode id :us.amazon.nova-pro-v1:0

MODEL_ID = "us.amazon.nova-lite-v1:0"
# Open the image you'd like to use and encode it as a Base64 string.
with open("media/test1.png", "rb") as image_file:
    binary_data = image_file.read()
    base_64_encoded_data = base64.b64encode(binary_data)
    base64_string = base_64_encoded_data.decode("utf-8")
# Define your system prompt(s).
system_list = [    {
        "text": "You are an expert artist. When the user provides you with an image, provide 3 potential art titles"
    }
]
# Define a "user" message including both the image and a text prompt.
message_list = [
    {
        "role": "user",
        "content": [
            {
                "image": {
                    "format": "png",
                    "source": {"bytes": base64_string},
                }
            },
            {
                "text": "Provide art titles for this image."
            }
        ],
    }
]
# Configure the inference parameters.
inf_params = {"max_new_tokens": 300, "top_p": 0.1, "top_k": 20, "temperature": 0.3}

native_request = {
    "schemaVersion": "messages-v1",
    "messages": message_list,
    "system": system_list,
    "inferenceConfig": inf_params,
}
# Invoke the model and extract the response body.
response = client.invoke_model(modelId=MODEL_ID, body=json.dumps(native_request))
model_response = json.loads(response["body"].read())
# Pretty print the response JSON.
print("[Full Response]")
print(json.dumps(model_response, indent=2))
# Print the text content for easy readability.
content_text = model_response["output"]["message"]["content"][0]["text"]
print("\n[Response Content Text]")
print(content_text)