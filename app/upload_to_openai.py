import os
import glob
from dotenv import load_dotenv
import openai


class OptiUploader:
    def __init__(self, chunks_dir):
        load_dotenv()
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.OPENAI_API_KEY
        self.chunks_dir = chunks_dir

    def upload_files(self):

        # Uploads each chunk file to OpenAI File API for use with Assistants.
        # Returns a list of OpenAI file IDs.

        file_ids = []
        chunk_files = glob.glob(os.path.join(self.chunks_dir, "*.md"))
        print(f"Uploading {len(chunk_files)} chunk files from {self.chunks_dir}...")

        for file_path in chunk_files:
            with open(file_path, "rb") as f:
                response = openai.files.create(file=f, purpose="assistants")
                file_id = response.id
                file_ids.append(file_id)
                print(f"Uploaded {os.path.basename(file_path)}: {file_id}")
        print(f"Uploaded {len(file_ids)} files to OpenAI.")
        return file_ids

    def create_vector_store(self, name="Optisigns Help Articles Vector Store"):
        # Creates a new OpenAI vector store and returns its ID.

        vector_store = openai.vector_stores.create(name=name)
        vector_store_id = vector_store.id
        print(f"Created vector store: {vector_store_id}")
        return vector_store_id

    def attach_files_to_vector_store(self, file_ids, vector_store_id):
        # Attaches each uploaded file to the specified vector store.

        print(f"Attaching {len(file_ids)} files to vector store {vector_store_id}...")
        for file_id in file_ids:
            openai.vector_stores.files.create(
                vector_store_id=vector_store_id, file_id=file_id
            )
            print(f"Attached file {file_id} to vector store.")
        print("All files attached.")

    def upload_and_attach(self):
        # Setup: upload files -> create vector store -> attach files.

        file_ids = self.upload_files()
        vector_store_id = self.create_vector_store()
        self.attach_files_to_vector_store(file_ids, vector_store_id)
        print(
            f"All {len(file_ids)} chunk files uploaded and attached to vector store {vector_store_id}."
        )
        print("Vector store setup complete.")

    def delete_all_openai_files(self):    
        # Deletes all files from the OpenAI account.

        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        files = openai.files.list().data
        if not files:
            print("No files to delete.")
            return
        print(f"Deleting {len(files)} files from OpenAI account...")
        for file in files:
            try:
                openai.files.delete(file.id)
                print(f"Deleted file: {file.id} ({file.filename})")
            except Exception as e:
                print(f"Failed to delete file {file.id}: {e}")
        print("All files deleted.")
