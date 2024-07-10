import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import React from "react";
import Navbar from "./components/Navbar.jsx";
import Predictors from "./pages/PredictorsPage.jsx";
import About from "./pages/AboutPage.jsx";
import Login from "./pages/LoginPage.jsx";
import Signup from "./pages/SignupPage.jsx";
import HomePage from "./pages/HomePage.jsx";

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/predictors" element={<Predictors />} />
          <Route path="/about" element={<About />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
