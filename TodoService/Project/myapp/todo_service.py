# Function to fetch the public key from AuthService
import requests
from django.core.exceptions import PermissionDenied
from cryptography.hazmat.primitives import serialization

def fetch_public_key():
    try:
        response = requests.get("http://127.0.0.1:8000/auth/public-key", timeout=5)
        response.raise_for_status()  # Raises an error for non-2xx responses
        public_key_pem = response.json()["public_key"]
        public_key = serialization.load_pem_public_key(public_key_pem.encode())
        return public_key
    except requests.RequestException as e:
        raise PermissionDenied('Error fetching public key from AuthService') from e
    except KeyError:
        raise PermissionDenied('Invalid response format from AuthService')
    except Exception as e:
        raise PermissionDenied(f"Public key parsing error: {str(e)}")
