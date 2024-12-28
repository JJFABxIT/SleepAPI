from flask import Flask, jsonify
import os
import queue
import threading
import time

app = Flask(__name__)

# Creates the task queue
task_queue = queue.Queue()

# The worker function to process tasks in the queue defined above
def worker():
    while True:
        task = task_queue.get()
        if task == "sleep":
            time.sleep(1)
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif task == "shutdown":
            os.system("shutdown /s /t 1")
        task_queue.task_done()

# Starts the worker thread        
threading.Thread(target=worker, daemon=True).start()

# Exposed endpoint to sleep PC
@app.route('/sleep', methods=['POST'])
def sleep():
    task_queue.put("sleep")
    
    response = jsonify({"status": "PC is going to sleep."})
    response.status_code = 200
    return response 

# Exposed endpoint to shutdown PC
@app.route('/shutdown', methods=['POST'])
def shutdown():
    task_queue.put("shutdown")
    
    response = jsonify({"status": "PC is shutting down."})
    response.status_code = 200
    return response 
