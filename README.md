# Gene Regulatory Element Scanner – Promoter Detection

A Streamlit web app that accepts a DNA sequence, validates it, searches for selected promoter-related motifs (TATA Box, CAAT Box, and a simplified GC marker), reports sequence length and GC content, and allows results to be downloaded as CSV.

## Run locally
1. Install Python 3.9 or newer.
2. Open Terminal in this project folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the website locally:
   ```bash
   streamlit run app.py
   ```
5. Streamlit will print a local address (usually `http://localhost:8501`). Open it in your browser.

## Deploy online using GitHub + Streamlit Community Cloud
1. Create a GitHub repository and upload all four project files (`app.py`, `promoter_scanner.py`, `requirements.txt`, `test_promoter_scanner.py`) and this README.
2. Go to Streamlit Community Cloud and sign in with GitHub.
3. Choose **Create app**, select your repository, branch (`main`), and main file path (`app.py`).
4. Click **Deploy**. Once deployment finishes, Streamlit will provide a public website URL.

## Run tests
```bash
python -m unittest test_promoter_scanner.py
```

## Limitations
This project searches exact patterns. The simplified `GC` marker is not a complete biological GC-box consensus. Detecting a motif does not by itself confirm promoter activity.
