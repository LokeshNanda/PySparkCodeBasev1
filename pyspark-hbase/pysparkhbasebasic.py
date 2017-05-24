#!/usr/bin/env python

from pyspark import SparkContext


def get_hbase_as_rdd(host,tablename):
	sc = SparkContext(appName="hbase2rdd")
	conf = {"hbase.zookeeper.quorum": host, "hbase.mapreduce.inputtable": tablename, "zookeeper.znode.parent": "/hbase-unsecure"}
	print "Connecting to host: " + conf["hbase.zookeeper.quorum"] + " table: " + conf["hbase.mapreduce.inputtable"]
	keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"
	valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"
	hbase_rdd = sc.newAPIHadoopRDD("org.apache.hadoop.hbase.mapreduce.TableInputFormat","org.apache.hadoop.hbase.io.ImmutableBytesWritable","org.apache.hadoop.hbase.client.Result",keyConverter=keyConv,valueConverter=valueConv,conf=conf)
	return hbase_rdd

if __name__ == "__main__":

	rddh = get_hbase_as_rdd("lokesh.dev.local","test")
	print rddh.count()
	print rddh.collect()
