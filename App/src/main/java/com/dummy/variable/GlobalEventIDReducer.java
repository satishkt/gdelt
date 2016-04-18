package com.dummy.variable;

import com.google.common.collect.Iterables;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;

/**
 * Created by Satish on 4/18/16.
 */
public class GlobalEventIDReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

    Logger logger = LoggerFactory.getLogger(getClass());

    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        int count = Iterables.size(values);
        context.write(key, new IntWritable(count));

    }
}
