# Setup project
1. Start python app for generate logs - `python3 ./host_metrics_app/main.py`
2. Create `.env` file - `cp .env.example .env`
2. Start docker containers - `docker-compose up`
3. Go to [kibana](http://localhost/)
4. Setup Kibana Dashboard:
- Create index (Discover -> Create index pattern) ![image](images/index_setup.png)
- Go to Discover
5. See your data ![image](images/data_sample.png)