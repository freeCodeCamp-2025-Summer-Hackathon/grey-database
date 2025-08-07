
# WorkWave
A job-hunting journal for tracking applications and interviews.

**Link to project:** http://recruiters-love-seeing-live-demos.com/

![alt tag](http://placecorgi.com/1200/650)

## How It's Made:

**Tech used:** React, Python, Flask, MongoDB.

Here's where you can go to town on how you actually built this thing. Write as much as you can here, it's totally fine if it's not too much just make sure you write *something*. If you don't have too much experience on your resume working on the front end that's totally fine. This is where you can really show off your passion and make up for that ten fold.

## How To Get Up And Running:


#### Backend
- Python >= **3.7** (tested with **3.13.5**)
- `pip` (Python package manager)

#### Frontend
- Node.js >= **20.19.0** (required by Vite 7.x)
- `npm` (bundled with Node.js)
- Recommended: [nvm](https://github.com/coreybutler/nvm-windows/releases) for managing Node versions


### Backend Setup

1. Navigate to the backend folder  
`cd backend`

2. *OPTIONAL*: Create and activate a virtual environment  
`python -m .venv .venv`  
`.\.venv\Scripts\activate` (on Windows)  
`source .venv/bin/activate` (on Linux/Mac)

3. Install dependencies  
`pip install -r requirements.txt`

4. Run the backend server  
`python app.py`

If you encounter issues starting the backend, ensure any required environment variables (e.g., `FLASK_ENV=dev`) are set. You may also try running:  `flask run`


### Frontend Setup

1. Ensure correct Node version  
`node -v`  
If below 20.19.0, install and use the correct version with nvm:  
`nvm install 20.19.0`  
`nvm use 20.19.0`

2. Navigate to the frontend folder  
`cd FrontEnd`

3. Install frontend dependencies  
`npm install`

4. Check and configure `.env`  
Ensure `.env` file contains:  
`VITE_API_URL="http://127.0.0.1:5000"`

This points the frontend to the backend API.

5. Run the frontend server  
`npm run dev`

### Notes

Run backend and frontend in separate terminal windows.  
Make sure no other services are using ports 5000 (backend) or 5173 (frontend).  
You may modify `.env` to change API URLs if needed.

## Optimizations
*(optional)*

You don't have to include this section but interviewers *love* that you can not only deliver a final product that looks great but also functions efficiently. Did you write something then refactor it later and the result was 5x faster than the original implementation? Did you cache your assets? Things that you write in this section are **GREAT** to bring up in interviews and you can use this section as reference when studying for technical interviews!

## Lessons Learned:

No matter what your experience level, being an engineer means continuously learning. Every time you build something you always have those *whoa this is awesome* or *fuck yeah I did it!* moments. This is where you should share those moments! Recruiters and interviewers love to see that you're self-aware and passionate about growing.

<div align='center'>

## 👥 Team Members

| Name | Discord Username |
|------|------------------|
| **akhil** | `@akhil` |
| **Quasar(Sidhant)** | `@Quasar(Sidhant)` |
| **ConstantLynx** | `@ConstantLynx` |
| **devanshu** | `@devanshu` |
| **unmani** | `@unmani` |
| **ctrl2life** | `@ctrl2life` |
| **SyedUmairCodes** | `@SyedUmairCodes` |
| **Gurkirat-Singh** | `@Gurkirat-Singh` |
| **vinay** | `@vinay` |
| **Dimi** | `@Dimi` |
| **Dinesh kumar** | `@Dinesh kumar` |

---

*Building something amazing together! 🚀*

</div>
