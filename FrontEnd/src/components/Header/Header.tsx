import { Link,useNavigate } from "react-router-dom";
import Cookies from "js-cookie";

const Header = () => {
    const navigate = useNavigate();
    const username = Cookies.get("username");

    const Logout = () => {
        Cookies.remove("username");
        navigate("/login");
    };

    return (
        <>
        <div style={{display:'flex',
            alignItems:'center',
            padding: '10px 20px',
            gap:'20px',
            borderBottom: '2px solid rgb(205,205,205)'
        }}>
        <img src='../../../public/Workwave Logo.png' style= {{height: '50px'}}/>
        
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/resume">Resumes</Link>

        
        <div style= {{marginLeft:"auto",display:"flex",alignItems:"center",gap:"10px"}}>
            <span>{username}</span>
            <button onClick={Logout}>Logout</button>
        </div>
       
         {/* <a href='/DashBoard'>DashBoard</a>
        <a href='/resume'>Resumes</a> */}
        </div>
        </>

    )
};

export default Header;