from eth_account import Account
from eth_account.messages import encode_defunct
import os

def generate_wallet():
    acct = Account.create()
    return acct

def sign_message(private_key, message):
    message_encoded = encode_defunct(text=message)
    signed_message = Account.sign_message(message_encoded, private_key=private_key)
    return signed_message.signature.hex()

if __name__ == "__main__":
    # Generate wallet
    wallet = generate_wallet()
    print("Wallet Address:", wallet.address)
    print("Private Key:", wallet.key.hex())

    # Message to sign (challenge)
    challenge = "Login challenge nonce: " + os.urandom(16).hex()
    print("Challenge:", challenge)

    # Sign the challenge
    signature = sign_message(wallet.key, challenge)
    print("Signature:", signature)

    # Output info for verification
    print("\n--- To verify, use these values ---")
    print(f"address = '{wallet.address}'")
    print(f"message = '{challenge}'")
    print(f"signature = '{signature}'")
