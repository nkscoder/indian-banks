# 🇮🇳 Indian Banks – Logos & Structured Data

A **centralized, open-source repository** containing structured data and official **logos of Indian Banks**.  
Includes high-quality vector logos, symbols, and verified metadata for use in apps, websites, and fintech products.  

## 📌 Why this project?
Finding **reliable, verified bank logos and data** for all Indian banks is time-consuming.  
This repo makes it easy with a **single source of truth** that includes:  

- ✅ Official vector & PNG logos  
- ✅ Bank codes & IFSC prefixes  
- ✅ Website links & USSD balance check codes  
- ✅ Categorization by **Public Sector, Private Sector, Small Finance, Payments Banks**  

## 🚀 Current Status

- [ ] Vector Logos → In Progress  
- [ ] Data Structure Finalization → In Progress  
  - Bank Name  
  - Logo (Full + Symbol)  
  - Short Code / Slug  
  - IFSC Prefix  
  - Balance Check USSD Code  
  - Website  
  - Bank Type (Reference: [RBI Official List](https://www.rbi.org.in/scripts/banklinks.aspx))  
- [ ] Automated scraping of official websites → Planned  

## 🏦 Bank Slugs & Logos

| Bank Name                  | Slug   | Logo                                                    | Symbol                                                    |
| --------------------------- | ------ | ------------------------------------------------------- | --------------------------------------------------------- |
| State Bank of India         | `sbin` | <img src="./assets/logos/sbin/logo.svg" height="64" /> | <img src="./assets/logos/sbin/symbol.svg" height="64" /> |
| HDFC Bank                   | `hdfc` | <img src="./assets/logos/hdfc/logo.svg" height="64" /> | <img src="./assets/logos/hdfc/symbol.svg" height="64" /> |
| ICICI Bank                  | `icic` | <img src="./assets/logos/icic/logo.svg" height="64" /> | <img src="./assets/logos/icic/symbol.svg" height="64" /> |
| Axis Bank                   | `utib` | <img src="./assets/logos/utib/logo.svg" height="64" /> | <img src="./assets/logos/utib/symbol.svg" height="64" /> |
| Punjab National Bank        | `punb` | <img src="./assets/logos/punb/logo.svg" height="64" /> | <img src="./assets/logos/punb/symbol.svg" height="64" /> |
| Union Bank of India         | `ubin` | <img src="./assets/logos/ubin/logo.svg" height="64" /> | <img src="./assets/logos/ubin/symbol.svg" height="64" /> |
| ... more banks coming soon  |        |                                                         |                                                           |

➡️ Full list coming soon with **all RBI-recognized banks**.

## 🔧 Optimize & Convert Logos

```sh
# Optimize SVGs
brew install svgo
./optimize.sh
