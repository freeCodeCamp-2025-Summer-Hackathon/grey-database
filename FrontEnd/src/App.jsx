import React from "react";
import Login from "../src/components/Login/Login.jsx";
import { Toaster } from "react-hot-toast";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Header from "./components/Header/Header";
import Dashboard from "./components/Dashboard/Dashboard";
import useAuthStore from "./store/useAuthStore.js";

function App() {
  const loggedIn = useAuthStore((state) => state.loggedIn);

  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route
          path="/login"
          element={loggedIn ? <Navigate to="/dashboard" /> : <Login />}
        />
        <Route
          path="/dashboard"
          element={
            loggedIn ? (
              <>
                <Header />
                <Dashboard />
              </>
            ) : (
              <Navigate to="/login" />
            )
          }
        />
        <Route
          path="*"
          element={<Navigate to={loggedIn ? "/dashboard" : "/login"} />}
        />
      </Routes>
    </BrowserRouter>
    <Toaster position="top-right"></Toaster>
    </>
    
  );
}

export default App;
