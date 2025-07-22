import os
import glob
import re


class OptiChunker:
    def __init__(self, markdown_dir, chunks_dir):
        self.markdown_dir = markdown_dir
        self.chunks_dir = chunks_dir
        os.makedirs(self.chunks_dir, exist_ok=True)

    def slugify(self, text):
        return re.sub(r"[^a-zA-Z0-9-]+", "-", text.lower()).strip("-")
    def split_by_heading(self, md_text):
        # Split at headings (## or ### and above, but not # which is usually the article title)
        # Capture the heading itself as part of the chunk.
        matches = list(re.finditer(r'^(#{2,})\s+.+', md_text, flags=re.MULTILINE))
        if not matches:
            return [md_text.strip()]  # fallback: one chunk (no headings found)

        chunks = []
        for i, match in enumerate(matches):
            start = match.start()
            end = matches[i+1].start() if i+1 < len(matches) else len(md_text)
            chunk = md_text[start:end].strip()
            if chunk:
                chunks.append(chunk)
        return chunks

    def chunk_markdown_files(self):
        md_files = glob.glob(os.path.join(self.markdown_dir, "*.md"))
        total_chunks = 0
        for md_path in md_files:
            with open(md_path, "r", encoding="utf-8") as f:
                md_text = f.read()
            base_slug = self.slugify(os.path.splitext(os.path.basename(md_path))[0])
            chunks = self.split_by_heading(md_text)
            if len(chunks) == 1 and "##" not in md_text:
                print(
                    f"{os.path.basename(md_path)}: No headings found, fallback to single chunk."
                )
            for idx, chunk in enumerate(chunks):
                chunk_filename = f"{base_slug}_chunk{idx+1}.md"
                chunk_path = os.path.join(self.chunks_dir, chunk_filename)
                with open(chunk_path, "w", encoding="utf-8") as cf:
                    cf.write(chunk)
            print(f"{os.path.basename(md_path)}: {len(chunks)} section chunks written.")
            total_chunks += len(chunks)
        print(f"\nDone! Total section chunks created: {total_chunks}")
        return total_chunks  # <-- Return count for accurate logging


    def chunk_markdown_file(self, md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            md_text = f.read()
        base_slug = self.slugify(os.path.splitext(os.path.basename(md_path))[0])
        chunks = self.split_by_heading(md_text)
        for idx, chunk in enumerate(chunks):
            chunk_filename = f"{base_slug}_chunk{idx+1}.md"
            chunk_path = os.path.join(self.chunks_dir, chunk_filename)
            with open(chunk_path, "w", encoding="utf-8") as cf:
                cf.write(chunk)
        print(f"{os.path.basename(md_path)}: {len(chunks)} section chunks written.")
        return len(chunks)

    def chunk_selected_files(self, filenames):
        count = 0
        for fname in filenames:
            md_path = os.path.join(self.markdown_dir, fname)
            if not os.path.exists(md_path):
                continue
            with open(md_path, "r", encoding="utf-8") as f:
                md_text = f.read()
            base_slug = self.slugify(os.path.splitext(os.path.basename(md_path))[0])
            chunks = self.split_by_heading(md_text)
            for idx, chunk in enumerate(chunks):
                chunk_filename = f"{base_slug}_chunk{idx+1}.md"
                chunk_path = os.path.join(self.chunks_dir, chunk_filename)
                with open(chunk_path, "w", encoding="utf-8") as cf:
                    cf.write(chunk)
                count += 1
            print(f"{os.path.basename(md_path)}: {len(chunks)} section chunks written.")
        print(f"\nDone! Total section chunks created: {count}")
        return count
