from elasticsearch import Elasticsearch

ELASTIC_URL = 'https://ssei-knowledge-base.rastaiha.ir'
ELASTIC_USERNAME = 'elastic'
ELASTIC_PASSWORD = 'dXiC5KlY0ABcia1mzYu1M7qZKTFVJdWN'

# اتصال به Elasticsearch با احراز هویت
es = Elasticsearch(
    ELASTIC_URL,
    basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD)
)

# بررسی اتصال
if es.ping():
    print("Connected to Elasticsearch!")
else:
    print("Failed to connect to Elasticsearch.")
