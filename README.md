# HW-4

## Скрины
![1](./screens/airflow.jpg)
![2](./screens/jupyter.jpg)
![3](./screens/first_screen.jpg)
![4](./screens/second_screen.jpg)

## Инструкция по использованию
### Применение конфигураций

kubectl apply -f airflow-configmap.yml

kubectl apply -f airflow-deployment.yml

kubectl apply -f jupyter-configmap.yml

kubectl apply -f jupyter-deployment.yml

### Верификация Pod'а

kubectl get pods

kubectl get services

### Доступ к сервисам из кубера

minikube service jupyter-service --url

minikube service airflow-service --url

