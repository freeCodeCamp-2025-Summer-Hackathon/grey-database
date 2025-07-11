import React from 'react';
import './Login.css';

function Login() {
    return(
        <div className="outer-box">
            <div className="inner-login-box"><img src="/Workwave Logo.png" alt="WorkWave Logo" className="logo" />
                
                <h2>Log in to continue</h2>

                <label>Email</label><input type="email" placeholder="Enter your email" />
                <label>Password</label><input type="password" placeholder="Enter your password" />

                <span className="remember-me">
                    <input type="checkbox" id="remember" /><label htmlFor="remember">Remember me</label>
                    </span>

                    <button className="continue-button">Continue</button>
                    </div>
                    </div>
    );
};

export default Login;