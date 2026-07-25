import re

with open("sample_email.txt", "r") as file:
    email = file.read()

    risk = 0

if "SPF: Fail" in email:
    print("SPF Check: Failed")
    risk += 30

if "DKIM: None" in email:
    print("DKIM: Missing")
    risk += 20

if "Return-Path" in email:
    print("Return-Path Found")

    links = re.findall(r'https?://\S+', email)

print("\nLinks Found:")

for link in links:
    print(link)

    if "paypa1" in link:
        risk += 30

        keywords = [
    "urgent",
    "immediately",
    "verify",
    "suspended",
    "locked"
]

print("\nSuspicious Keywords:")

for word in keywords:
    if word.lower() in email.lower():
        print(word)
        risk += 5


        print("\nRisk Score:", risk)

if risk < 30:
    result = "Low"

elif risk < 60:
    result = "Medium"

else:
    result = "High"

print("Phishing Likelihood:", result)


report = f"""
Email Security Audit Report

SPF Check:
{"Failed" if "SPF: Fail" in email else "Passed"}

DKIM:
{"Missing" if "DKIM: None" in email else "Present"}

Links:
{links}

Risk Score:
{risk}

Likelihood:
{result}
"""

with open("Email_Report.txt","w") as file:
    file.write(report)
