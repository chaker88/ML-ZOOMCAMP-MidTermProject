# 🧾 Demographic and Personal Information

## 1. person_gender
**What it means:** Whether the applicant is male or female (sometimes includes “other” or missing).  
**Why it matters:** Helps explore if gender influences loan approval rates (but be careful—banks shouldn’t legally discriminate).  
**Ideas:** Compare approval rates or average incomes between genders.

---

## 2. person_education
**What it means:** The applicant’s highest education level (e.g., high school, bachelor’s, master’s, PhD).  
**Why it matters:** Education can be linked to income and financial stability.  
**Ideas:** Analyze whether higher education levels correlate with higher income or loan approval.

---

## 3. person_home_ownership
**What it means:** Whether the person owns their home, rents, or has a mortgage.  
**Why it matters:** Homeowners may be seen as more financially stable, which can influence loan decisions.  
**Ideas:** Compare approval rates across ownership types (owners vs renters).

---

## 4. loan_intent
**What it means:** The purpose of the loan (e.g., education, car, business, home improvement, etc.).  
**Why it matters:** Some loan types are riskier than others — for instance, business loans might have higher default risk than education loans.  
**Ideas:** Analyze which loan purposes have the highest approval rates or interest rates.

---

## 5. previous_loan_defaults_on_file
**What it means:** Whether the person has defaulted (failed to repay) a loan in the past (Yes/No or 0/1).  
**Why it matters:** A history of default is one of the strongest predictors of loan refusal.  
**Ideas:** Examine how default history affects credit score, loan approval, or interest rate.

---

# 💰 Financial and Employment Information

## 6. person_age
**What it means:** Applicant’s age.  
**Why it matters:** Age may indirectly reflect experience or stability. Younger applicants might have less stable income or credit history.  
**Ideas:** Group ages into bins (e.g., 18–25, 26–35, etc.) to compare approval or income patterns.

---

## 7. person_income
**What it means:** The applicant’s annual income.  
**Why it matters:** Higher income generally means more ability to repay loans.  
**Ideas:** Explore income distribution by loan approval, or create ratios (like loan amount vs income).

---

## 8. person_emp_exp
**What it means:** The number of years the applicant has been employed.  
**Why it matters:** More experience usually means job stability and lower risk.  
**Ideas:** Compare loan approval or credit score across experience levels.

---

# 💳 Loan and Credit Information

## 9. loan_amnt
**What it means:** The total amount of money requested for the loan.  
**Why it matters:** Larger loans carry higher risk for the lender.  
**Ideas:** Compare requested loan amounts for approved vs refused applicants.

---

## 10. loan_int_rate
**What it means:** The interest rate offered for the loan.  
**Why it matters:** Higher interest rates often reflect higher perceived risk.  
**Ideas:** Examine how the interest rate varies with credit score, loan amount, or approval status.

---

## 11. loan_percent_income
**What it means:** Ratio of the loan amount to the applicant’s income (`loan_amnt / person_income`).  
**Why it matters:** It measures **affordability** — a higher ratio means the person is borrowing more relative to what they earn.  
**Ideas:** Check whether higher ratios lead to more refusals.

---

## 12. cb_person_cred_hist_length
**What it means:** The length of the applicant’s credit history (in years).  
**Why it matters:** A longer credit history gives lenders more trust and information about repayment behavior.  
**Ideas:** Explore how credit history length relates to credit score or approval.

---

## 13. credit_score
**What it means:** A numerical value that measures creditworthiness (typically between 300–850).  
**Why it matters:** One of the most important factors — a higher score means lower risk.  
**Ideas:** Plot approval rates by credit score ranges (e.g., poor, fair, good, excellent).

---

## 14. loan_status
**What it means:** Whether the loan was **approved (1)** or **refused (0)** — your **target variable** for prediction.  
**Why it matters:** This is what you want to understand or predict using all the other features.  
**Ideas:** Analyze what patterns distinguish approved vs refused loans.
