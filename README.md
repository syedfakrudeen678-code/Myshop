# Myshop

A Django e-commerce application featuring asynchronous email notification dispatch via Celery, RabbitMQ message brokerage, session-based cart management, and real-time task monitoring with Flower.

## Django E-Commerce Platform with Asynchronous Messaging

A robust e-commerce web application built with **Django**, designed to handle user shopping sessions, order creation, and asynchronous background processing using **Celery** and **RabbitMQ**.

### Key Features

* **Cart & Order Management:** Dynamic session-based shopping cart supporting real-time additions, updates, and item removal, seamlessly integrated into a multi-step checkout flow.
* **Asynchronous Notification Pipeline:** Background task execution offloads email notifications upon order placement, preventing request blocking and optimizing user response times.
* **Message Brokerage & Scheduling:** Dockerized **RabbitMQ** instance serving as the message broker, paired with a Windows-compatible single-threaded Celery (`solo` pool) execution environment.
* **Task Monitoring:** Integrated **Flower** dashboard tracking worker node health, task lifecycle states (SUCCESS/FAILURE), and execution latency in real-time.
