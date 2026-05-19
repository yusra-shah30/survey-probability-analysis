 # Survey Probability Analysis (Excel / Google Sheets Project)

## 📌 Project Title
**Survey Probability Analysis of Preferred Social Media App**

---

## 👤 Student Information
- **Name:** Yusra Jan  
- **Tool Used:** Google Sheets / Microsoft Excel  
- **Project Type:** Survey Data Probability Analysis  

---

## 🎯 Project Objective
The objective of this project is to analyze survey responses using probability concepts.  
This project calculates:
- Frequency of responses
- Probability distribution
- Percentage distribution
- Conditional probability (Daily vs Weekly users)
- Expected value prediction (out of 100)
- Simulation-based probability analysis (novelty)

---

## 📊 Dataset Description
A survey dataset of **60 respondents** was created using the following question:

**Question:** Preferred Social Media App  
**Options:** Instagram, YouTube, TikTok, Facebook  

An additional column was included:
- **Usage Frequency:** Daily / Weekly  

This dataset helps identify majority patterns and user preference trends.

---

## Google Spreadsheet Link
https://docs.google.com/spreadsheets/d/1ybyK2AIHMNef2OBWUMvv2TjAmiQebutcag52lgjn1Gs/edit?usp=sharing

## Daily Progress Log

### Day 1 (10-05-2026)
- Created Google Spreadsheet for project tracking.
- Added proper headings (Date, Start Time, Content, End Time).
- Shared Google Spreadsheet access with teacher: syedhydermahadi@gmail.com
- Created GitHub public repository.
- Added project title and description in README.md.
- Sent GitHub collaborator invite to teacher (syedhydermahadi@gmail.com).
### Day 2 (11-05-2026)
- Created "Survey Data" sheet and entered sample survey responses.
- Created "Analysis" sheet for probability calculations.
- Used COUNTIF formula to calculate frequency of each answer choice.
- Calculated probability of each option using Frequency / Total Responses.
- Created pie chart to show opinion distribution and majority pattern.
- Updated Google spreadsheet and GitHub README with Day 2 progress.
### Day 3 (12-05-2026)
- Extended survey dataset by adding more responses for better accuracy.
- Updated analysis formulas according to new dataset size.
- Verified frequency calculations using COUNTIF.
- Updated probability and percentage table for answer distribution.
- Created pie chart and bar chart for visualization of majority patterns.
- Identified most selected and least selected answer choice.
- Updated Google Spreadsheet and GitHub README with Day 3 progress.
- ### Day 4 (13-05-2026)
- Verified frequency and probability calculations after dataset expansion.
- Confirmed total probability equals 1 and total percentage equals 100%.
- Created bar chart for frequency comparison of each answer choice.
- Updated pie chart to show percentage labels for better visualization.
- Wrote summary findings showing most selected and least selected survey option.
- Updated Google Spreadsheet and GitHub README with Day 4 progress.
- ### Day 5 (14-05-2026)
- Added an extra column "Usage Frequency" in Survey Data for conditional probability analysis.
- Calculated conditional probability based on Daily users using COUNTIFS formulas.
- Created a new conditional probability summary table in Analysis sheet.
- Improved spreadsheet formatting (borders, bold headings, correct percent format).
- Verified calculations and updated charts for improved presentation.
- Updated Google Spreadsheet and GitHub README with Day 5 progress.
- ### Day 6 (15-05-2026)
- Created conditional probability table for Weekly users using COUNTIFS formulas.
- Calculated P(Answer | Weekly) and percentage distribution.
- Compared conditional probability results of Daily vs Weekly users.
- Verified total probability equals 1 for Weekly condition.
- Updated analysis sheet and ensured correct formatting.
- Updated Google Spreadsheet and GitHub README with Day 6 progress.
### Day 7 (16-05-2026)
- Created comparison summary between conditional probability results of Daily and Weekly users.
- Added comparison table showing probability differences for each answer choice.
- Wrote interpretation notes explaining majority patterns and trends.
- Created combined bar chart to compare Daily vs Weekly distribution.
- Verified calculations and corrected formatting issues in analysis sheet.
- Updated Google Spreadsheet and GitHub README with Day 7 progress.
- ### Day 8 (17-05-2026)
- Prepared final project report structure including summary and conclusion section.
- Added final summary statistics such as total responses, highest probability option, and lowest probability option.
- Organized all charts (pie chart, bar chart, comparison chart) in analysis sheet for final presentation.
- Added final findings and conclusion notes in spreadsheet.
- Updated Google Spreadsheet and GitHub README with Day 8 progress.
### Day 9 (18-05-2026)
- Verified the accuracy of survey dataset and corrected any spelling inconsistencies.
- Rechecked all formulas for frequency, probability, percentage, and conditional probability.
- Verified totals (probability sum = 1 and percentage sum = 100).
- Added discussion and recommendations section in analysis sheet.
- Improved formatting and presentation with proper headings and table borders.
- Updated GitHub README and ensured Google Spreadsheet link is working properly.
### Day 10 (19-05-2026) [Final Project Completion]
- Finalized the Survey Probability Analysis project with novelty improvements.
- Created a Dashboard sheet showing key project results: Total Responses, Most Selected App, Least Selected App, and probability validation checks.
- Added Expected Value Prediction table to estimate expected users out of 100 respondents.
- Developed a Simulation sheet using RAND and INDEX formulas to generate random survey responses and calculate simulated probability distribution.
- Compared simulation probabilities with original survey probabilities to validate trends.
- Finalized all visualizations including Pie Chart, Bar Chart, and Daily vs Weekly Comparison Chart.
- Added final conclusion and recommendation section in Analysis sheet.
- Verified formulas, totals, spreadsheet sharing permissions, and GitHub repository README for final submission.




