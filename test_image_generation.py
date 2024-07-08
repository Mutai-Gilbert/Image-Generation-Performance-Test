import requests
import time
import json

# Endpoint URLs
init_url = ""
status_url = ""

# Payload and headers (adjust based on your API requirements)
payload = {
    # Add the necessary payload for your request
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer"
}

def generate_image():
    # Step 1: Initiate the request
    init_response = requests.post(init_url, json=payload, headers=headers)
    if init_response.status_code != 200:
        return None, f"Failed to initiate image generation: {init_response.text}"

    init_result = init_response.json()
    request_id = init_result.get("id")

    # Step 2: Poll the status until completed
    status = "IN_QUEUE"
    result = None
    while status in ["IN_QUEUE", "IN_PROGRESS", "PROCESSING"]:
        time.sleep(3)  # Wait for 3 seconds before next check
        status_response = requests.get(f"{status_url}{request_id}", headers=headers)
        if status_response.status_code != 200:
            return None, f"Failed to get status: {status_response.text}"

        result = status_response.json()
        status = result.get("status")

    if status == "COMPLETED":
        return result, None
    else:
        return None, f"Image generation failed: {result.get('message')}"

def main():
    iterations = 10
    total_time = 0

    for i in range(iterations):
        start_time = time.time()
        result, error = generate_image()
        end_time = time.time()

        time_taken = end_time - start_time
        total_time += time_taken

        print(f"Iteration {i+1}: Time taken = {time_taken:.2f} seconds")
        if error:
            print(f"Error: {error}")
        else:
            print(f"Result: {json.dumps(result, indent=2)}")

    average_time = total_time / iterations
    print(f"\nAverage time taken over {iterations} iterations = {average_time:.2f} seconds")

if __name__ == "__main__":
    main()
