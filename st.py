import os
import webbrowser

import streamlit as st
from executer import run_test,load_json_from_file


def run_app():

    st_json=load_json_from_file("st.json")
    st.title("RoboTester")
    st.subheader("Form Tutorial")
    form1=st.form(key='form1')
    all_tests_list=[]
    tests_path = st_json["tests_path"]
    tests_config=st_json["test_config"]
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