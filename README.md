# Email Risk Analyzer

## Overview

Email Risk Analyzer is a Python-based cybersecurity tool that scans email headers and body content to identify potential phishing attempts. It analyzes security headers such as SPF, DKIM, and Return-Path, detects suspicious links and urgent phishing keywords, calculates a phishing risk score, and generates an email security audit report.

## Features

- Parses email headers
  - Return-Path
  - Received
  - SPF
  - DKIM
- Detects suspicious links
- Identifies domain spoofing patterns
- Searches for phishing keywords
- Calculates a phishing risk score
- Classifies phishing likelihood
- Generates an Email Security Audit Report

## Technologies Used

- Python 3
- Regular Expressions (re)
- File Handling

## Project Structure

```
Email-Risk-Analyzer/
│── email_analyzer.py
│── sample_email.txt
│── Phishing_Analysis_Report.pdf
└── README.md
```

## How It Works

1. Reads a sample email.
2. Parses important email headers.
3. Checks SPF and DKIM status.
4. Extracts URLs from the email body.
5. Detects suspicious phishing keywords.
6. Calculates an overall phishing risk score.
7. Generates a security audit report.

## How to Run

Clone the repository and execute:

```bash
python email_analyzer.py
```

## Sample Output

```
SPF Check: Failed
DKIM: Missing
Return-Path Found

Links Found:
http://paypa1-login-security.com

Suspicious Keywords:
immediately
verify
suspended
locked

Risk Score: 100

Phishing Likelihood: High
```

## Report Generated

The program generates an email security audit report summarizing:

- Header analysis
- SPF/DKIM results
- Suspicious links
- Phishing indicators
- Overall risk score
- Final phishing likelihood

## Future Improvements

- Support `.eml` email files
- Detect URL shortening services
- WHOIS domain reputation lookup
- Machine learning-based phishing detection
- GUI interface for email analysis

## Author

**Rishabh Singh Tomar**
