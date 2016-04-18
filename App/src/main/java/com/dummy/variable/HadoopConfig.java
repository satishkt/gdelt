package com.dummy.variable;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.ImportResource;
import org.springframework.data.hadoop.config.annotation.EnableHadoop;

/**
 * Created by Satish on 4/18/16.
 */
@Configuration
@EnableHadoop
@ImportResource("classpath:hadoop-config.xml")
public class HadoopConfig {



}
