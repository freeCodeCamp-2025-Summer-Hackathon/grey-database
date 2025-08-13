import { Link, useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import useAuthStore from "../../store/useAuthStore";
import "./site.css";

const Header = () => {
  const navigate = useNavigate();
  const username = Cookies.get("username");
  const logout = useAuthStore((state) => state.logout);

  const Logout = () => {
    Cookies.remove("username");
    logout();
    navigate("/login");
  };

  return (
    <>
      <div className="header-container">
        <img src="../../../public/Workwave Logo.png" className="logo-image " />

        <div className="links">
          <Link to="/dashboard" className="dashboard-link">
            Dashboard
          </Link>
          <Link to="/resume" className="resume-link">
            Resumes
          </Link>
        </div>

        <div className="user-section">
          <span className="username">{username?.[0]}</span>
          <button className="logout-button" onClick={Logout}>
            Logout
          </button>
        </div>
      </div>
    </>
  );
};

export default Header;
