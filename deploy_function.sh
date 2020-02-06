gcloud functions deploy read_people --region europe-west1 --timeout 300s --runtime python37 --trigger-http --set-env-vars=MYSQL_USER=$SQL_CLOUD_USER,MYSQL_PASSWORD=$SQL_CLOUD_PASSWORD,MYSQL_SOCKET_PATH=$SQL_SOCKET_PATH,MYSQL_RAISE_ON_WARNINGS=$SQL_CLOUD_RAISE_WARNINGS,MYSQL_DATABASE=$SQL_CLOUD_DATABASE