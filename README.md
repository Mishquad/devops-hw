
# HW-4
Все yml файлы в папке src
## Скрины
![1](./screens/airflow.jpg)
![3](./screens/scre1.png)
![3](./screens/scre2.png)
![3](./screens/scre6.png)
![3](./screens/scre4.png)
![3](./screens/scre5.png)


### Манифесты

```
- kubectl create -f postgres_configmap.yml
- kubectl create -f postgres_secret.yml
- kubectl create -f airflow_configmap.yml
- kubectl create -f airflow_secret.yml
- kubectl create -f airflow_postgres.yml
- kubectl create -f airflow_init.yml
- kubectl create -f airflow_scheduler.yml
- kubectl create -f airflow_webserver.yml
```
