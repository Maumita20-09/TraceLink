# 🔍 URL Redirect Checker (TraceLink)

A simple yet powerful cybersecurity tool that analyzes URL redirection chains to help detect suspicious or potentially malicious links.

---

## 🚀 Features

* 🔗 Displays full redirect chain
* 📡 Shows HTTP status codes (301, 302, 200, etc.)
* 🎯 Identifies final destination URL
* 🔢 Counts total number of redirects
* ⚠️ Flags suspicious links (more than 3 redirects)

---

## 🧠 Use Case

This tool is useful in:

* Phishing detection
* Malware analysis
* OSINT investigations
* Understanding URL shortening services
* Web security learning

---

## 🗂️ Project Structure

```
TraceLink/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/Maumita20-09/TraceLink.git
cd TraceLink
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python app.py
```

---

## 🌐 Usage

1. Open the app in your browser (Codespaces will provide a link or use `localhost:5000`)
2. Enter a URL (e.g., `http://example.com`)
3. Click **Check**
4. View:

   * Redirect chain
   * Status codes
   * Final destination
   * Warning (if redirects > 3)

---

## ⚠️ Example Output

```
bit.ly/abc → 302
short1.com → 302
short2.com → 302
finalsite.com → 302
landingpage.com → 200

⚠ Warning: This URL has more than 3 redirects and may be suspicious.
```

---

## 🛠️ Tech Stack

* Python
* Flask
* Requests
* HTML/CSS

---

## ⭐ License

This project is open-source and free to use for educational purposes.
