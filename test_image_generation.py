import requests
import time

# Endpoint URL
url = "https://your-serverless-endpoint"

# Payload and headers (adjust based on your API requirements)
payload = {
    "model": "dreamshaper-lightning",
    "settings": {
        "steps": "recommended",
        # Add other necessary settings as required
    }
}
headers = {
    "Content-Type": "application/json",
    # Include any authentication headers if needed
}

def generate_image():
    response = requests.post(url, json=payload, headers=headers)
    return response

def main():
    iterations = 10
    total_time = 0

    for i in range(iterations):
        start_time = time.time()
        response = generate_image()
        end_time = time.time()

        time_taken = end_time - start_time
        total_time += time_taken

        print(f"Iteration {i+1}: Time taken = {time_taken:.2f} seconds")
        if response.status_code != 200:
            print(f"Error: {response.text}")

    average_time = total_time / iterations
    print(f"\nAverage time taken over {iterations} iterations = {average_time:.2f} seconds")

if __name__ == "__main__":
    main()