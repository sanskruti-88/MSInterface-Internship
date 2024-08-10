from PIL import Image

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            # Apply encryption by adding the key to each color channel
            encrypted_pixel = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )
            pixels[i, j] = encrypted_pixel

    image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            # Apply decryption by subtracting the key from each color channel
            decrypted_pixel = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )
            pixels[i, j] = decrypted_pixel

    image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    print("Image Encryption Tool")
    choice = input("Would you like to (e)ncrypt or (d)ecrypt an image? ").lower()
    image_path = input("Enter the path to the image: ")
    output_path = input("Enter the output image path: ")
    key = int(input("Enter the encryption/decryption key (integer): "))

    if choice == 'e':
        encrypt_image(image_path, output_path, key)
    elif choice == 'd':
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid choice! Please select 'e' for encryption or 'd' for decryption.")

if __name__ =="__main__":
    main()