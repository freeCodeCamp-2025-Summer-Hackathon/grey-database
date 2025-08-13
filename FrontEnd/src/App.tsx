import React from "react";
import Login from "./components/Login/Login.js";
import { Toaster } from "react-hot-toast";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Header from "./components/Header/Header.js";
import Dashboard from "./components/Dashboard/Dashboard.js";
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

           <Route
        path="/resume"
        element={
          loggedIn ? (
            <>
            <Header />
            <div>Resume Page</div>
            </>
          ) : (
            <Navigate to="/login" />
          )
        } 
        />
        
      </Routes>
    </BrowserRouter>
    <Toaster position="top-right"></Toaster>
    </>
    
  );
}

export default App;
