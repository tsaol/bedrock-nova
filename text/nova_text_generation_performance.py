import boto3
import json
from datetime import datetime

def test_nova_speed():
    # Create a Bedrock Runtime client
    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    
    LITE_MODEL_ID = "amazon.nova-lite-v1:0"
    
    # System and message setup
    system_list = [{"text": "Act as a assistant."}]
    message_list = [{"role": "user", "content": [{"text": "hello, tell me a long story about china"}]}]
    
    # Inference parameters
    inf_params = {
        "max_new_tokens": 2000,  
        "top_p": 0.9,
        "top_k": 20,
        "temperature": 0.5
    }
    
    request_body = {
        "schemaVersion": "messages-v1",
        "messages": message_list,
        "system": system_list,
        "inferenceConfig": inf_params,
    }
    
    # Start timing
    start_time = datetime.now()
    time_to_first_token = None
    token_count = 0
    generated_text = ""
    
    # Call the model
    response = client.invoke_model_with_response_stream(
        modelId=LITE_MODEL_ID,
        body=json.dumps(request_body)
    )
    
    print("Starting generation...")
    
    # Process response stream
    stream = response.get("body")
    if stream:
        for event in stream:
            chunk = event.get("chunk")
            if chunk:
                chunk_json = json.loads(chunk.get("bytes").decode())
                content_block_delta = chunk_json.get("contentBlockDelta")
                
                if content_block_delta:
                    if time_to_first_token is None:
                        time_to_first_token = datetime.now() - start_time
                        print(f"\nFirst token latency: {time_to_first_token}")
                    
                    text = content_block_delta.get("delta").get("text")
                    generated_text += text
                    token_count += 1
                    print(text, end="")
        
        # Calculate performance metrics
        total_time = (datetime.now() - start_time).total_seconds()
        tokens_per_second = token_count / total_time
        
        print("\n\nPerformance Statistics:")
        print(f"Total tokens: {token_count}")
        print(f"Total time: {total_time:.2f} seconds")
        print(f"Average tokens per second: {tokens_per_second:.2f}")
        print(f"First token latency: {time_to_first_token}")
    else:
        print("No response stream received")

if __name__ == "__main__":
    test_nova_speed()
