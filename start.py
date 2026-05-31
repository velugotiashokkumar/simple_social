import subprocess

# Start FastAPI
fastapi_process = subprocess.Popen([
    "uv",
    "run",
    ".\main.py"
])

# Start Streamlit
streamlit_process = subprocess.Popen([
    "uv",
    "run",
    "streamlit",
    "run",
    "app\\frountend.py"
])

try:
    fastapi_process.wait()
    streamlit_process.wait()

except KeyboardInterrupt:
    fastapi_process.terminate()
    streamlit_process.terminate()