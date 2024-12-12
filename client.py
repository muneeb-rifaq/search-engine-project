import socket
import threading

# Server configuration
SERVERS = [('127.0.0.1', 12345)]  # List of servers (IP, Port)
FILE_NAME = 'downloaded_file.txt'  # Name of the recombined file
CHUNK_SIZE = 1024 * 1024  # 1 MB per chunk
NUM_CHUNKS = 10  # Total number of chunks expected (Update based on actual file size)

# Shared dictionary to store downloaded chunks
downloaded_chunks = {}

def download_chunk(server, chunk_index):
    host, port = server
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))  # Connect to the server
            s.sendall(str(chunk_index).encode())  # Send the requested chunk index
            chunk_data = b''
            while True:
                data = s.recv(4096)  # Receive chunk data in parts (buffer size 4 KB)
                if not data:
                    break
                chunk_data += data

            # Save the chunk in the shared dictionary
            downloaded_chunks[chunk_index] = chunk_data
            print(f"Chunk {chunk_index} downloaded from {server}")
    except Exception as e:
        print(f"Failed to download chunk {chunk_index} from {server}: {e}")

def recombine_file():
    with open(FILE_NAME, 'wb') as file:
        for chunk_index in range(NUM_CHUNKS):
            if chunk_index in downloaded_chunks:
                file.write(downloaded_chunks[chunk_index])  # Write the chunk to the final file
    print(f"File recombination complete: {FILE_NAME}")

def download_file():
    threads = []
    for chunk_index in range(NUM_CHUNKS):
        # Distribute chunks across servers
        server = SERVERS[chunk_index % len(SERVERS)]  # Alternate servers for load balancing
        t = threading.Thread(target=download_chunk, args=(server, chunk_index))  # Thread for each chunk
        threads.append(t)
        t.start()  # Start the thread

    for t in threads:
        t.join()  # Wait for all threads to complete

    # Verify if all chunks are downloaded
    if len(downloaded_chunks) == NUM_CHUNKS:
        recombine_file()
        print("Download complete and file successfully recombined.")
    else:
        print("Download incomplete. Missing chunks:", 
              [i for i in range(NUM_CHUNKS) if i not in downloaded_chunks])

if __name__ == '__main__':
    download_file()