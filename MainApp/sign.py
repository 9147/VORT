import binascii
import hashlib

# Function to calculate the hash of a file and store it
def store_file_hash(file_path, hash_output_file):
    # Calculate the hash of the file
    with open(file_path, 'rb') as file:
        file_content = file.read()
        file_hash = binascii.hexlify(hashlib.sha256(file_content).digest()).decode('utf-8')

    # Write the hash to a file
    with open(hash_output_file, 'w') as hash_file:
        hash_file.write(file_hash)

    print("Hash of the PDF file stored in", hash_output_file)

def calculate_file_hash(file):
    sha256 = hashlib.sha256()
    for chunk in file.chunks():
        sha256.update(chunk)
    return binascii.hexlify(sha256.digest()).decode('utf-8')

# Function to verify the integrity of a PDF file using stored hash
def verify_pdf_integrity(pdf_path, stored_hash_file):
    # Read the stored hash from the file
    with open(stored_hash_file, 'r') as hash_file:
        stored_hash = hash_file.read()

    # Calculate the hash of the current PDF file
    recalculated_hash = hashlib.sha256(open(pdf_path, 'rb').read()).hexdigest()

    # Compare the stored hash with the recalculated hash
    if recalculated_hash == stored_hash:
        print("PDF integrity verified. Not altered.")
        return True
    else:
        print("PDF integrity compromised. Altered.")
        return False

# Example usage:
if __name__ == "__main__":
    event='sample_event'
    # Path to the PDF file
    pdf_file_path = "SLP3.pdf"
    pdf_file_path2 = "SLP.pdf"

    # Path to store the hash value
    stored_hash_file = "stored_hash.txt"

    # Store the hash of the PDF file
    store_file_hash(pdf_file_path, stored_hash_file)

    # Verify the integrity of the PDF file using the stored hash
    verification_result = verify_pdf_integrity(pdf_file_path2, stored_hash_file)
