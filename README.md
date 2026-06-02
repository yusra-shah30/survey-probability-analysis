# Survey Probability Analysis (Excel / Google Sheets Project)

## 📌 Project Title

Survey Probability Analysis of Preferred Social Media App

## 👤 Student Information

* Name: Yusra Jan
* Tool Used: Google Sheets / Microsoft Excel
* Project Type: Survey Data Probability Analysis

## 🎯 Project Objective

The objective of this project is to analyze survey responses using probability concepts. This project calculates:

* Frequency of responses
* Probability distribution
* Percentage distribution
* Conditional probability (Daily vs Weekly users)
* Expected Value Prediction (out of 100 respondents)
* Simulation-Based Probability Analysis (Novelty Feature)

## 📊 Dataset Description

A survey dataset of 60 respondents was created using the following question:

**Question:** Preferred Social Media App

**Options:**

* Instagram
* YouTube
* TikTok
* Facebook

An additional column was included:

**Usage Frequency:** Daily / Weekly

This dataset helps identify majority patterns and user preference trends.

## Google Spreadsheet Link

https://docs.google.com/spreadsheets/d/1ybyK2AIHMNef2OBWUMvv2TjAmiQebutcag52lgjn1Gs/edit?usp=sharing

## Project Files

* README.md – Project documentation
* main.py – Python implementation of survey probability analysis
* Google Spreadsheet – Data collection and analysis
* Dashboard – Visual summary of results

## 📅 Daily Progress Log

### Day 1 (01-05-2026)

* Created Google Spreadsheet for project tracking.
* Planned project structure and probability analysis workflow.
* Created separate sheets for Survey Data, Analysis, Dashboard, and Simulation.
* Shared Google Spreadsheet access with teacher: [syedhydermahadi@gmail.com](mailto:syedhydermahadi@gmail.com).
* Created GitHub public repository.
* Added project title and basic description in README.md.

### Day 2 (02-05-2026)

* Designed survey question and finalized response categories.
* Prepared initial survey format for data collection.
* Added headings and formatting in Survey Data sheet.
* Tested spreadsheet structure and formula layout.

### Day 3 (03-05-2026)

* Entered initial sample survey responses in Survey Data sheet.
* Added respondent serial numbering for organized dataset.
* Verified data entry consistency.
* Updated GitHub README with project setup progress.

### Day 4 (04-05-2026)

* Expanded survey dataset with additional responses.
* Reviewed dataset for duplicate or missing values.
* Improved spreadsheet formatting using borders and colors.
* Organized survey responses properly for analysis.

### Day 5 (05-05-2026)

* Created Analysis sheet for probability calculations.
* Used COUNTIF formulas to calculate frequency of each answer choice.
* Verified calculations manually for accuracy.
* Added labels and headings for analysis tables.

### Day 6 (06-05-2026)

* Calculated probability distribution using Frequency ÷ Total Responses.
* Added percentage distribution calculations.
* Verified that total probability equals 1.
* Verified that total percentage equals 100%.

### Day 7 (07-05-2026)

* Created Pie Chart to visualize overall survey distribution.
* Added percentage labels in the Pie Chart.
* Adjusted chart formatting for better presentation.
* Updated GitHub README with analysis progress.

### Day 8 (08-05-2026)

* Created Bar Chart for frequency comparison.
* Compared popularity of all social media apps visually.
* Identified the most selected and least selected platforms.
* Improved chart titles and axis labels.

### Day 9 (09-05-2026)

* Rechecked COUNTIF formulas and dataset accuracy.
* Corrected spelling inconsistencies in survey responses.
* Verified frequency and probability calculations.
* Improved overall spreadsheet organization.

### Day 10 (10-05-2026)

* Added Usage Frequency column in Survey Data sheet.
* Entered Daily and Weekly user categories.
* Prepared dataset for conditional probability analysis.
* Updated GitHub repository progress.

### Day 11 (11-05-2026)

* Used COUNTIFS formulas for Daily user analysis.
* Calculated conditional probability for Daily users.
* Created a separate Daily probability summary table.
* Verified all Daily condition calculations.

### Day 12 (12-05-2026)

* Performed Weekly user conditional probability calculations.
* Created a Weekly probability summary table.
* Verified Weekly probability totals equal 1.
* Compared Daily and Weekly trends.

### Day 13 (13-05-2026)

* Created a comparison summary between Daily and Weekly users.
* Added a probability comparison table.
* Wrote interpretation notes explaining trends.
* Improved table formatting and alignment.

### Day 14 (14-05-2026)

* Created a combined comparison chart for Daily vs Weekly users.
* Customized chart labels and legends.
* Verified chart accuracy with dataset values.
* Updated GitHub README with comparison analysis progress.

### Day 15 (15-05-2026)

* Reviewed all formulas used in the Analysis sheet.
* Cross-checked totals and percentages.
* Corrected formatting inconsistencies.
* Improved readability of spreadsheet sections.

