import { Link,useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import useAuthStore from "../../store/useAuthStore";

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
        <div style={{display:'flex',
            alignItems:'center',
            padding: '10px 20px',
            gap:'20px',
            borderBottom: '2px solid rgb(205,205,205)',
            justifyContent:'space-between'
        }}>
        <img src='../../../public/Workwave Logo.png' style= {{height: '50px'}}/>
        
        <div style={{
            display: 'flex',
            gap: '20px'
        }}>
            <Link to="/dashboard" style={{
                textDecoration:"none",
                color:"#003366",
                fontWeight:"500",
                padding: "5px 8px",
                borderRadius:"5px",
            }}>Dashboard</Link>
            <Link to="/resume" style={{
                textDecoration:"none",
                color:"#003366",
                fontWeight:"500",
                padding: "4px 6px",
                borderRadius:"6px",
            }}>Resumes</Link>

        </div>
        
        <div style= {{display:"flex",alignItems:"center",gap:"10px"}}>
            <span
                style={{
                    display: "inline-flex",
                    alignItems: "center",
                    justifyContent: "center",
                    width: "36px",
                    height: "36px",
                    borderRadius: "50%",
                    background: "#e6e6e8",
                    fontWeight: "bold",
                    fontSize: "16px",
                    color: "#03040a",
                    textTransform: "uppercase"
                }}
            >
                {username?.[0]}
            </span>
            <button onClick={Logout} style={{
                backgroundColor:"#0C66E4",
                color:"#ffffff",
                border:"none",
                borderRadius:"5px",
                cursor:"pointer",
                fontWeight:"500",
                padding: "12px 12px"
            }}>Logout</button>
        </div>
       
         
        </div>
        </>

    )
};

export default Header;