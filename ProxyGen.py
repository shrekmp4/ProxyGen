import requests

def get_proxies(api_url, num_proxies=5):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            proxies = response.json()[:num_proxies]
            return proxies
        else:
            print(f"Error al obtener proxies. Código de estado: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    api_url = "https://www.proxy-list.download/api/v1/get?type=https"
    num_proxies = 5

    proxies = get_proxies(api_url, num_proxies)

    if proxies:
        print("Proxies obtenidos:")
        for proxy in proxies:
            print(proxy)
    else:
        print("No se pudieron obtener proxies.")
