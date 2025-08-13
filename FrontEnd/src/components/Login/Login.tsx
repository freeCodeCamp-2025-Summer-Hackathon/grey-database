import React from "react";
import "./Login.css";
import useAuthStore from "../../store/useAuthStore";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [userName, setUserName] = React.useState("");
  const [password, setPassword] = React.useState("");
  const { login } = useAuthStore();
  let navigate = useNavigate();

  const onUserNameChange = (event) => {
    setUserName(event.target.value);
  };

  const onPasswordChange = (event) => {
    setPassword(event.target.value);
  };
  const onLoginClick = () => {
    login(userName, password);
  };

  return (
    <div className="outer-box">
      <div className="inner-login-box">
        <img src="/Workwave Logo.png" alt="WorkWave Logo" className="logo" />

        <h2>Log in to continue</h2>

        <label>Email</label>
        <input
          type="email"
          placeholder="Enter your email"
          onChange={onUserNameChange}
        />
        <label>Password</label>
        <input
          type="password"
          placeholder="Enter your password"
          onChange={onPasswordChange}
        />

        <span className="remember-me">
          <input type="checkbox" id="remember" />
          <label htmlFor="remember">Remember me</label>
        </span>

        <button className="continue-button" onClick={onLoginClick}>
          Continue
        </button>
      </div>
    </div>
  );
};

export default Login;
