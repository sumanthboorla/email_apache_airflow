from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta 
from clean import pre_process
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from filter import filter_function
default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 6, 25),  # Correct order: year, month, day
    "retries": 2,
    "retry_delay": timedelta(seconds=15)
}

 
with DAG(
    dag_id='email_dag',
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    # retry_delay = timedelta(seconds=15)
) as dag:
#task 1 : checkup
    check_file = BashOperator(
        task_id='check_file',
        bash_command="shasum ~/ip_files/countries.csv"
    )
 #task2 : cleanup
    pre_process = PythonOperator(
        task_id='pre_process',
        python_callable = pre_process
    )

    # task3 : filter the data
    filter_task = PythonOperator(
        task_id= 'filter_data',
        python_callable = filter_function

    )
    #task4 : sending email
    email = EmailOperator(
        task_id='send_email',
        to='sumanthb31@gmail.com',
        subject='Daily report generated',
        html_content='<p> Your reports generated sucessfully, Thanks '
    )

    check_file >> pre_process >> filter_task>>email
