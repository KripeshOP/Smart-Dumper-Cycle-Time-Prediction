
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Smart Dumper Cycle Time Prediction", page_icon="🚛", layout="wide")

model = joblib.load("cycle_time_model.pkl")

st.sidebar.title("🚛 Mining ML Dashboard")
st.sidebar.info("""
### Smart Dumper Cycle Time Prediction

Developer: Kripesh Kumar Karmakar

Institute: NIT Rourkela

Model: Linear Regression
""")

st.title("🚛 Smart Dumper Cycle Time Prediction System")
st.write("Predict dumper cycle time and estimate productivity.")

col1, col2 = st.columns(2)

with col1:
    distance = st.number_input("Haul Distance (km)",4.0,5.0,4.5)
    payload = st.number_input("Payload (tonnes)",53.0,56.0,55.0)
    gradient = st.number_input("Road Gradient (%)",2.0,6.0,4.0)
    loading = st.number_input("Loading Time (min)",2.5,4.0,3.1)

with col2:
    travel = st.number_input("Loaded Travel Time (min)",6.0,15.0,9.0)
    dumping = st.number_input("Dumping Time (min)",0.5,2.0,1.0)
    return_time = st.number_input("Return Travel Time (min)",6.0,15.0,8.0)
    waiting = st.number_input("Waiting Time (min)",0.0,5.0,2.0)

road = st.selectbox("Road Condition",["Good","Average","Poor"])
weather = st.selectbox("Weather",["Clear","Cloudy","Rainy"])
shift = st.selectbox("Shift",["Day","Night"])

if "history" not in st.session_state:
    st.session_state.history=[]

if st.button("🚀 Predict Cycle Time",use_container_width=True):

    input_data = pd.DataFrame({
        "Trip_ID":[1],
        "Haul_Distance_km":[distance],
        "Payload_t":[payload],
        "Road_Gradient_percent":[gradient],
        "Loading_Time_min":[loading],
        "Travel_Time_Loaded_min":[travel],
        "Dumping_Time_min":[dumping],
        "Return_Travel_Time_min":[return_time],
        "Waiting_Time_min":[waiting],
        "Road_Condition_Good":[1 if road=="Good" else 0],
        "Road_Condition_Poor":[1 if road=="Poor" else 0],
        "Weather_Cloudy":[1 if weather=="Cloudy" else 0],
        "Weather_Rainy":[1 if weather=="Rainy" else 0],
        "Shift_Night":[1 if shift=="Night" else 0]
    })

    prediction=model.predict(input_data)
    cycle_time=float(prediction[0])
    trips=60/cycle_time
    tph=trips*payload

    a,b,c=st.columns(3)
    a.metric("Cycle Time",f"{cycle_time:.2f} min")
    b.metric("Trips/Hour",f"{trips:.2f}")
    c.metric("Productivity",f"{tph:.1f} TPH")

    if cycle_time<=20:
        st.success("🟢 Excellent Efficiency")
        rec="Maintain current operating conditions."
    elif cycle_time<=22:
        st.warning("🟡 Good Efficiency")
        rec="Reduce waiting time where possible."
    else:
        st.error("🔴 Needs Improvement")
        rec="Improve dispatch and reduce delays."

    st.progress(min(max(int((24-cycle_time)/4*100),0),100))

    st.subheader("Recommendation")
    st.info(rec)

    row={
        "Cycle Time":round(cycle_time,2),
        "Trips/Hour":round(trips,2),
        "TPH":round(tph,2),
        "Road":road,
        "Weather":weather,
        "Shift":shift
    }
    st.session_state.history.append(row)

    st.subheader("Prediction History")
    hist=pd.DataFrame(st.session_state.history)
    st.dataframe(hist,use_container_width=True)

    st.download_button(
        "Download Prediction History",
        hist.to_csv(index=False).encode(),
        "prediction_history.csv",
        "text/csv"
    )

st.markdown("---")
st.caption("Developed by Kripesh Kumar Karmakar | NIT Rourkela")
