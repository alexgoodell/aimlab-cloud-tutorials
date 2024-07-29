
Task
-------------------------

I'd like to create a synthetic dataset of surgical patients formatted in JSON. A description of the column type and an example is shown for each column. 

Column Descriptions
-------------------------

mrn
10 random digits
8881580592

csn
18 random digits
8888158059200881580592

dob
date of birth MM/DD/YYYY between 01/01/1920 and 01/01/2004
01/01/1980

age
integer between 18 and 104, derived from dob
42

sex
self-identified sex of the patient (M, F, O)
F

cpt_primary
5 random digits, underscore, followed by a medical procedure
82945_Glucose, Urine, Random

icd_primary
letter followed by 2 digits, period, 2 digits, period, 2 digits, letter, followed by a description of a medical diagnosis
V97.33XD: Sucked into jet engine, subsequent encounter

icd_secondary
letter followed by 2 digits, period, 2 digits, period, 2 digits, letter, followed by a description of a medical diagnosis
V97.33XD: Sucked into jet engine, subsequent encounter

procedure_primary
description of a medical procedure, all caps
COLONOSCOPY WITH OR WITHOUT BIOPSY

procedure_secondary
description of a medical procedure, all caps. often includes the word "with" or "without" or "possible" or the type of anesthesia "monitored anesthesia care" or "general anesthesia"
MONITORED ANESTHESIA CARE

anesthesia_type
code for the type of anesthesia used (MAC, GA, RA, etc)
MAC

anesthesia_start_time
time of day in 24-hour format
13:00

anesthesia_end_time
time of day in 24-hour format
15:00

anesthesia_duration_minutes
integer between 30 and 300
120

day_of_surgery
date of surgery MM/DD/YYYY between 01/01/2020 and 01/01/2022
01/01/2021

admission_class
either inpatient, outpatient, or observation. Make some caps and some lowercase at random. 
inpatient

allergies
comma separated list of allergies to medications or substances
penicillin, sulfa, peanuts

home_medications
comma separated list of medications the patient is taking (if any; most blank)
metformin, lisinopril, atorvastatin

problem_list
comma separated list of medical problems the patient has (if any; most blank)
diabetes, hypertension, hyperlipidemia

preop_blood_pressure_systolic
integer between 90 and 200
120

preop_blood_pressure_diastolic
integer between 60 and 120
80

preop_heart_rate
integer between 40 and 120
60

preop_temperature_celsius
float between 35 and 40
37.0

preop_oxygen_saturation
int between 90 and 100
98

intraop_bleeding
boolean
True

intraop_hypotension
boolean
False

net_fluid_balance_ml
integer between -5000 and 5000
1000

postop_pain_score
integer between 0 and 10
2

postop_nausea
boolean
False

postop_vomiting
boolean
False

postop_temperature_celsius
float between 35 and 40
37.0

postop_oxygen_saturation
int between 90 and 100
98

postop_blood_pressure_systolic
integer between 90 and 200
120

postop_blood_pressure_diastolic
integer between 60 and 120
80

postop_heart_rate
integer between 40 and 120
60

postop_medication_administered
comma separated list of medications given postoperatively
morphine, ondansetron, acetaminophen

unanticipated_admission
boolean
False

unanticipated_icu_admission
boolean
False

quality_report_filed
boolean - most are False
True

quality_report_comments
text - most are blank. if True, a brief description of the quality issue (vague, hurried, and non-specific)
Safety concerns re wheelchair

disposition
home, ICU, floor, NA







