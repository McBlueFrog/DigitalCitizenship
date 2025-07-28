from eth_account import Account
from eth_account.messages import encode_defunct

def verify_signature(address, signature, message):
    message_encoded = encode_defunct(text=message)
    recovered_address = Account.recover_message(message_encoded, signature=signature)
    return recovered_address.lower() == address.lower()

if __name__ == "__main__":
    # Replace these with outputs from wallet_sign.py
    address = "0xaddress"
    message = "message_to_sign"
    signature = "0xsignature"

    is_valid = verify_signature(address, signature, message)
    if is_valid:
        print("✅ Wallet verified! User is authentic.")
    else:
        print("❌ Verification failed! User is NOT authentic.")
