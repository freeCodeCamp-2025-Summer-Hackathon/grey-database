import { create } from "zustand";
import axios from "axios";
import Cookies from "js-cookie";
import toast from "react-hot-toast";

const apiUrl = "http://127.0.0.1:5000";
const authApi = `${apiUrl}/auth`;

type AuthStore = {
    loading: boolean;
    error: string | null;
    loggedIn: boolean;

    register: (username: string, password: string) => Promise<void>;
    login: (username: string, password: string) => Promise<void>;
    logout: () => void;
};

const useAuthStore = create<AuthStore>((set) => ({
    loading: false,
    error: null,
    loggedIn: false,

    register: async (username, password) => {
        set({ loading: true, error: null });
        try {
            const res = await axios.post(`${authApi}/register`, {
                username,
                password,
            });
            toast.success(res.data.message || "Registered successfully");
        } catch (err: any) {
            toast.error(err.response?.data?.error || "Registration failed");
            set({ error: err.message });
        } finally {
            set({ loading: false });
        }
    },

    login: async (username, password) => {
        set({ loading: true, error: null });
        const res = await axios.post(
            `${authApi}/login`,
            { username, password },
            { validateStatus: () => true }
        );

        if (res.status === 200) {
            Cookies.set("username", username);
            toast.success(res.data.message || "Login successful");
            set({ loggedIn: true });
        } else if (res.status === 401) {
            toast.error(res.data.error || "Invalid credentials");
            set({ error: res.data.error || "Unauthorized" });
        } else {
            toast.error("Error while verifying credentials");
            set({ error: "Unknown login error" });
        }

        set({ loading: false });
    },

    logout: () => {
        set({ loggedIn: false });
        toast.success("Logged out");
    },
}));

export default useAuthStore;
