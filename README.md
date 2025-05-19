# 📰 Al Jazeera Web Crawler

This project crawls and extracts public content from [Al Jazeera](https://www.aljazeera.com), following ethical guidelines and site policies.

## 📦 Files

- `IR.ipynb`: Jupyter notebook with crawling and extraction code.
- `Documentation.docx`: Analysis of `robots.txt`, sitemaps, RSS feeds, and findings.

## 🛠️ Setup

```bash
pip install requests beautifulsoup4 pandas selenium playwright
playwright install
```

## ✅ Features

- Respects `robots.txt` and avoids disallowed paths.
- Uses a 2-second delay between requests.
- Extracts titles, dates, authors, and article text.
- Supports static and JavaScript-rendered content (via Selenium/Playwright).
- Uses sitemaps and RSS feeds for discovery.
- No API endpoints or disallowed paths accessed.

## 🔍 Findings

- Page titles follow:  
  `"Section | Today's latest from Al Jazeera"`
- >50 articles extracted.
- RSS feeds are reliable and recommended.

playwright install
## 🚀 How to Run

Open IR.ipynb in Jupyter.
Step through each cell to:
Parse and analyze robots.txt
Crawl static or dynamic content pages
Extract and display structured data
Results are printed and optionally saved to CSV.
