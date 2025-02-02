from crypto_system import CryptoSystem

def main():
    print("Welcome to the Cryptography System!\n")

    # Ask user if they want to use an existing key or generate a new one
    choice = input("Do you want to (1) generate a new key or (2) use an existing key? Enter 1 or 2: ")

    if choice == '1':
        crypto = CryptoSystem()  # Generate a new random key
        print("New encryption key generated.")
    elif choice == '2':
        filename = input("Enter the filename where the key is stored: ")
        try:
            crypto = CryptoSystem()
            crypto.load_key(filename)
            print(f"Key loaded from {filename}.")
        except Exception as e:
            print(f"Error loading key: {e}")
            return
    else:
        print("Invalid choice. Exiting.")
        return

    while True:
        print("\n--- Menu ---")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Save the encryption key to a file")
        print("4. Load the encryption key from a file")
        print("5. Exit")

        option = input("Select an option: ")

        if option == "1":
            plaintext = input("Enter the message to encrypt: ")
            iv, encrypted_message = crypto.encrypt(plaintext)
            print(f"Encrypted message: {encrypted_message}")
            print(f"IV (initialization vector): {iv}")

        elif option == "2":
            iv = input("Enter the IV (initialization vector) of the message: ")
            ciphertext = input("Enter the encrypted message: ")
            try:
                decrypted_message = crypto.decrypt(iv, ciphertext)
                print(f"Decrypted message: {decrypted_message}")
            except Exception as e:
                print(f"Error decrypting message: {e}")

        elif option == "3":
            filename = input("Enter the filename to save the key: ")
            crypto.save_key(filename)
            print(f"Key saved to {filename}.")

        elif option == "4":
            filename = input("Enter the filename to load the key from: ")
            try:
                crypto.load_key(filename)
                print(f"Key loaded from {filename}.")
            except Exception as e:
                print(f"Error loading key: {e}")

        elif option == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
