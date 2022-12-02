from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092", # Brokers
    client_id='rajaApp1'
)

topic_list = []
topic_list.append(NewTopic(name="topic_user_location", num_partitions=2, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)