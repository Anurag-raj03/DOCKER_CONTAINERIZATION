# 🐳🚀 Dockerized ML Model with MLOps - Sleep Efficiency Predictor 🌙✨

## 📌 Overview

Welcome to my **Dockerized ML Model Deployment** project! 🚀 This project focuses on **containerizing** a Machine Learning model using **Docker** and **MLflow** for tracking experiments. The goal is to **deploy a sleep efficiency prediction model** while exploring **MLOps best practices**. ⚡

🔹 **Main Focus**: **Dockerization & MLflow Integration** 🐳📈  
🔹 **Not Focused on**: Achieving the highest accuracy ❌📊  
🔹 **Python Version**: **3.11** 🐍  
🔹 **Repository Status**: **Public** 🌍

---

## 🎯 What This Project Covers

✅ **Dockerizing** a Streamlit ML App 🌐  
✅ Using **Volumes** to manage data persistence 📂  
✅ **MLflow Tracking** to log experiments & monitor model performance 📊  
✅ Running the ML model inside a **containerized environment** 🖥️  
✅ Building an **MLOps pipeline** to improve ML model management 🔄  

---

## 🔥 Technologies & Tools Used

| 🛠️ Technology | 🚀 Purpose |
|--------------|-----------|
| **Docker** 🐳 | Containerizing the ML Model |
| **Streamlit** 🎨 | Interactive UI for Predictions |
| **MLflow** 📊 | Experiment Tracking & Model Logging |
| **Python 3.11** 🐍 | Main Programming Language |
| **Scikit-learn** 📚 | Model Training |
| **Git & GitHub** 🔗 | Version Control |

---

## 🏗️ Docker Setup & Configuration

Here's how Docker is used in this project! 🔥

### **1️⃣ Docker Compose File (docker-compose.yml)**

🔹 **Volumes** are used to persist **model, process files, and logs** between container runs.  
🔹 **Restart Policy** ensures the container restarts if it stops unexpectedly. 🚀  
🔹 **Port Mapping** exposes Streamlit on `8501`. 🌍  

---

### **2️⃣ Dockerfile - Building the Container**

🔹 **Base Image**: Using Python 3.11 🐍  
🔹 **Installing Dependencies** from `requirements.txt` 📦  
🔹 **Copying Application Code** into the container 📂  
🔹 **Running Streamlit App** inside the container 🎨  

---

## 🚀 Running the Project with Docker

### **1️⃣ Build & Start the Container**
```bash
docker-compose up --build
```

### **2️⃣ Stop the Running Container**
```bash
docker-compose down
```

### **3️⃣ Check Running Containers**
```bash
docker ps
```

### **4️⃣ Remove Unused Images & Containers**
```bash
docker system prune -a
```

---

## 📊 MLflow Integration - Experiment Tracking 🎯

MLflow helps in **tracking model performance** and maintaining experiment logs. 📝

### **How MLflow Helps in This Project?**
✅ **Logging Model Performance** 📊  
✅ **Tracking Different Experiments** 🔄  
✅ **Versioning ML Models** 📂  
✅ **Comparing Different Runs** 📈  

### **Start MLflow UI & Track Models**
```bash
mlflow ui --host 0.0.0.0 --port 5000
```
📍 Open in Browser: **http://localhost:5000** 🌐  

---

## 🎯 Machine Learning Model Overview

This project uses a **basic regression model** for predicting **sleep efficiency** based on user input features like:

🔹 Age  
🔹 Sleep Duration ⏳  
🔹 REM Sleep (%) 😴  
🔹 Deep Sleep (%) 🌙  
🔹 Light Sleep (%) 💡  
🔹 Number of Awakenings ⚡  

**Note:** The model is **not optimized for accuracy** but serves as a demonstration of **Docker & MLOps concepts**. 🚀

---

## 🔗 Useful Links & Resources

🔹 **GitHub Repo**: [👉 Click Here](https://github.com/Anurag-raj03/DOCKER_CONTAINERIZATION) 🖥️  
🔹 **My Kaggle Profile**: [👉 Click Here](https://www.kaggle.com/anuragraj03/code) 📊  

---

## 🎯 Next Steps: MLOps Pipeline 🔄

🚀 **Future Enhancements:**
- Integrate **GitHub Actions** for CI/CD 🤖
- Implement **model versioning with MLflow** 📂
- Automate **deployment using Kubernetes** ☸️
- Improve **data pipeline automation** 🔄

---

## 📢 Conclusion 🎉

This project showcases **Dockerization of a Machine Learning model** 🐳📊 with **MLflow integration** to track experiments. The main focus was on **MLOps principles**, not model accuracy. Hope this helps anyone getting started with **Docker + MLflow + MLOps**! 🚀💡

💬 **Have suggestions?** Feel free to reach out! 😃🚀

