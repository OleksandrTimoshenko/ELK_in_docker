from invoke import task
import os

@task
def start_logger(c):
    os.system("python3 ./host_metrics_app/main.py &")

@task
def start_elastic(c):
    running_containers = c.run("docker ps --format '{{.Names}}'").stdout.strip().split("\n")
    if "elasticsearch" not in running_containers:
        c.run("docker-compose up --no-deps elasticsearch -d")
        c.run("sleep 20")

@task
def update_password(c, user):
    res = c.run(f"echo 'y' | docker exec -i elasticsearch  /usr/share/elasticsearch/bin/elasticsearch-reset-password -u {user} -a")
    return res.stdout.strip().split(" ")[-1]

@task
def setup_credentials(c, kibana_pass, elastic_pass):
    c.run( "echo 'KIBANA_USERNAME=kibana_system' > .env")
    c.run(f"echo 'KIBANA_PASSWORD=\"{kibana_pass}\"\n' >> .env")
    c.run( "echo 'LOGSTASH_USERNAME=elastic' >> .env")
    c.run(f"echo 'LOGSTASH_PASSWORD=\"{elastic_pass}\"' >> .env")

@task
def start_another_containers(c):
    c.run("docker-compose up --no-recreate")

@task
def start(c):
    start_logger(c)
    start_elastic(c)
    kibana_pass =  update_password(c, "kibana_system")
    elastic_pass = update_password(c, "elastic")
    setup_credentials(c, kibana_pass, elastic_pass)
    start_another_containers(c)