## 🧮 Methods and Formulas Used

### 1) Frequency Calculation (COUNTIF)
Frequency was calculated using:

`=COUNTIF(range,"Option")`

Example:

`=COUNTIF('Survey Data'!C2:C61,"Instagram")`

---

### 2) Probability Calculation
Probability was calculated using:

**Probability = Frequency / Total Responses**

Formula example:

`=B2/SUM($B$2:$B$5)`

---

### 3) Percentage Calculation
Percentage was calculated using:

`=Probability*100`

Example:

`=C2*100`

---

### 4) Conditional Probability (COUNTIFS)
Conditional probability was calculated using:

`=COUNTIFS(AnswerRange,"Instagram",UsageRange,"Daily")`

Example:

`=COUNTIFS('Survey Data'!C2:C61,"Instagram",'Survey Data'!D2:D61,"Daily")`

---

### 5) Expected Value Prediction (Novelty Feature)
Expected value predicts expected users out of 100 respondents:

**Expected Value = Probability × 100**

Example:

`=Probability*100`

---

### 6) Random Simulation (Novelty Feature)
A simulation was created using:

`=INDEX({"Instagram","YouTube","TikTok","Facebook"},RANDBETWEEN(1,4))`

This generates random responses and compares simulated probability distribution with real survey results.

---

## 📈 Charts and Visualizations
The following charts were created:
- **Pie Chart** (Overall Distribution)
- **Bar Chart** (Frequency Comparison)
- **Daily vs Weekly Comparison Chart**
- **Dashboard Sheet** (Final Summary)

---

## 🏆 Key Results
- **Most Selected App:** Instagram  
- **Least Selected App:** Facebook  
- **Major Trend:** Daily users show stronger preference for Instagram compared to Weekly users.

---

## ✅ Final Conclusion
The survey probability analysis shows that **Instagram is the most preferred social media platform** with the highest frequency and probability value.  
**YouTube and TikTok** have moderate probabilities and remain strong competitors.  
**Facebook has the lowest probability** and is the least preferred platform in the dataset.

Conditional probability analysis confirms that **Daily users prefer Instagram more strongly** than Weekly users.  
Simulation results also support the same trend, validating the probability distribution.

---

## 📌 Final Recommendation
Based on probability distribution, conditional probability, and simulation results, **Instagram is recommended as the best platform for marketing, awareness campaigns, and audience engagement strategies**.

---
## 📌 Project Status
✅ Project Completed Successfully  
✅ Final Submission Ready  
