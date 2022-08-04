import os
import webbrowser
import subprocess
import json

import streamlit as st
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


def run_app():

    #st_json=load_json_from_file("https://github.com/ahmada90ayoub/streamlit-example/blob/93509104e28635513eb4f47a22e8d0b7b7aa4cd5/st.json")
    st.title("RoboTester")
    st.subheader("Form Tutorial")
    form1=st.form(key='form1')
    all_tests_list=[]
    #tests_path = st_json["tests_path"]
    #tests_config=st_json["test_config"]   
    tests_path = "C:\\RoboTester\\RoboTesterAuto\\GoTests\\projectcloud\\tests"
    tests_config="C:\\RoboTester\\RoboTesterAuto\\GoTests\\projectcloud\\tests_config"
    for filename in os.listdir(tests_path):
        all_tests_list.append(filename.split(".")[0])
    test_name = form1.selectbox("Test", all_tests_list)
    run_test_button = form1.form_submit_button("run test")



    if run_test_button:
        #output_log=run_test(test_name)
        output_log="a link"
        #st.success(f"output _ log : \{output_log}")


        with  st.form(key='form2'):
            col1,col2= st.columns([2,1])
            with col1:
                st.success(f"output _ log : \{output_log}")
                json_file_path = os.path.join(tests_config, f"{test_name}.json")
                cont = load_json_from_file(json_file_path)
                st.json(cont)
            with col2:
                st.form_submit_button("got_to_log_button",on_click=func1(output_log))
                robot_file_path = os.path.join(tests_path, f"{test_name}.robot")
                with open(robot_file_path, "r") as f:
                    data = f.readlines()
                all_data = "\n".join(data)
                st.text(all_data)


def func1(output_log):
    print("yes2")
    #webbrowser.open_new_tab("\\\\10.4.0.102\\swgwork1\\ahayoub\\work\\robot_results\\gui_output\\TestSample\\log.html")

    #webbrowser.open_new_tab(output_log)












if __name__ == "__main__":
    run_app()
