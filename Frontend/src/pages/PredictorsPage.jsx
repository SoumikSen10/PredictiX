import React from "react";
import Card from "../components/Card";
import heartImage from "../assets/heart.png";
import lungImage from "../assets/lung.png";
import diabetesImage from "../assets/diabetes.png";
import breastImage from "../assets/breast.png";
import "../App.css";

function Predictors() {
  return (
    <div className="predictor-container">
      <h1 className="welcome-text">WELCOME, XYZ XYZ</h1>
      <p className="description">
        Comprehensive Health Diagnostics Suite: AI-powered systems for early
        detection and accurate predictions of breast cancer, lung cancer, heart
        disease, and diabetes. Empowering proactive healthcare for a healthier
        future.
      </p>
      <div className="card-container">
        <Card
          image={heartImage}
          title="Heart Disease"
          description="Guarding Hearts: AI solutions for accurate prediction and early intervention in heart disease."
        />
        <Card
          image={lungImage}
          title="Lung Cancer"
          description="Clearing the Air: AI-driven insights for proactive lung cancer prediction and care."
        />
        <Card
          image={breastImage}
          title="Breast Cancer"
          description="Beyond Detection: AI innovation for early, precise breast cancer prediction and care."
        />
        <Card
          image={diabetesImage}
          title="Diabetes"
          description="Empowering Health: AI solutions for precise diabetes prediction and proactive wellness."
        />
      </div>
    </div>
  );
}

export default Predictors;
