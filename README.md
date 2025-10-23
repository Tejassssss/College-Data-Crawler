# College Info Scraper

This Python script uses **Selenium** to automatically collect and display information about a college from [CollegeSimply.com](https://www.collegesimply.com/).
It retrieves data such as enrollment, location, housing, tuition cost, and admissions statistics based on a college name provided by the user.

---

## 🧩 Features

* Automatically opens Firefox and searches for a college
* Scrapes details like:

  * State
  * Student population
  * Campus setting
  * On-campus housing
  * Profit type (public/private)
  * Website
  * Sticker price and average net price
  * Acceptance rate, GPA, SAT, and ACT averages

---

## ⚙️ Requirements

Make sure you have the following installed:

* **Python 3.7+**
* **Selenium** library

  ```bash
  pip install selenium
  ```
* **GeckoDriver** (for Firefox)

  * Download from: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
  * Add it to your system PATH

---

## 🚀 How to Run

1. Save the script as `college_scraper.py`
2. Open a terminal in the same directory
3. Run:

   ```bash
   python college_scraper.py
   ```
4. When prompted, type the name of the college (e.g., `Worcester Polytechnic Institute`)
5. Wait a few seconds as Selenium opens Firefox, navigates the site, and prints the information to your terminal.

---

## 🧠 Notes

* This script uses **XPath** and **CSS selectors** to locate elements, which may break if the CollegeSimply website layout changes.
* Some colleges may not have all data available — in those cases, the script may throw an error or skip fields.
* You can modify `sleep()` durations if your internet speed affects page load times.

---

## 📋 Example Output

```
---------------------------------------------------------
College Name: Worcester Polytechnic Institute
State: Massachusetts
Students Enrolled: 6,900
Campus Setting: City
On-Campus Housing: Yes
Profit Type: Non-Profit
Website: www.wpi.edu

Sticker Price: $54,640 per year
Net Price: $43,002

Acceptance Rate: 59%
Average GPA: 3.9
Average Sat: 1360
Average Sat Math: 690
Average Sat English: 670
Average ACT: 31
---------------------------------------------------------
```
