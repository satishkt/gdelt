package com.dummy.variable;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.util.StringTokenizer;

/**
 * Created by Satish on 4/17/16.
 */
public class GlobablEventIDMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

    Logger logger = LoggerFactory.getLogger(getClass());

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        logger.debug("Inside the map method with the key {} and value {} ", key.toString(), value.toString());
        String line = value.toString();
        StringTokenizer tokenizer = new StringTokenizer(value.toString(), "\t");
        //logger.info("Parsing event id {} ",tokenizer.nextToken());
        Text dayOfEvent = new Text(tokenizer.nextToken());
        //logger.info("Parsing token {} ", dayOfEvent.toString());
        context.write(dayOfEvent, new IntWritable(1));


    }
}