### Day 16 (16-05-2026)

* Added a summary findings section in the Analysis sheet.
* Documented the highest and lowest probability values.
* Added observations about user preference patterns.
* Improved presentation layout.

### Day 17 (17-05-2026)

* Planned novelty features for higher project scoring.
* Researched simulation-based probability analysis concepts.
* Designed the Expected Value Prediction section.
* Prepared formulas for prediction analysis.

### Day 18 (18-05-2026)

* Created the Expected Value Prediction table.
* Calculated expected users out of 100 respondents.
* Verified prediction values using probability formulas.
* Added explanation notes for the expected value concept.

### Day 19 (19-05-2026)

* Created the Simulation sheet for random probability generation.
* Used RAND and INDEX formulas for simulation.
* Generated random social media responses automatically.
* Tested simulation functionality multiple times.

### Day 20 (20-05-2026)

* Calculated simulated frequency and probability distributions.
* Compared simulation results with original survey probabilities.
* Verified similarity in trends and outcomes.
* Added interpretation notes for simulation analysis.

### Day 21 (21-05-2026)

* Created the Dashboard sheet for the final project summary.
* Added total responses, highest probability, and lowest probability indicators.
* Added probability validation checks.
* Improved dashboard formatting and alignment.

### Day 22 (22-05-2026)

* Organized all charts and tables in final format.
* Improved visual presentation using colors and borders.
* Verified chart placements and labels.
* Updated GitHub README documentation.

### Day 23 (23-05-2026)

* Rechecked the entire spreadsheet for formula errors.
* Verified all totals and conditional probabilities.
* Tested simulation formulas again for consistency.
* Reviewed final findings and recommendations.

### Day 24 (24-05-2026)

* Added the final conclusion and recommendation section.
* Improved overall report formatting.
* Verified spreadsheet sharing permissions.
* Finalized README structure and project documentation.

### Day 25 (25-05-2026) – Final Project Completion

* Completed Python implementation of survey probability analysis.
* Finalized the complete Survey Probability Analysis project.
* Verified all formulas, charts, dashboard values, and simulation outputs.
* Confirmed Probability Sum = 1 and Percentage Sum = 100%.
* Completed all novelty features including Expected Value Prediction and Random Simulation Analysis.
* Finalized Pie Chart, Bar Chart, Daily vs Weekly Comparison Chart, and Dashboard.
* Updated GitHub README with complete project details and final submission content.
* Prepared the project for final evaluation and submission.

## 🧮 Methods and Formulas Used

### 1. Frequency Calculation (COUNTIF)

Frequency was calculated using:

=COUNTIF(range,"Option")

Example:

=COUNTIF('Survey Data'!C2:C61,"Instagram")

### 2. Probability Calculation

Probability was calculated using:

Probability = Frequency / Total Responses

Formula Example:

=B2/SUM($B$2:$B$5)

### 3. Percentage Calculation

Percentage was calculated using:

Percentage = Probability × 100

Formula Example:

=C2*100

### 4. Conditional Probability (COUNTIFS)

Conditional probability was calculated using:

=COUNTIFS(AnswerRange,"Instagram",UsageRange,"Daily")

Example:

=COUNTIFS('Survey Data'!C2:C61,"Instagram",'Survey Data'!D2:D61,"Daily")

### 5. Expected Value Prediction (Novelty Feature)

Expected value predicts the expected number of users out of 100 respondents.

Expected Value = Probability × 100

Formula Example:

=Probability*100

### 6. Random Simulation (Novelty Feature)

A simulation was created using:

=INDEX({"Instagram","YouTube","TikTok","Facebook"},RANDBETWEEN(1,4))

This generates random responses and compares the simulated probability distribution with real survey results.

## 📈 Charts and Visualizations

The following charts were created:

* Pie Chart (Overall Distribution)
* Bar Chart (Frequency Comparison)
* Daily vs Weekly Comparison Chart
* Dashboard Sheet (Final Summary)

## 🏆 Key Results

* Most Selected App: Instagram
* Least Selected App: Facebook
* Major Trend: Daily users show a stronger preference for Instagram compared to Weekly users.

## ✅ Final Conclusion

The survey probability analysis shows that Instagram is the most preferred social media platform with the highest frequency and probability value. YouTube and TikTok have moderate probabilities and remain strong competitors. Facebook has the lowest probability and is the least preferred platform in the dataset. Conditional probability analysis confirms that Daily users prefer Instagram more strongly than Weekly users. Simulation results also support the observed trend, validating the probability distribution.

## 📌 Final Recommendation

Based on probability distribution, conditional probability analysis, expected value prediction, and simulation results, Instagram is recommended as the best platform for marketing, awareness campaigns, and audience engagement strategies.

## 📌 Project Status

✅ Project Completed Successfully
✅ Final Submission Ready

