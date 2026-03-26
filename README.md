# MAG4 Uploader & Viewer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mag4datasharing-app-pb0ioldt9x.streamlit.app/)

**MAG4 Uploader & Viewer** is an open‑source platform for sharing and exploring geological datasets. It provides a simple web interface to upload, manage, and view data, with all files stored securely in a public GitHub repository.

---

## ✨ Features

- **ORCID Authentication** – Log in with your ORCID iD to ensure secure, attributed contributions.
- **File Upload** – Upload geological datasets (CSV, Excel, JSON, etc.) directly through the interface.
- **Data Preparation** – A dedicated *Prepare your file for upload* page helps you validate, anonymize, and format your data before submission.
- **View & Manage** – Browse and update previously uploaded datasets.
- **Public Repository** – All uploads are stored in a public GitHub repository, making them citable and accessible.
- **Open Source** – The entire platform is open source; contributions are welcome.

---

## 🚀 How to Use

1. **Visit the app**: [https://mag4datasharing-app-pb0ioldt9x.streamlit.app/](https://mag4datasharing-app-pb0ioldt9x.streamlit.app/)
2. **Log in** with your ORCID credentials.
3. **Prepare your file** (optional): Use the *Prepare your file for upload* page to clean and validate your data.
4. **Upload** your dataset – provide metadata and confirm the upload.
5. **View and manage** your datasets from the main dashboard.
6. **Log out** when finished.

---

## 🔐 Authentication

This app uses **ORCID** for authentication. When you click *Log in with ORCID*, you will be redirected to ORCID’s website to grant permissions. After successful login, you will be able to upload and manage datasets.

---

## 📂 Data Storage

All uploaded files are stored in a **public GitHub repository**. This ensures:
- Permanent, version‑controlled storage.
- DOI minting (via Zenodo or similar) for future citation.
- Transparency and open access to the data.

---

## 🛠️ Local Development

To run the app locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/mag4-uploader.git
   cd mag4-uploader
