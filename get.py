import requests

def fetch_url_content(url: str) -> None:
    try:
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        print("Response Body:")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_url = "http://212.132.64.73:4446/"
    fetch_url_content(target_url)