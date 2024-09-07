import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def generate_and_save_keys(private_key_path, public_key_path):
    # Generate RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Save the private key to a PEM file
    with open(private_key_path, "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    # Generate RSA public key
    public_key = private_key.public_key()

    # Save the public key to a PEM file
    with open(public_key_path, "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print(f"Private key saved to {private_key_path}")
    print(f"Public key saved to {public_key_path}")


if __name__ == "__main__":
    # Ensure the 'keys' directory exists
    os.makedirs("../keys", exist_ok=True)

    # Define file paths to save keys in the 'keys/' directory
    private_key_file = "./keys/private_key.pem"
    public_key_file = "./keys/public_key.pem"

    # Generate and save the keys
    generate_and_save_keys(private_key_file, public_key_file)
