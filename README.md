# Smart Dumper Cycle-Time Prediction

A machine-learning based system for predicting **dumper cycle time** in opencast mining operations and estimating corresponding haulage productivity.

## Live Demo

https://smart-dumper-cycle-time-prediction-bmgu3tqrhgzx9xpuibfxas.streamlit.app/

## GitHub Repository

https://github.com/KripeshOP/Smart-Dumper-Cycle-Time-Prediction

---

## Overview

Dumper cycle time is an important parameter in opencast mine haulage because it directly affects the number of trips completed by a dumper and the overall material-handling productivity.

This project develops a **Linear Regression model** to predict total dumper cycle time using operational and environmental parameters such as:

- Haul distance
- Payload
- Road gradient
- Road condition
- Weather
- Shift
- Loading time
- Loaded travel time
- Dumping time
- Return travel time
- Waiting time

The predicted cycle time is then used to calculate:

- Trips per hour
- Haulage productivity in tonnes/hour

The model is integrated into an interactive **Streamlit application**.

---

## Project Pipeline

```text
Mining Trip Data
       ↓
Data Preprocessing
       ↓
Feature Selection
       ↓
Categorical Encoding
       ↓
Train-Test Split
       ↓
Linear Regression Model
       ↓
Cycle-Time Prediction
       ↓
Trips/Hour Calculation
       ↓
Productivity Calculation
       ↓
Streamlit Application

```
Smart-Dumper-Cycle-Time-Prediction/
│── app.py
│── cycle_time_model.pkl
│── requirements.txt
│── README.md
│── NALCO_Synthetic_Dumper_Cycle_Time_Dataset.xlsx
```


```bash
pip install -r requirements.txt
streamlit run app.py
```





**Kripesh Kumar Karmakar**

Mining Engineering

National Institute of Technology Rourkela
