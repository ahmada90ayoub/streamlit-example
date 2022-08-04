import os
import subprocess
import json

class Executer:

    def execute(self,command,timeout=None):
        print(f"command={command}")
        cmd = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = cmd.communicate(timeout=timeout)
        return out,err

def run_test(robot_test_name):

    cmd=[]
    cmd.append(os.path.normpath(r"C:\RoboTester\RoboTesterAuto\env\Scripts\python"))
    cmd.append(os.path.normpath(r"C:\RoboTester\RoboTesterAuto\roboframework\robotframework\src\robot\__main__.py"))
    cmd.append("-P")
    cmd.append("C:\RoboTester\RoboTesterAuto")
    cmd.append("--outputdir")
    output = f"\\\\10.4.0.102\\swgwork1\\ahayoub\\work\\robot_results\\gui_output\\{robot_test_name}"
    #output = self.test_output_dir
    cmd.append(os.path.normpath(output))
    cmd.append("--loglevel DEBUG:INFO")
    robot=f"C:\\RoboTester\\RoboTesterAuto\\Gotests\\projectcloud\\tests\\{robot_test_name}.robot"
    cmd.append(os.path.normpath(robot))
    command=" ".join(cmd)
    print(f"command= {command}")
    exe1=Executer()
    out, err = exe1.execute(command)
    #print(f"out={out}")
    log_output= os.path.join(output,"log.html")
    print(f"log = {log_output}")
    return log_output

def load_json_from_file(json_file):
    try:
        with open(json_file, 'r') as fs:
            return json.load(fs)
    except FileNotFoundError:
        raise