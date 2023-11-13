# Requirements
- Docker (>=24.0.7)
- Docker Compose (>=v2.23.0)
- Python3
- Invoke (>=1.4.1) (if you want to use Invoke setup)

# Setup project
### Invoke setup
`invoke start`

### Manual setup
1. Start python app for generate logs - `python3 ./host_metrics_app/main.py`
2. Create `.env` file - `cp .env.example .env`
3. Start Elasticsearch container - `docker-compose up --no-deps elasticsearch -d`
4. Setup passwords for users:
- `echo 'y' | docker exec -i elasticsearch  /usr/share/elasticsearch/bin/elasticsearch-reset-password -u kibana_system -a`
- `echo 'y' | docker exec -i elasticsearch  /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic -a`
6. Update passwords in .env file (it`s better for now using elastic user credentials for logstash)
7. Start all containers - `docker-compose up --no-recreate`

### Kibana setup
1. Go to [kibana](http://localhost/) (You can find credentials in generated .env file, use `elastic` user)
2. Setup Kibana Dashboard:
- Create index (Discover -> Create data view) ![image](images/index_setup.png)
- Go to Discover
3. See your data ![image](images/data_sample.png)

### Second start
If you didn\`t delete volumes than you can use command `docker-compose up` for recreate containers.

### TODO:
1. setup Elasticsearch with more than one node