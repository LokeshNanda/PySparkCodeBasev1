
# Create sample Hbase Table:

create 'test', 'cf1'

put 'test', 'row-1', 'cf1:name', 'lokesh'

put 'test', 'row-1', 'cf1:age', '26'

put 'test', 'row-2', 'cf1:age', '27'

put 'test', 'row-2', 'cf1:name', 'pitamber'


# Spark-submit command:

spark-submit --jars  /usr/hdp/current/hbase-client/lib/hbase-client.jar,/usr/hdp/current/hbase-client/lib/hbase-common.jar,/usr/hdp/current/hbase-client/lib/hbase-server.jar,/usr/hdp/current/hbase-client/lib/hbase-protocol.jar,/usr/hdp/current/spark-client/lib/spark-examples-1.6.2.2.4.3.0-227-hadoop2.7.1.2.4.3.0-227.jar,/usr/hdp/2.4.3.0-227/hbase/lib/guava-12.0.1.jar /home/lokesh/testsublime.py
